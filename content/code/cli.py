import pandas as pd
from matplotlib import pyplot as plt
import pytest
import click

def plot_data(values, mean_value, month, column):
    plt.figure()
    plt.xlabel("Measurement index")
    plt.ylabel(column)
    plt.plot(values, "r-", label=column)
    plt.axhline(y=mean_value, color="b", linestyle="--", label=f"Mean {column}")
    plt.title(f"Month {month} {column}")
    plt.legend()
    plt.savefig(f"month-{month}_{column}.png")
    plt.show()
    plt.close()


def compute_mean(data):
    mean = sum(data) / len(data)
    return mean

def test_compute_mean():
    result = compute_mean([1.0, 2.0, 3.0, 4.0])
    assert result == pytest.approx(2.5)

def read_data(file_name, column, month):
    data = pd.read_csv(file_name)
    data = data[data['month'] == month].reset_index(drop=True)  # Filter for month and reindex
    return data[column]

@click.command()
@click.option(
    "--month", required=True, type=int, help="Month."
)
@click.option("--column", required=True, help="Column name.")
@click.option("--in-file", required=True, help="File name where we read from.")
def main(month, in_file, column):
    values = read_data(
        file_name=in_file,
        month=month,
        column=column,
    )

    mean = compute_mean(values)

    plot_data(
        values=values,
        mean_value=mean,
        month=month,
        column=column,
    )


if __name__ == "__main__":
    main()
