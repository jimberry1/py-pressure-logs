import py_pressure_logs.sunshine_experiment as exp


if __name__ == "__main__":
    file_path = "resources/sunshine/2024-03-04_17h00m11s_full.csv"

    experiment_protocol = exp.SunshineExperiment(file_path)

    summary = experiment_protocol.summarise_experiments()

    experiment_protocol.output_csv()
