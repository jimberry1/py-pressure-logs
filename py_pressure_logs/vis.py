import plotly.graph_objects as go
from collections import defaultdict


def visualise_experiment(experiment_logs):
    row_numbers = []
    pressures_by_pump = defaultdict(list)

    for log_line in experiment_logs:

        row_numbers.append(log_line["row_number"])

        for pump_key, pressure_value in log_line["pressure"].items():
            pressures_by_pump[pump_key].append(float(pressure_value))

    # Create the plot
    fig = go.Figure()

    # Add a line for each pressure key
    for handler, pressures in pressures_by_pump.items():
        fig.add_trace(
            go.Scatter(x=row_numbers, y=pressures, mode="lines", name=handler)
        )

    # Update layout
    fig.update_layout(
        title="System pressure",
        xaxis_title="Experiment log row #",
        yaxis_title="Pressure (bar)",
        template="plotly_dark",
    )

    # Show the plot
    fig.show()
