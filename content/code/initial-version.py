import pandas as pd
from matplotlib import pyplot as plt

month = 1

# read data from file
df = pd.read_csv("weather_data.csv")
data = df[df['month'] == month].reset_index(drop=True)  # Filter for January only and reindex
temperatures = data["air_temperature"]
precipitation = data["precipitation"]
num_measurements = len(precipitation)

# compute statistics
temp_mean = sum(temperatures) / num_measurements
precip_mean = sum(precipitation) / num_measurements

# plot temperature
plt.figure()
plt.plot(temperatures, "r-")
plt.axhline(y=temp_mean, color="r", linestyle="--")
plt.savefig(f"month-{month}_air_temperature.png")
plt.show()
plt.close()

# plot precipitation
plt.figure()
plt.plot(precipitation, "b-")
plt.axhline(y=precip_mean, color="b", linestyle="--")
plt.savefig(f"month-{month}_precipitation.png")
plt.show()
plt.close()

