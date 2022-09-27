import pandas as pd
from matplotlib import pyplot as plt
import pytest


def plot_data(data, mean, xlabel, ylabel, file_name):
    plt.plot(data, "r-")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.axhline(y=mean, color="b", linestyle="--")
    #   plt.show()
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


def main():
    for num_measurements in [25, 100, 500]:

        temperatures = read_data(
            file_name="temperatures.csv",
            nrows=num_measurements,
            column="Air temperature (degC)",
        )

        mean = compute_mean(temperatures)

        plot_data(
            data=temperatures,
            mean=mean,
            xlabel="measurements",
            ylabel="air temperature (deg C)",
            file_name=f"{num_measurements}.png",
        )


if __name__ == "__main__":
    main()
