import pytest
from py_pressure_logs.sunshine_experiment import SunshineExperiment


@pytest.fixture
def sunshine_experiment():
    test_data_location = "test_resources/sunshine_test_data.csv"
    return SunshineExperiment(test_data_location)


@pytest.mark.parametrize(
    "expected",
    [
        {
            "001": {
                "Quad Pump 1 | current pressure | (bar)": 0.0,
                "Quad Pump 3 | current pressure | (bar)": -0.1,
                "Quad Pump 2 | current pressure | (bar)": 0.0,
            },
            "002": {
                "Quad Pump 1 | current pressure | (bar)": 0.0,
                "Quad Pump 3 | current pressure | (bar)": -0.1,
                "Quad Pump 2 | current pressure | (bar)": 0.0,
            },
            "003": {
                "Quad Pump 1 | current pressure | (bar)": 0.0,
                "Quad Pump 3 | current pressure | (bar)": -0.1,
                "Quad Pump 2 | current pressure | (bar)": 0.1,
            },
            "004": {
                "Quad Pump 1 | current pressure | (bar)": 0.0,
                "Quad Pump 3 | current pressure | (bar)": -0.1,
                "Quad Pump 2 | current pressure | (bar)": 0.1,
            },
            "005": {
                "Quad Pump 1 | current pressure | (bar)": 0.2,
                "Quad Pump 3 | current pressure | (bar)": 0.0,
                "Quad Pump 2 | current pressure | (bar)": 0.2,
            },
            "006": {
                "Quad Pump 1 | current pressure | (bar)": 0.2,
                "Quad Pump 3 | current pressure | (bar)": 0.0,
                "Quad Pump 2 | current pressure | (bar)": 0.2,
            },
            "007": {
                "Quad Pump 1 | current pressure | (bar)": 0.5,
                "Quad Pump 3 | current pressure | (bar)": 0.0,
                "Quad Pump 2 | current pressure | (bar)": 0.5,
            },
            "008": {
                "Quad Pump 1 | current pressure | (bar)": 0.5,
                "Quad Pump 3 | current pressure | (bar)": 0.0,
                "Quad Pump 2 | current pressure | (bar)": 0.5,
            },
            "009": {
                "Quad Pump 1 | current pressure | (bar)": 1.2,
                "Quad Pump 3 | current pressure | (bar)": 0.3,
                "Quad Pump 2 | current pressure | (bar)": 1.2,
            },
            "010": {
                "Quad Pump 1 | current pressure | (bar)": 1.2,
                "Quad Pump 3 | current pressure | (bar)": 0.3,
                "Quad Pump 2 | current pressure | (bar)": 1.2,
            },
            "011": {
                "Quad Pump 1 | current pressure | (bar)": 2.9,
                "Quad Pump 3 | current pressure | (bar)": 0.9,
                "Quad Pump 2 | current pressure | (bar)": 2.8,
            },
            "012": {
                "Quad Pump 1 | current pressure | (bar)": 2.9,
                "Quad Pump 3 | current pressure | (bar)": 1.0,
                "Quad Pump 2 | current pressure | (bar)": 2.9,
            },
        },
    ],
)
def test_happy_path(sunshine_experiment, expected):
    assert sunshine_experiment.summarise_experiment() == expected
