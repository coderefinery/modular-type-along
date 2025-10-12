from pathlib import Path


import pandas as pd
import matplotlib.pyplot as plt
import pytest
import click


def read_data(file_name):
    data = pd.read_csv(file_name)

    # combine 'date' and 'time' into a single datetime column
    data["datetime"] = pd.to_datetime(data["date"] + " " + data["time"])

    # set datetime as index for convenience
    data = data.set_index("datetime")

    return data


def arithmetic_mean(values):
    mean_value = sum(values) / len(values)
    return mean_value


def test_arithmetic_mean():
    result = arithmetic_mean([1.0, 2.0, 3.0, 4.0])
    assert result == pytest.approx(2.5)


def plot(date_range, values, label, location, color, compute_mean, file_name):
    fig, ax = plt.subplots()

    # time series
    ax.plot(
        date_range,
        values,
        label=label,
        color=color,
    )

    if compute_mean:
        mean_value = arithmetic_mean(values)

        # mean (as horizontal dashed line)
        ax.axhline(
            y=mean_value,
            label=f"mean {label}: {mean_value:.1f}",
            color=color,
            linestyle="--",
        )

    ax.set_title(f"{label} at {location}")
    ax.set_xlabel("date and time")
    ax.set_ylabel(label)
    ax.legend()
    ax.grid(True)

    # format x-axis for better date display
    fig.autofmt_xdate()

    # fig.show()
    fig.savefig(file_name)


@click.command()
@click.option("--month", required=True, type=str, help="Which month (YYYY-MM)?")
@click.option(
    "--data-file",
    required=True,
    type=click.Path(exists=True, path_type=Path),
    help="Data is read from this file.",
)
@click.option(
    "--output-directory",
    required=True,
    type=click.Path(exists=True, path_type=Path),
    help="Figures are written to this directory.",
)
def main(
    month,
    data_file,
    output_directory,
):
    data = read_data(data_file)

    data_month = data.loc[month]
    date_range = data_month.index

    plot(
        date_range,
        data_month["air_temperature_celsius"].values,
        "air temperature (C)",
        "Helsinki airport",
        "red",
        compute_mean=True,
        file_name=output_directory / f"{month}-temperature.png",
    )
    plot(
        date_range,
        data_month["precipitation_mm"].values,
        "precipitation (mm)",
        "Helsinki airport",
        "blue",
        compute_mean=False,
        file_name=output_directory / f"{month}-precipitation.png",
    )


if __name__ == "__main__":
    main()
