import pandas as pd
from matplotlib import pyplot as plt
import pytest
import click


def plot_data(data, mean, xlabel, ylabel, file_name):
    plt.plot(data, "r-")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.axhline(y=mean, color="b", linestyle="--")
    plt.savefig(file_name)
    plt.clf()


def compute_mean(data):
    mean = sum(data) / len(data)
    return mean


def test_compute_mean():
    result = compute_mean([1.0, 2.0, 3.0, 4.0])
    assert result == pytest.approx(2.5)


def read_data(file_name, nrows, column):
    data = pd.read_csv(file_name, nrows=nrows)
    return data[column]


@click.command()
@click.option(
    "--num-measurements", required=True, type=int, help="Number of measurements."
)
@click.option("--in-file", required=True, help="File name where we read from.")
@click.option("--out-file", required=True, help="File name where we write to.")
def main(num_measurements, in_file, out_file):

    temperatures = read_data(
        file_name=in_file,
        nrows=num_measurements,
        column="Air temperature (degC)",
    )

    mean = compute_mean(temperatures)

    plot_data(
        data=temperatures,
        mean=mean,
        xlabel="measurements",
        ylabel="air temperature (deg C)",
        file_name=out_file,
    )


if __name__ == "__main__":
    main()
