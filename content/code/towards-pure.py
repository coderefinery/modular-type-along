import pandas as pd
from matplotlib import pyplot as plt


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


def read_data(file_name, column, month):
    data = pd.read_csv(file_name)
    data = data[data['month'] == month].reset_index(drop=True)  # Filter for month and reindex
    return data[column]


for month in [1, 2, 3]:
    for column in ["air_temperature", "precipitation"]:
        values = read_data(
            file_name="weather_data.csv", column=column, month=month
        )
        mean_value = compute_mean(values)
        plot_data(values, mean_value, month, column)
