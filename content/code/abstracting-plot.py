import pandas as pd
from matplotlib import pyplot as plt

plt.xlabel("measurements")
plt.ylabel("air temperature (deg C)")


def plot_temperatures(temperatures):
    plt.plot(temperatures, "r-")
    plt.axhline(y=mean, color="b", linestyle="--")
    plt.show()
    plt.savefig(f"{num_measurements}.png")
    plt.clf()


for num_measurements in [25, 100, 500]:

    # read data from file
    data = pd.read_csv("temperatures.csv", nrows=num_measurements)
    temperatures = data["Air temperature (degC)"]

    # compute statistics
    mean = sum(temperatures) / num_measurements

    # plot results
    #   plt.plot(temperatures, 'r-')
    #   plt.axhline(y=mean, color='b', linestyle='--')
    #   plt.show()
    #   plt.savefig(f'{num_measurements}.png')
    #   plt.clf()
    plot_temperatures(temperatures)
