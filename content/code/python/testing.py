import pandas as pd
import matplotlib.pyplot as plt
import pytest


def read_data(file_name):
    data = pd.read_csv(file_name)

    # combine 'date' and 'time' into a single column 'recorded_at' as type datetime
    data["recorded_at"] = pd.to_datetime(data["date"] + " " + data["time"])

    # set 'recorded_at' as index for convenience
    data = data.set_index("recorded_at")

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

    fig.savefig(file_name)


def main():
    data = read_data("weather_data.csv")

    for month in ["2024-01", "2024-02", "2024-03"]:
        data_month = data.loc[month]
        date_range = data_month.index

        plot(
            date_range,
            data_month["air_temperature_celsius"].values,
            "air temperature (C)",
            "Helsinki airport",
            "red",
            compute_mean=True,
            file_name=f"{month}-temperature.png",
        )
        plot(
            date_range,
            data_month["precipitation_mm"].values,
            "precipitation (mm)",
            "Helsinki airport",
            "blue",
            compute_mean=False,
            file_name=f"{month}-precipitation.png",
        )


if __name__ == "__main__":
    main()
