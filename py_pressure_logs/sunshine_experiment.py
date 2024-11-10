import re
import py_pressure_logs.regex_utils as regex_utils
from py_pressure_logs.experiment import Experiment


class SunshineExperiment(Experiment):

    def is_pressure_field(self, header):
        pattern = r".*(\d+).*current pressure.*"
        return regex_utils.regex_match(pattern, header, ignore_case=True)

    def select_experiment_keys(self, row):
        """Selects keys from raw csv data into a just the key-value map relevant for the experiment.
        Common keys such as time and output are handled internally."""
        formatted_row = {self.PRESSURE_KEY: {}}
        for key, val in row.items():
            if self.is_pressure_field(key):
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

    def is_start_of_wash(self, row):
        row_output = row[self.OUTPUT_KEY]
        pattern = (
            r"Cleaning: Washing started|Pressure Check: B All experiments completed"
        )
        return regex_utils.regex_match(pattern, row_output, ignore_case=True)

    def is_end_of_wash(self, row):
        row_output = row[self.OUTPUT_KEY]
        pattern = (
            r"Protocol\s*b-4 system cleaning: completed|Sample Loop Cleaning: Completed"
        )
        return regex_utils.regex_match(pattern, row_output, ignore_case=True)

    def get_wash_experiment_number(self, logs_for_wash):
        first_row_output = logs_for_wash[0][self.OUTPUT_KEY]
        pattern = r"Experiment (\d+):"
        match = re.search(pattern, first_row_output, re.IGNORECASE)

        if match:
            return match.group(1)
        else:
            raise Exception(
                f"no experiment number found for wash row {first_row_output}"
            )
