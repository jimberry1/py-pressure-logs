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
            "time": "04/03/2024 17:00",
            "output": "00:05:51 : Sunshine Development Prime: Successfully completed | 00:05:51 : Sunshine Development Prime: Protocol Stopping | 00:05:51 : Sunshine Development Prime: Automated collector: Stop | 00:05:51 : Sunshine Development Prime: Protocol All devices now stopped | 00:05:51 : Sunshine Development Prime: Automated collector: Setting valve to Drain | 00:00:00 : Please wait while we import parameters..... | 00:00:00 : Excel import | 00:00:00 : Importing Schema and system configuration | 00:00:00 : Importing Fluidic configuration | 00:00:00 : Importing Input 1 pump parameters | 00:00:00 : Importing Input 2 pump parameters | 00:00:00 : Importing Dilution pump parameters | 00:00:00 : Importing Collector parameters | 00:00:00 : Importing Experiment parameters | 00:00:00 : Importing experiment table | 00:00:00 : Validating experiments | 00:00:00 : Updating description to Installation IQOQ Protocol 2 Sunshine Protocol, Sunny 490 Trident T,  Fluidic Configuration A, 7 Experiment(s) defined, Wash Level High | 00:00:00 : Updating protocol parameters | 00:00:00 : Excel Import: Completed | 00:00:00 : Imported. | 00:00:00 : Please wait while we import parameters..... | 00:00:00 : Excel import | 00:00:00 : Importing Schema and system configuration | 00:00:00 : Importing Fluidic configuration | 00:00:00 : Importing Input 1 pump parameters | 00:00:00 : Importing Input 2 pump parameters | 00:00:00 : Importing Dilution pump parameters | 00:00:00 : Importing Collector parameters | 00:00:00 : Importing Experiment parameters | 00:00:00 : Importing experiment table | 00:00:00 : Validating experiments | 00:00:00 : Updating description to Operational Qualification Protocol 1 Sunshine Protocol, Sunny 490 Trident T,  Fluidic Configuration A, 12 Experiment(s) defined, Wash Level High | 00:00:00 : Updating protocol parameters | 00:00:00 : Excel Import: Completed | 00:00:00 : Imported. | 00:00:00 : Sunshine protocol: Starting... | 00:00:00 : Sunshine protocol: Automated collector: Stop | 00:00:00 : Sunshine protocol: Protocol All pumps fitted with Red Syringes | 00:00:00 : Sunshine protocol: Protocol Collector rack description selected: 2 ml Rack, 35 Vials, 5x7 matches imported rack description",
            "pressure": {
                "Quad Pump 1 | current pressure | (bar)": "0",
                "Quad Pump 3 | current pressure | (bar)": "-0.1",
                "Quad Pump 2 | current pressure | (bar)": "0",
            },
            "row_number": 2,
        }
    ],
)
def test_first_log_line(sunshine_experiment, expected):
    assert sunshine_experiment.logs[0] == expected


def test_correct_number_of_keys(sunshine_experiment):
    assert len(sunshine_experiment.experiments.keys()) == 12


