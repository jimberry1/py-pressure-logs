import streamlit as st
import pandas as pd
from py_pressure_logs.sunshine_experiment import SunshineExperiment
from py_pressure_logs.sunscreen_experiment import SunscreenExperiment
import re
from py_pressure_logs.regex_utils import regex_match
import py_pressure_logs.vis as vis

PROTOCOL_NAME = "file_contents"
SUNSHINE_PROTOCOL_NAME = "sunshine"
SUNSCREEN_PROTOCOL_NAME = "sunscreen"


def main():
    st.session_state[PROTOCOL_NAME] = None
    # Options with a placeholder
    options = [
        "Select one",
        SUNSHINE_PROTOCOL_NAME,
        SUNSCREEN_PROTOCOL_NAME,
    ]

    # Create the selectbox
    selected_option = st.selectbox("Choose an experimental protocol:", options)

    # Check if a valid option is selected
    if selected_option == "Select one":
        st.write("Please select a valid option.")
    else:
        st.session_state[PROTOCOL_NAME] = selected_option

    st.title("Logs Viewer")
    st.write(
        "Upload a CSV file from the Sunshine or Sunscreen protocol to view its contents."
    )
    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None and st.session_state[PROTOCOL_NAME]:
        try:
            # Read CSV into a DataFrame
            df = pd.read_csv(uploaded_file)
            st.write("## All Logs")
            st.dataframe(df)
            df = df.astype(str)

            data_as_dicts = df.to_dict(orient="records")
            # print(f"this is my data_as_dicts {data_as_dicts[0]}")
            exp = (
                SunscreenExperiment(None, file_contents=data_as_dicts)
                if st.session_state[PROTOCOL_NAME] == SUNSCREEN_PROTOCOL_NAME
                else SunshineExperiment(None, file_contents=data_as_dicts)
            )
            data = exp.output_summary()
            # Convert back to DataFrame to display

            # Extract headers and data
            headers = data[0]  # First row as column names
            data = data[1:]  # Remaining rows as data

            # Create DataFrame
            new_df = pd.DataFrame(data, columns=headers)

            # Display the table in Streamlit
            st.write("## Summarised Results:")
            new_df

            st.write("## See Experimental Graphs:")
            if st.button("Full Protocol", key="button-index-all"):
                vis.visualise_experiment(exp.logs)
            num_columns = 4
            columns = st.columns(num_columns)  #
            for i, row in new_df.iterrows():
                exp_num_pattern = r"(\d+)"
                exp_name = row["Experiment Number"]
                exp_num = re.search(exp_num_pattern, row["Experiment Number"]).group(0)
                col = columns[i % num_columns]
                with col:
                    if st.button(f"{exp_name}", key=f"button-index-{exp_name}"):
                        is_wash = regex_match(r"wash", exp_name, ignore_case=True)
                        logs = (
                            exp.experiments[exp_num]
                            if not is_wash
                            else exp.washes[exp_num]
                        )
                        vis.visualise_experiment(logs)

        except Exception as e:
            st.error(f"Error reading the CSV file: {e}")


if __name__ == "__main__":
    main()
