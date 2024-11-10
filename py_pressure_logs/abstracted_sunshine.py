from itertools import takewhile, dropwhile
import re
import py_pressure_logs.regex_utils as regex_utils
from py_pressure_logs.experiment import Experiment


class SunshineExperiment(Experiment):

    def is_pressure_field(self, header):
        pattern = r".*(\d+).*current pressure.*"
        return regex_utils.regex_match(pattern, header, ignore_case=True)

    def transform_row(self, row):
        """Transforms a row from all csv data to a collection of log lines"""
        formatted_row = {self.PRESSURE_KEY: {}}
        for key, val in row.items():
            if self.is_time_field(key):
                formatted_row[self.TIME_KEY] = val
                continue
            elif self.is_output_field(key):
                formatted_row[self.OUTPUT_KEY] = val
                continue
            elif self.is_pressure_field(key):
                formatted_row[self.PRESSURE_KEY][key] = val
                continue

        return formatted_row

    def get_experiment_number_from_start_row(self, row):
        row_output = row[self.OUTPUT_KEY]
        pattern = r".*Experiment (\d+):.*Experiment Preparation Begun"
        match = re.search(pattern, row_output, re.IGNORECASE)

        if match:
            return match.group(1)
        else:
            raise Exception(f"no experiment number found for row {row}")

    def is_start_of_experiment(self, row):
        row_output = row[self.OUTPUT_KEY]
        pattern = r".*Experiment \d+:.*Experiment Preparation Begun"
        return regex_utils.regex_match(pattern, row_output, ignore_case=True)

    def is_end_of_experiment(self, row):
        row_output = row[self.OUTPUT_KEY]
        pattern = r"Experiment run completed"
        return regex_utils.regex_match(pattern, row_output, ignore_case=True)

    def extract_experiment_logs(self, rows):
        """Returns all rows for an experiment, dropping all rows up to the start of the experiment"""
        logs_from_experiment_start = dropwhile(
            lambda row: not self.is_start_of_experiment(row), rows
        )

        experiment_rows = takewhile(
            lambda row: not self.is_end_of_experiment(row), logs_from_experiment_start
        )

        return list(experiment_rows)
