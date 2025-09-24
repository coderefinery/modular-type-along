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
plt.xlabel("Measurement index")
plt.ylabel("Temperature (°C)")
plt.plot(temperatures, "r-", label="Air temperature")
plt.axhline(y=temp_mean, color="r", linestyle="--", label="Mean temperature")
plt.title(f"Month {month} Air Temperature")
plt.legend()
plt.savefig(f"month-{month}_air_temperature.png")
plt.show()
plt.close()

# plot precipitation
plt.figure()
plt.xlabel("Measurement index")
plt.ylabel("Precipitation (mm)")
plt.plot(precipitation, "b-", label="Precipitation")
plt.axhline(y=precip_mean, color="b", linestyle="--", label="Mean precipitation")
plt.title(f"Month {month} Precipitation")
plt.legend()
plt.savefig(f"month-{month}_precipitation.png")
plt.show()
plt.close()
