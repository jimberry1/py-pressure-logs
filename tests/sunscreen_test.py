import pytest
from py_pressure_logs.sunscreen_experiment import SunscreenExperiment


@pytest.fixture
def sunscreen_experiment():
    test_data_location = "test_resources/sunscreen_test_data.csv"
    return SunscreenExperiment(test_data_location)


@pytest.mark.parametrize(
    "expected",
    [
        {
            "01": {
                "Fluid Handler 1 | system current pressure | (bar)": 0.2,
                "Fluid Handler 2 | system current pressure | (bar)": 0.3,
                "Fluid Handler 3 | system current pressure | (bar)": 0.1,
            },
            "02": {
                "Fluid Handler 1 | system current pressure | (bar)": 0.2,
                "Fluid Handler 2 | system current pressure | (bar)": 0.2,
                "Fluid Handler 3 | system current pressure | (bar)": 0.1,
            },
            "03": {
                "Fluid Handler 1 | system current pressure | (bar)": 0.3,
                "Fluid Handler 2 | system current pressure | (bar)": 0.3,
                "Fluid Handler 3 | system current pressure | (bar)": 0.2,
            },
            "04": {
                "Fluid Handler 1 | system current pressure | (bar)": 0.3,
                "Fluid Handler 2 | system current pressure | (bar)": 0.4,
                "Fluid Handler 3 | system current pressure | (bar)": 0.2,
            },
            "05": {
                "Fluid Handler 1 | system current pressure | (bar)": 0.4,
                "Fluid Handler 2 | system current pressure | (bar)": 0.5,
                "Fluid Handler 3 | system current pressure | (bar)": 0.2,
            },
            "06": {
                "Fluid Handler 1 | system current pressure | (bar)": 0.4,
                "Fluid Handler 2 | system current pressure | (bar)": 0.5,
                "Fluid Handler 3 | system current pressure | (bar)": 0.2,
            },
            "07": {
                "Fluid Handler 1 | system current pressure | (bar)": 0.8,
                "Fluid Handler 2 | system current pressure | (bar)": 0.7,
                "Fluid Handler 3 | system current pressure | (bar)": 0.5,
            },
            "08": {
                "Fluid Handler 1 | system current pressure | (bar)": 0.8,
                "Fluid Handler 2 | system current pressure | (bar)": 0.7,
                "Fluid Handler 3 | system current pressure | (bar)": 0.5,
            },
            "09": {
                "Fluid Handler 1 | system current pressure | (bar)": 2.1,
                "Fluid Handler 2 | system current pressure | (bar)": 1.9,
                "Fluid Handler 3 | system current pressure | (bar)": 1.3,
            },
            "10": {
                "Fluid Handler 1 | system current pressure | (bar)": 2.1,
                "Fluid Handler 2 | system current pressure | (bar)": 2.1,
                "Fluid Handler 3 | system current pressure | (bar)": 1.3,
            },
            "11": {
                "Fluid Handler 1 | system current pressure | (bar)": 5.4,
                "Fluid Handler 2 | system current pressure | (bar)": 5.4,
                "Fluid Handler 3 | system current pressure | (bar)": 3.7,
            },
            "12": {
                "Fluid Handler 1 | system current pressure | (bar)": 5.4,
                "Fluid Handler 2 | system current pressure | (bar)": 5.3,
                "Fluid Handler 3 | system current pressure | (bar)": 3.6,
            },
            "13": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.1,
                "Fluid Handler 2 | system current pressure | (bar)": 0.9,
                "Fluid Handler 3 | system current pressure | (bar)": 0.6,
            },
            "14": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.1,
                "Fluid Handler 2 | system current pressure | (bar)": 1.0,
                "Fluid Handler 3 | system current pressure | (bar)": 0.6,
            },
            "15": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.1,
                "Fluid Handler 2 | system current pressure | (bar)": 1.0,
                "Fluid Handler 3 | system current pressure | (bar)": 0.6,
            },
            "16": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.1,
                "Fluid Handler 2 | system current pressure | (bar)": 1.0,
                "Fluid Handler 3 | system current pressure | (bar)": 0.6,
            },
            "17": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.1,
                "Fluid Handler 2 | system current pressure | (bar)": 1.0,
                "Fluid Handler 3 | system current pressure | (bar)": 0.6,
            },
            "18": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.1,
                "Fluid Handler 2 | system current pressure | (bar)": 1.1,
                "Fluid Handler 3 | system current pressure | (bar)": 0.7,
            },
            "19": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.1,
                "Fluid Handler 2 | system current pressure | (bar)": 1.0,
                "Fluid Handler 3 | system current pressure | (bar)": 0.7,
            },
            "20": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.0,
                "Fluid Handler 2 | system current pressure | (bar)": 0.9,
                "Fluid Handler 3 | system current pressure | (bar)": 0.6,
            },
            "21": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.1,
                "Fluid Handler 2 | system current pressure | (bar)": 1.0,
                "Fluid Handler 3 | system current pressure | (bar)": 0.6,
            },
            "22": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.1,
                "Fluid Handler 2 | system current pressure | (bar)": 1.1,
                "Fluid Handler 3 | system current pressure | (bar)": 0.6,
            },
            "23": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.0,
                "Fluid Handler 2 | system current pressure | (bar)": 0.9,
                "Fluid Handler 3 | system current pressure | (bar)": 0.6,
            },
            "24": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.0,
                "Fluid Handler 2 | system current pressure | (bar)": 1.0,
                "Fluid Handler 3 | system current pressure | (bar)": 0.6,
            },
        }
    ],
)
def test_happy_path(sunscreen_experiment, expected):
    assert sunscreen_experiment.summarise_experiment() == expected