@pytest.mark.parametrize(
    "expected",
    [
        {
            "time": "04/03/2024 17:01",
            "output": "00:01:44 : Sunshine protocol: B Running experiments | 00:01:44 : Sunshine protocol: ExperimentNInput1FluidRequired | 00:01:44 : Sunshine protocol: ExperimentNDilutionFluidRequired | 00:01:44 : Sunshine protocol: Experiment 001: parameters valid | 00:01:44 : Experiment 001: OQ1 - Pressure Check: Experiment Preparation Begun | 00:01:44 : Experiment 001: OQ1 - Pressure Check: Protocol  B-1 Experiment Preparation:  | 00:01:44 : Experiment 001: OQ1 - Pressure Check: Protocol  B-1.1 Experiment Preparation: Collector set valve to DRAIN | 00:01:44 : Experiment 001: OQ1 - Pressure Check: Automated collector: Setting valve to Drain | 00:01:44 : Experiment 001: OQ1 - Pressure Check: Protocol  B-1.2 Experiment Preparation: Collector set vial to WASH position | 00:01:44 : Experiment 001: OQ1 - Pressure Check: Automated collector: Positioning at Wash position",
            "pressure": {
                "Quad Pump 1 | current pressure | (bar)": "0",
                "Quad Pump 3 | current pressure | (bar)": "-0.1",
                "Quad Pump 2 | current pressure | (bar)": "0",
            },
            "row_number": 99,
        }
    ],
)
def test_correct_first_experiment_line(sunshine_experiment, expected):
    assert sunshine_experiment.experiments["001"][0] == expected


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
def test_summarise_experiments(sunshine_experiment, expected):
    assert sunshine_experiment.summarise_experiments() == expected


@pytest.mark.parametrize(
    "expected",
    [
        {
            "001": {
                "Quad Pump 1 | current pressure | (bar)": 0.7,
                "Quad Pump 3 | current pressure | (bar)": 0.1,
                "Quad Pump 2 | current pressure | (bar)": 0.8,
            },
            "002": {
                "Quad Pump 1 | current pressure | (bar)": 0.7,
                "Quad Pump 3 | current pressure | (bar)": 0.1,
                "Quad Pump 2 | current pressure | (bar)": 0.8,
            },
            "003": {
                "Quad Pump 1 | current pressure | (bar)": 0.8,
                "Quad Pump 3 | current pressure | (bar)": 0.1,
                "Quad Pump 2 | current pressure | (bar)": 0.8,
            },
            "004": {
                "Quad Pump 1 | current pressure | (bar)": 0.8,
                "Quad Pump 3 | current pressure | (bar)": 0.1,
                "Quad Pump 2 | current pressure | (bar)": 0.8,
            },
            "005": {
                "Quad Pump 1 | current pressure | (bar)": 0.8,
                "Quad Pump 3 | current pressure | (bar)": 0.1,
                "Quad Pump 2 | current pressure | (bar)": 0.8,
            },
            "006": {
                "Quad Pump 1 | current pressure | (bar)": 0.8,
                "Quad Pump 3 | current pressure | (bar)": 0.1,
                "Quad Pump 2 | current pressure | (bar)": 0.8,
            },
            "007": {
                "Quad Pump 1 | current pressure | (bar)": 0.8,
                "Quad Pump 3 | current pressure | (bar)": 0.1,
                "Quad Pump 2 | current pressure | (bar)": 0.8,
            },
            "008": {
                "Quad Pump 1 | current pressure | (bar)": 0.8,
                "Quad Pump 3 | current pressure | (bar)": 0.1,
                "Quad Pump 2 | current pressure | (bar)": 0.8,
            },
            "009": {
                "Quad Pump 1 | current pressure | (bar)": 0.8,
                "Quad Pump 3 | current pressure | (bar)": 0.1,
                "Quad Pump 2 | current pressure | (bar)": 0.8,
            },
            "010": {
                "Quad Pump 1 | current pressure | (bar)": 0.8,
                "Quad Pump 3 | current pressure | (bar)": 0.1,
                "Quad Pump 2 | current pressure | (bar)": 0.8,
            },
            "011": {
                "Quad Pump 1 | current pressure | (bar)": 0.8,
                "Quad Pump 3 | current pressure | (bar)": 0.1,
                "Quad Pump 2 | current pressure | (bar)": 0.8,
            },
            "012": {
                "Quad Pump 1 | current pressure | (bar)": 1.0,
                "Quad Pump 3 | current pressure | (bar)": 0.1,
                "Quad Pump 2 | current pressure | (bar)": 1.1,
            },
        }
    ],
)
def test_summarise_washes(sunshine_experiment, expected):
    assert sunshine_experiment.summarise_washes() == expected
