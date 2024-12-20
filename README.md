# py-pressure-logs

# Introduction

This project is designed to parse experimental logs, grouping them into experiments, tracking pressure values and visualising experimental progression.

# Supported protocols

This project currently only supports documents of the `sunscreen` and `sunshine` protocols

# Running the application

## Run as an executable

To support ease of use, this project has been bundled into a self-contained executable file with all external dependencies, which can be run on both Mac and Windows.
The executable is eponymously named `py_pressure_logs`

### Examples

Once an executable has been downloaded or recreated, run:

Mac
```
py_pressure_logs sunshine path/to/log/file.csv
```

Windows
```
py_pressure_logs.exe sunshine path/to/log/file.csv
```

Optionally, an name for the output csv can be specified via

```
py_pressure_logs sunshine path/to/log/file.csv -o output_file_name
```

If help is required using the script, run:

```
py_pressure_logs --help
```

## Generating the executeable

The executeable dist can be regenerated by running either `make build-mac` (on Mac) or `poetry run pyinstaller --onefile --distpath dist/windows --name=py_pressure_logs py_pressure_logs/main.py`, depending on the target execution environment.

## Running the project locally

## Prerequisites

To run this project you will need:

- [Git installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Python v3.12.7 installed](https://www.python.org/downloads/)
- [Poetry - the python dependency manager installed](https://python-poetry.org/docs/#installing-with-the-official-installer)
- [Poetry added to your system Path](https://python-poetry.org/docs/#installing-with-the-official-installer:~:text=Add%20Poetry%20to%20your%20PATH,poetry%20if%20%24POETRY_HOME%20is%20set.)

## Project set up

To run this project as a standalone application, you will need to do the following:

- Clone this git repository
- run `poetry install`
- run `poetry run streamlit run py_pressure_logs/app.py`

## Using the application UI

As noted above, the UI can be started by running `poetry run streamlit run py_pressure_logs/app.py` at the root of the project. This should spin up a webserver accessible [here](http://localhost:8501)

### Select an experimental protocol

An experimental protocol must be selected like so:

![select experiment](/assets/select_experiment.png)

This tells the program what experimental and wash trigger entry and exit points to look for.

### Upload the experimental logs

Select browse files and select the `.csv` file containing the experimental logs. This file must be from either the `sunshine` or `sunscreen` protocols.

![browse files](/assets/select_file.png)

### View experimental summaries

Experimental summaries from all experiments and all washes will be visible in a table called `summaries`.
This table will display the maximum system pressures across the experiment, as well as the experiment start (inclusive) and end (exclusive) log lines

![experimental summary](/assets/summarised_results.png)

### Visualise experimental pressures

Experimental pressures can also be visualed through the `See Experimental Graphs` section of the page. Clicking each button will load another window with a visualisation of the pressures across the experiment

![visualise_button](/assets//access_graphs.png)
![experimental_graphs](/assets/experimental_graphs.png)
