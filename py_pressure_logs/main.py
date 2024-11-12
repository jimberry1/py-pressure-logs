import py_pressure_logs.sunshine_experiment as sunshine_exp
import py_pressure_logs.sunscreen_experiment as sunscreen_exp
import argparse

SUNSHINE_PROTOCOL_NAME = "sunshine"
SUNSCREEN_PROTOCOL_NAME = "sunscreen"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Py Pressure Logs",
        description="A script to analyse experimental logs from Sunshine and Suncreen protocols and group them by experiment, tracking the maximum pressure for each pump throughout the protocol",
        epilog="""
        Example dist usage: 'py_pressure_logs sunshine /Users/YOUR-USER/path/to/file/2024-03-04_17h00m11s_full.csv -o sunshine-analysis-output'
        Example usage running locally: 'poetry run python main.py sunshine /Users/YOUR-USER/path/to/file/2024-03-04_17h00m11s_full.csv -o output-file-name'""",
    )

    parser.add_argument(
        "experimental_protocol",
        type=str,
        choices=[SUNSHINE_PROTOCOL_NAME, SUNSCREEN_PROTOCOL_NAME],
        help=f"Select an experimental protocol for the analysis. Currently {SUNSCREEN_PROTOCOL_NAME} or {SUNSHINE_PROTOCOL_NAME} are supported.",
    )
    parser.add_argument(
        "filepath",
        type=str,
        help="The relative path to the input csv file, e.g. ./Documents/output/2024_11_03.csv",
    )
    parser.add_argument(
        "-o",
        "--output_filename",
        type=str,
        default="py_pressure_logs_output",
        help="Optionally specify the output name of the file generated from this execution",
    )

    args = parser.parse_args()

    filepath = args.filepath

    experiment_protocol = sunshine_exp.SunshineExperiment(args.filepath)

    if args.experimental_protocol == SUNSHINE_PROTOCOL_NAME:
        experiment_protocol = sunshine_exp.SunshineExperiment(args.filepath)
    else:
        experiment_protocol = sunscreen_exp.SunscreenExperiment(args.filepath)

    experiment_protocol.output_csv(output_filename=args.output_filename)
