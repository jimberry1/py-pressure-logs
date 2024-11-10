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
            "time": "07/03/2024 23:01",
            "output": "00:00:34 : Initialization protocol: Successfully completed | 00:00:34 : Initialization protocol: Input 1 Stack: Sample Pump: State set to Idle | 00:00:34 : Initialization protocol: Input 1 Stack: System Pump: State set to Idle | 00:00:34 : Initialization protocol: Input 2 Stack: Sample Pump: State set to Idle | 00:00:34 : Initialization protocol: Input 2 Stack: System Pump: State set to Idle | 00:00:34 : Initialization protocol: Collection Stack: Sample Pump: State set to Idle | 00:00:34 : Initialization protocol: Collection Stack: System Pump: State set to Idle | 00:00:34 : Sunscreen Experimental Protocol: Starting... | 00:00:34 : Sunscreen Experimental Protocol: Input 1 well plate definition assigned IST Scientific 2.2 ml Round Bottom (7206088) | 00:00:34 : Sunscreen Experimental Protocol: Input 2 well plate definition assigned IST Scientific 2.2 ml Round Bottom (7206088) | 00:00:34 : Sunscreen Experimental Protocol: Collection well plate definition assigned IST Scientific 2.2 ml Round Bottom (7206088)",
            "pressure": {
                "Fluid Handler 1 | system current pressure | (bar)": "-0.1",
                "Fluid Handler 2 | system current pressure | (bar)": "0",
                "Fluid Handler 3 | system current pressure | (bar)": "-0.1",
            },
            "row_number": 2,
        }
    ],
)
def test_first_log_line(sunscreen_experiment, expected):
    assert sunscreen_experiment.logs[0] == expected


def test_correct_number_of_keys(sunscreen_experiment):
    assert len(sunscreen_experiment.experiments.keys()) == 24


@pytest.mark.parametrize(
    "expected",
    [
        {
            "time": "07/03/2024 23:03",
            "output": "00:02:16 : Exp01: C: Collection Stack - Collection preparation completed | 00:02:16 : Exp01: preparation completed | 00:02:16 : Exp01: run | 00:02:16 : Exp01: D-1: Input 1 Stack - Starting Sample pre-pressurisation | 00:02:16 : Exp01: D-2: Input 2 Stack - Starting Sample pre-pressurisation",
            "pressure": {
                "Fluid Handler 1 | system current pressure | (bar)": "-0.1",
                "Fluid Handler 2 | system current pressure | (bar)": "0",
                "Fluid Handler 3 | system current pressure | (bar)": "-0.1",
            },
            "row_number": 103,
        }
    ],
)
def test_correct_first_experiment_line(sunscreen_experiment, expected):
    assert sunscreen_experiment.experiments["01"][0] == expected


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
def test_experiments_summary(sunscreen_experiment, expected):
    assert sunscreen_experiment.summarise_experiments() == expected


