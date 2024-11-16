import streamlit as st
import pandas as pd
from py_pressure_logs.sunshine_experiment import SunshineExperiment

FILE_CONTENTS_KEY = "file_contents"


def main():
    st.title("CSV Viewer")

    st.write("Upload a CSV file to view its contents.")

    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    # Check if `data` is already stored in session state
    if FILE_CONTENTS_KEY not in st.session_state:
        st.session_state[FILE_CONTENTS_KEY] = None  # Initialize it to None

    if uploaded_file is not None:
        try:
            # Read CSV into a DataFrame
            df = pd.read_csv(uploaded_file)
            st.write("### Input data:")
            st.dataframe(df)
            df = df.astype(str)

            data_as_dicts = df.to_dict(orient="records")
            # print(f"this is my data_as_dicts {data_as_dicts[0]}")
            exp = SunshineExperiment(None, file_contents=data_as_dicts)
            data = exp.output_summary()
            # Convert back to DataFrame to display

            # Extract headers and data
            headers = data[0]  # First row as column names
            data = data[1:]  # Remaining rows as data

            # Create DataFrame
            new_df = pd.DataFrame(data, columns=headers)

            # Display the table in Streamlit
            st.write("### Summary:")
            st.dataframe(new_df)

            # # Display additional statistics or visualizations if needed
            # st.write("### Data Summary:")
            # st.write(df.describe())
        except Exception as e:
            st.error(f"Error reading the CSV file: {e}")


if __name__ == "__main__":
    main()
