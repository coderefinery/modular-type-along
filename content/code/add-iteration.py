import pandas as pd
from matplotlib import pyplot as plt

# read data from file
df = pd.read_csv("weather_data.csv")

for month in [1, 2, 3]:
    for column in ["air_temperature", "precipitation"]:
        data = df[df['month'] == month].reset_index(drop=True)  # Filter for month only and reindex
        values = data[column]
        num_measurements = len(values)

        # compute statistics
        mean_value = sum(values) / num_measurements

        # plot data
        plt.figure()
        plt.xlabel("Measurement index")
        plt.ylabel(column)
        plt.plot(values, color="r", linestyle="-", label=column)
        plt.axhline(y=mean_value, color="r", 
                    linestyle="--", label=f"Mean {column}")
        plt.title(f"Month {month} {column}")
        plt.legend()
        plt.savefig(f"month-{month}_{column}.png")
        plt.show()
        plt.close()
