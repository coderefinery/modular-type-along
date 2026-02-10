import pandas as pd
import matplotlib.pyplot as plt


# read data
data = pd.read_csv("weather_data.csv")

# combine 'date' and 'time' into a single column 'recorded_at' as type datetime
data["recorded_at"] = pd.to_datetime(data["date"] + " " + data["time"])

# set 'recorded_at' as index for convenience
data = data.set_index("recorded_at")

# keep only january data using datetime period indexing
january = data.loc["2024-01"]

fig, ax = plt.subplots()

# temperature time series
ax.plot(
    january.index,
    january["air_temperature_celsius"],
    label="air temperature (C)",
    color="red",
)

values = january["air_temperature_celsius"].values
mean_temp = sum(values) / len(values)

# mean temperature (as horizontal dashed line)
ax.axhline(
    y=mean_temp,
    label=f"mean air temperature (C): {mean_temp:.1f}",
    color="red",
    linestyle="--",
)

ax.set_title("air temperature (C) at Helsinki airport")
ax.set_xlabel("date and time")
ax.set_ylabel("air temperature (C)")
ax.legend()
ax.grid(True)

# format x-axis for better date display
fig.autofmt_xdate()

fig.savefig("2024-01-temperature.png")
