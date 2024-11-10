import csv
import py_pressure_logs.sunshine_experiment as exp


def parse_csv(file_path):
    """
    Parses a CSV file, renames headers, and selects specific keys.

    :param file_path: Path to the CSV file.
    :return: List of dictionaries with renamed and filtered keys.
    """
    parsed_data = []

    with open(file_path, mode="r", newline="", encoding="utf-8") as csvfile:
        # Read data
        reader = csv.DictReader(csvfile)

        parsed_data = [
            {
                **exp.transform_row(row),
                "row_number": row_number,
            }
            for row_number, row in enumerate(reader, start=2)
        ]

    grouped_by_experiment_number = exp.group_into_experiments(parsed_data)

    return grouped_by_experiment_number


if __name__ == "__main__":
    file_path = "resources/sunshine/2024-03-04_17h00m11s_full.csv"

    experiments = parse_csv(file_path)

    summary = {
        experiment_number: exp.summarise_experiment(experimental_logs)
        for experiment_number, experimental_logs in experiments.items()
    }
