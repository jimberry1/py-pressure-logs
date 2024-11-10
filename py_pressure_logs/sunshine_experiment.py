from collections import defaultdict
from itertools import takewhile, dropwhile
import re
import py_pressure_logs.regex_utils as regex_utils

TIME_KEY = "time"
PRESSURE_KEY = "pressure"
OUTPUT_KEY = "output"


def is_time_field(header):
    pattern = r"time"
    return regex_utils.regex_match(pattern, header, ignore_case=True)


def is_pressure_field(header):
    pattern = r".*(\d+).*current pressure.*"
    return regex_utils.regex_match(pattern, header, ignore_case=True)


def is_output_field(header):
    pattern = r"output"
    return regex_utils.regex_match(pattern, header, ignore_case=True)


def transform_row(row):
    """Transforms a row from all csv data to a collection of log lines"""
    formatted_row = {PRESSURE_KEY: {}}
    for key, val in row.items():
        if is_time_field(key):
            formatted_row[TIME_KEY] = val
            continue
        elif is_output_field(key):
            formatted_row[OUTPUT_KEY] = val
            continue
        elif is_pressure_field(key):
            formatted_row[PRESSURE_KEY][key] = val
            continue

    return formatted_row


def is_start_of_experiment(row):
    row_output = row[OUTPUT_KEY]
    pattern = r".*Experiment \d+:.*Experiment Preparation Begun"
    return regex_utils.regex_match(pattern, row_output, ignore_case=True)


def is_end_of_experiment(row):
    row_output = row[OUTPUT_KEY]
    pattern = r"Experiment run completed"
    return regex_utils.regex_match(pattern, row_output, ignore_case=True)


def get_experiment_number_from_start_row(row):
    row_output = row[OUTPUT_KEY]
    pattern = r".*Experiment (\d+):.*Experiment Preparation Begun"
    match = re.search(pattern, row_output, re.IGNORECASE)

    if match:
        return match.group(1)
    else:
        raise Exception(f"no experiment number found for row {row}")


def extract_experiment_logs(rows):
    """Returns all rows for an experiment, dropping all rows up to the start of the experiment"""
    logs_from_experiment_start = dropwhile(
        lambda row: not is_start_of_experiment(row), rows
    )

    experiment_rows = takewhile(
        lambda row: not is_end_of_experiment(row), logs_from_experiment_start
    )

    return list(experiment_rows)


def group_into_experiments(rows):
    row_iterator = iter(rows)
    grouped_results = {}
    try:
        while True:
            experiment_rows = extract_experiment_logs(row_iterator)
            if not experiment_rows or len(experiment_rows) == 0:
                break

            experiment_number = get_experiment_number_from_start_row(experiment_rows[0])
            grouped_results[experiment_number] = experiment_rows

    except StopIteration:
        print("The experimental logs have been exhausted")

    return grouped_results


def summarise_experiment(experiment_logs):
    """Given the logs for an experiment, calculates the maximum pressure values for each pump"""
    grouped_values = defaultdict(list)

    for log_line in experiment_logs:
        for pump_key, pressure_value in log_line[PRESSURE_KEY].items():
            grouped_values[pump_key].append(float(pressure_value))

    max_values = {key: max(values) for key, values in grouped_values.items()}

    return max_values