@pytest.mark.parametrize(
    "expected",
    [
        {
            "01": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.0,
                "Fluid Handler 2 | system current pressure | (bar)": 1.1,
                "Fluid Handler 3 | system current pressure | (bar)": 0.2,
            },
            "02": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.0,
                "Fluid Handler 2 | system current pressure | (bar)": 1.0,
                "Fluid Handler 3 | system current pressure | (bar)": 0.3,
            },
            "03": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.0,
                "Fluid Handler 2 | system current pressure | (bar)": 1.1,
                "Fluid Handler 3 | system current pressure | (bar)": 0.3,
            },
            "04": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.1,
                "Fluid Handler 2 | system current pressure | (bar)": 1.1,
                "Fluid Handler 3 | system current pressure | (bar)": 0.3,
            },
            "05": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.0,
                "Fluid Handler 2 | system current pressure | (bar)": 1.1,
                "Fluid Handler 3 | system current pressure | (bar)": 0.3,
            },
            "06": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.1,
                "Fluid Handler 2 | system current pressure | (bar)": 1.0,
                "Fluid Handler 3 | system current pressure | (bar)": 0.3,
            },
            "07": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.0,
                "Fluid Handler 2 | system current pressure | (bar)": 1.0,
                "Fluid Handler 3 | system current pressure | (bar)": 0.4,
            },
            "08": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.0,
                "Fluid Handler 2 | system current pressure | (bar)": 1.0,
                "Fluid Handler 3 | system current pressure | (bar)": 0.4,
            },
            "09": {
                "Fluid Handler 1 | system current pressure | (bar)": 0.9,
                "Fluid Handler 2 | system current pressure | (bar)": 0.8,
                "Fluid Handler 3 | system current pressure | (bar)": 0.2,
            },
            "10": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.0,
                "Fluid Handler 2 | system current pressure | (bar)": 0.9,
                "Fluid Handler 3 | system current pressure | (bar)": 0.4,
            },
            "11": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.0,
                "Fluid Handler 2 | system current pressure | (bar)": 1.1,
                "Fluid Handler 3 | system current pressure | (bar)": 0.4,
            },
            "12": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.1,
                "Fluid Handler 2 | system current pressure | (bar)": 1.1,
                "Fluid Handler 3 | system current pressure | (bar)": 0.4,
            },
            "13": {
                "Fluid Handler 1 | system current pressure | (bar)": 0.9,
                "Fluid Handler 2 | system current pressure | (bar)": 0.9,
                "Fluid Handler 3 | system current pressure | (bar)": 0.4,
            },
            "14": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.0,
                "Fluid Handler 2 | system current pressure | (bar)": 0.9,
                "Fluid Handler 3 | system current pressure | (bar)": 0.4,
            },
            "15": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.0,
                "Fluid Handler 2 | system current pressure | (bar)": 0.9,
                "Fluid Handler 3 | system current pressure | (bar)": 0.4,
            },
            "16": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.0,
                "Fluid Handler 2 | system current pressure | (bar)": 0.9,
                "Fluid Handler 3 | system current pressure | (bar)": 0.4,
            },
            "17": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.0,
                "Fluid Handler 2 | system current pressure | (bar)": 1.0,
                "Fluid Handler 3 | system current pressure | (bar)": 0.4,
            },
            "18": {
                "Fluid Handler 1 | system current pressure | (bar)": 0.9,
                "Fluid Handler 2 | system current pressure | (bar)": 1.0,
                "Fluid Handler 3 | system current pressure | (bar)": 0.4,
            },
            "19": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.0,
                "Fluid Handler 2 | system current pressure | (bar)": 1.0,
                "Fluid Handler 3 | system current pressure | (bar)": 0.4,
            },
            "20": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.0,
                "Fluid Handler 2 | system current pressure | (bar)": 1.1,
                "Fluid Handler 3 | system current pressure | (bar)": 0.4,
            },
            "21": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.0,
                "Fluid Handler 2 | system current pressure | (bar)": 0.9,
                "Fluid Handler 3 | system current pressure | (bar)": 0.4,
            },
            "22": {
                "Fluid Handler 1 | system current pressure | (bar)": 0.9,
                "Fluid Handler 2 | system current pressure | (bar)": 1.0,
                "Fluid Handler 3 | system current pressure | (bar)": 0.4,
            },
            "23": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.0,
                "Fluid Handler 2 | system current pressure | (bar)": 0.8,
                "Fluid Handler 3 | system current pressure | (bar)": 0.4,
            },
            "24": {
                "Fluid Handler 1 | system current pressure | (bar)": 1.0,
                "Fluid Handler 2 | system current pressure | (bar)": 0.9,
                "Fluid Handler 3 | system current pressure | (bar)": 0.4,
            },
        }
    ],
)
def test_wash_summary(sunscreen_experiment, expected):
    assert sunscreen_experiment.summarise_washes() == expected
