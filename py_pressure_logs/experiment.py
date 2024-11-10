from abc import ABC, abstractmethod
from collections import defaultdict
import py_pressure_logs.regex_utils as regex_utils
from typing import Dict, List


class Experiment(ABC):
    TIME_KEY = "time"
    PRESSURE_KEY = "pressure"
    OUTPUT_KEY = "output"

    logs: List[Dict[str, str]]
    experiments: Dict[str, Dict]
    summary: Dict[str, Dict]

    def __init__(self, logs):
        self.logs = logs
        self.experiments = self.group_into_experiments(logs)

    def summarise_experiment(self):
        """Given the logs for an experiment, calculates the maximum pressure values for each pump"""

        experiment_summary = {}
        for experiment_number, experiment_logs in self.experiments.items():

            grouped_values = defaultdict(list)
            for log_line in experiment_logs:
                for pump_key, pressure_value in log_line[self.PRESSURE_KEY].items():
                    grouped_values[pump_key].append(float(pressure_value))

            max_values = {key: max(values) for key, values in grouped_values.items()}
            experiment_summary[experiment_number] = max_values

        self.summary = experiment_summary
        return experiment_summary

    def is_time_field(header):
        pattern = r"time"
        return regex_utils.regex_match(pattern, header, ignore_case=True)

    def is_output_field(header):
        pattern = r"output"
        return regex_utils.regex_match(pattern, header, ignore_case=True)

    def group_into_experiments(self, rows):
        row_iterator = iter(rows)
        grouped_results = {}
        try:
            while True:
                experiment_rows = self.extract_experiment_logs(row_iterator)
                print(f"found these logs {len(experiment_rows)}")
                if not experiment_rows or len(experiment_rows) == 0:
                    break

                experiment_number = self.get_experiment_number_from_start_row(
                    experiment_rows[0]
                )
                grouped_results[experiment_number] = experiment_rows

        except StopIteration:
            print("The experimental logs have been exhausted")

        return grouped_results

    @abstractmethod
    def is_pressure_field(self, row):
        """Experiment specific regex to identify pressure field"""
        pass

    @abstractmethod
    def transform_row(self, row):
        """Experiment specific transformation function to extract important values"""
        pass

    @abstractmethod
    def get_experiment_number_from_start_row(self, start_row):
        """Experiment specific regex match function to identify experiment number from first row"""
        pass

    @abstractmethod
    def is_start_of_experiment(self, row):
        """Experiment specific regex match function to identify start of experiment"""
        pass

    @abstractmethod
    def is_end_of_experiment(self, row):
        """Experiment specific regex match function to identify end of experiment"""
        pass

    @abstractmethod
    def extract_experiment_logs(self, row_iterator):
        """Experiment specific function to group log lines into experiments"""
        pass
