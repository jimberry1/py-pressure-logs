from abc import ABC, abstractmethod
from collections import defaultdict
from itertools import dropwhile, takewhile
import py_pressure_logs.regex_utils as regex_utils
from typing import Dict, List
import csv


class Experiment(ABC):
    TIME_KEY = "time"
    PRESSURE_KEY = "pressure"
    OUTPUT_KEY = "output"
    ROW_NUMBER = "row_number"

    logs: List[Dict[str, str]]
    experiments: Dict[str, Dict]
    washes: Dict[str, Dict]
    experiment_summaries: Dict[str, Dict]
    wash_summaries: Dict[str, Dict]

    def __init__(self, file_path, *, file_contents=None):
        self.logs = (
            self.parse_csv(file_path)
            if file_path
            else self.parse_unstructured_file_rows(file_contents)
        )
        self.experiments = self.extract_experiments(self.logs)
        self.washes = self.extract_washes(self.logs)

    def is_time_field(self, header):
        pattern = r"time"
        return regex_utils.regex_match(pattern, header, ignore_case=True)

    def is_output_field(self, header):
        pattern = r"output"
        return regex_utils.regex_match(pattern, header, ignore_case=True)

    def select_common_keys(self, raw_csv_row):
        """Selects common keys shared between all experiments.
        Returns a map of data to be combined with experiment specific keys."""
        formatted_row = {}
        for key, val in raw_csv_row.items():
            if self.is_time_field(key):
                formatted_row[self.TIME_KEY] = val
                continue
            elif self.is_output_field(key):
                formatted_row[self.OUTPUT_KEY] = val
                continue
        return formatted_row

    def transform_row(self, row, row_number):
        """Transforms a row from raw data to the desired rows with standardised names"""
        return {
            **self.select_common_keys(row),
            **self.select_experiment_keys(row),
            self.ROW_NUMBER: row_number,
        }

    def parse_unstructured_file_rows(self, rows):
        """In the event that data is preloaded, instead of being opened with a file path,
        transforms rows into structured logs."""
        return [
            self.transform_row(row, row_number)
            for row_number, row in enumerate(rows, start=1)
        ]

    def parse_csv(self, file_path):
        """
        Parses a CSV file, renames headers, and selects specific keys.

        :param file_path: Path to the CSV file.
        :return: List of dictionaries with renamed and filtered keys.
        """
        parsed_data = []

        with open(file_path, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            parsed_data = [
                self.transform_row(row, row_number)
                for row_number, row in enumerate(reader, start=2)
            ]

        return parsed_data

    def extract_experiments(self, logs):
        """Iterates through the logs for the experimental run, extracting those relevant to experiments
        and grouping them in an associative structure."""
        log_iterator = iter(logs)
        grouped_experiment_logs = {}
        try:
            while True:
                logs_from_exp_start = dropwhile(
                    lambda row: not self.is_start_of_experiment(row), log_iterator
                )
                experiment_logs = list(
                    takewhile(
                        lambda row: not self.is_end_of_experiment(row),
                        logs_from_exp_start,
                    )
                )

                if not experiment_logs or len(experiment_logs) == 0:
                    break

                experiment_number = self.get_experiment_number_from_start_row(
                    experiment_logs[0]
                )
                grouped_experiment_logs[experiment_number] = experiment_logs

        except StopIteration:
            print("The experimental logs have been exhausted")

        return grouped_experiment_logs

    def extract_washes(self, logs):
        """Iterates through the logs for the experimental run, extracting those relevant
        to washes and grouping in an associative structure."""
        log_iterator = iter(logs)
        grouped_wash_logs = {}
        try:
            while True:
                logs_from_wash_start = dropwhile(
                    lambda row: not self.is_start_of_wash(row), log_iterator
                )
                wash_logs = list(
                    takewhile(
                        lambda row: not self.is_end_of_wash(row), logs_from_wash_start
                    )
                )

                if not wash_logs or len(wash_logs) == 0:
                    break

                experiment_number = self.get_wash_experiment_number(wash_logs)
                grouped_wash_logs[experiment_number] = wash_logs

        except StopIteration:
            print("The experimental logs have been exhausted")

        return grouped_wash_logs

    def summarise_experiments(self):
        """Given the logs for an experiment, calculates the maximum pressure values for each pump"""
        experiment_summary = {}
        for experiment_number, experiment_logs in self.experiments.items():

            grouped_values = defaultdict(list)
            for log_line in experiment_logs:
                for pump_key, pressure_value in log_line[self.PRESSURE_KEY].items():
                    grouped_values[pump_key].append(float(pressure_value))

            max_values = {key: max(values) for key, values in grouped_values.items()}
            experiment_summary[experiment_number] = max_values

        self.experiment_summaries = experiment_summary
        return experiment_summary

    def summarise_washes(self):
        """Given the logs for a wash, calculates the maximum pressure values for each pump"""
        wash_summary = {}
        for experiment_number, wash_logs in self.washes.items():

            grouped_values = defaultdict(list)
            for log_line in wash_logs:
                for pump_key, pressure_value in log_line[self.PRESSURE_KEY].items():
                    grouped_values[pump_key].append(float(pressure_value))

            max_values = {key: max(values) for key, values in grouped_values.items()}
            wash_summary[experiment_number] = max_values

        self.wash_summaries = wash_summary
        return wash_summary

    def _create_output_headers(self):
        """Creates the header row of the output csv dynamically from the pressure pump names"""
        headers = ["Experiment Number"]
        pump_names = [
            f"Maximum {pump_name}"
            for pump_name in self.logs[0][self.PRESSURE_KEY].keys()
        ]
        headers.extend(pump_names)
        headers.extend(["Start row number", "End row number"])
        return headers

    def _create_output_row(self, experiment_number, summary, name_override=None):
        """Transforms inputs into a single csv row to be output"""
        experiment_name = name_override if name_override else experiment_number
        row_data = [experiment_name]

        pump_max_pressures = [
            pump_max_pressure for pump_max_pressure in summary.values()
        ]
        row_data.extend(pump_max_pressures)
        row_data.append(self.experiments[experiment_number][0]["row_number"])
        row_data.append(self.experiments[experiment_number][-1]["row_number"])
        return row_data

    def output_summary(self):
        experiment_summaries = self.summarise_experiments()

        headers = self._create_output_headers()
        data = [headers]

        for experiment_number, experiment_summary in experiment_summaries.items():
            row_data = self._create_output_row(experiment_number, experiment_summary)
            data.append(row_data)

        wash_summaries = self.summarise_washes()
        for wash_number, wash_summary in wash_summaries.items():
            wash_name = f"{wash_number}-wash"
            row_data = self._create_output_row(
                wash_number, wash_summary, name_override=wash_name
            )
            data.append(row_data)

        return data

    def output_csv(self, output_filename="output"):
        """A crude implementation to output data from the experiment run"""
        data = self.output_summary()
        with open(f"{output_filename}.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)

    @abstractmethod
    def select_experiment_keys(self, row):
        """Experiment specific transformation function to extract important values"""
        pass

    @abstractmethod
    def get_experiment_number_from_start_row(self, start_row):
        """Experiment specific regex match function to identify experiment number from first row of experiment logs"""
        pass

    @abstractmethod
    def is_start_of_experiment(self, row):
        """Experiment specific regex match function to identify whether a row marks the start of an experiment"""
        pass

    @abstractmethod
    def is_end_of_experiment(self, row):
        """Experiment specific regex match function to identify whether a row marks the end of an experiment"""
        pass

    @abstractmethod
    def is_start_of_wash(self, row):
        """Experiment specific regex match function to identify whether a row marks the start of a wash"""
        pass

    @abstractmethod
    def is_end_of_wash(self, row):
        """Experiment specific regex match funnction to identify whether a row marks the end of a wash"""

    @abstractmethod
    def get_wash_experiment_number(self, logs_for_wash):
        """Experiment specific regex match function to return the experiment number from the logs for the wash"""
