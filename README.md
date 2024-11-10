# py-pressure-logs

# Introduction

This project aims to solve business specific logic relating to log outputs from a series of pressure experiments. Experiments emit a linear progression of outputs, which should be grouped into experiments and validated against known bounds.

# Supported protocols

This project currently only supports documents of the `Sunscreen` and `Sunshine` Protocols

# Running locally

## Prerequisites

To run this project you will need Python v3.12.7 installed. If you do not have this already follow these instructions...

Ensure the script is executable by ...

## Executing the programme

To run this script, it requires the csv input data

```
Example invocation
```


Way 1 - running project with poetry
1. download Python 3.12.17 (verify with python --version)
2. Download poetry (insert link) (verify with poetry --version)
3. Add poetry to path (advanced settings guide)
4. Download Git (verify with git --version)
5. In termal clone this repository
6. navigate to project with cd
7. poetry install
8. poetry shell
9. Poetry run python ....

Way 2 - running the executable
Look into pyinstaller

## Outputs

This programme currently outputs the peak max pressure for each pump for each experiment

```
Example output
```
