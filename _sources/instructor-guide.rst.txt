Instructor guide (spoiler alert!)
=================================


Before we start
---------------

We don't have to follow this line by line but it's important to study
this example well before demonstrating this.

Emphasize that the example is Python but we will try to see "through"
the code and focus on the bigger picture and hopefully manage to imagine
other languages in its place.

We collect ideas and feedback on HackMD while coding and the instructor
tries to react to that without going into the rabbit hole.


Our initial version
-------------------

We imagine that we assemble a working script from various StackOverflow
recommendations and arrive at:

.. code-block:: python

   import pandas as pd
   from matplotlib import pyplot as plt

   num_measurements = 25

   # read data from file
   data = pd.read_csv('temperatures.csv', nrows=num_measurements)
   temperatures = data['Air temperature (degC)']

   # compute statistics
   mean = sum(temperatures)/num_measurements

   # plot results
   plt.plot(temperatures, 'r-')
   plt.axhline(y=mean, color='b', linestyle='--')
   plt.savefig('25.png')
   plt.clf()


- We test it.
- Add ``requirements.txt``.


We add axis labels
------------------

It's not the best placement but it works and later it will bite us (only the
first plot will have labels) and we will improve it:

.. code-block:: python
   :emphasize-lines: 4,5

   import pandas as pd
   from matplotlib import pyplot as plt

   plt.xlabel('measurements')
   plt.ylabel('air temperature (deg C)')

   num_measurements = 25

   # read data from file
   data = pd.read_csv('temperatures.csv', nrows=num_measurements)
   temperatures = data['Air temperature (degC)']

   # compute statistics
   mean = sum(temperatures)/num_measurements

   # plot results
   plt.plot(temperatures, 'r-')
   plt.axhline(y=mean, color='b', linestyle='--')
   plt.savefig('25.png')
   plt.clf()

Once we get this working for 25 measurements, our task changes to also
plot the first 100 and the first 500 measurements in two additional
plots.


Plotting also 100 and 500 measurements
--------------------------------------

- Next idea is code duplication.
- Then a loop:

.. code-block:: python
   :emphasize-lines: 7

   import pandas as pd
   from matplotlib import pyplot as plt

   plt.xlabel('measurements')
   plt.ylabel('air temperature (deg C)')

   for num_measurements in [25, 100, 500]:

       # read data from file
       data = pd.read_csv('temperatures.csv', nrows=num_measurements)
       temperatures = data['Air temperature (degC)']

       # compute statistics
       mean = sum(temperatures)/num_measurements

       # plot results
       plt.plot(temperatures, 'r-')
       plt.axhline(y=mean, color='b', linestyle='--')
       plt.savefig(f'{num_measurements}.png')
       plt.clf()


Abstracting the plotting part into a function
---------------------------------------------

.. code-block:: python
   :emphasize-lines: 8-12,25-28

   import pandas as pd
   from matplotlib import pyplot as plt

   plt.xlabel('measurements')
   plt.ylabel('air temperature (deg C)')


   def plot_temperatures(temperatures):
       plt.plot(temperatures, 'r-')
       plt.axhline(y=mean, color='b', linestyle='--')
       plt.savefig(f'{num_measurements}.png')
       plt.clf()


   for num_measurements in [25, 100, 500]:

       # read data from file
       data = pd.read_csv('temperatures.csv', nrows=num_measurements)
       temperatures = data['Air temperature (degC)']

       # compute statistics
       mean = sum(temperatures)/num_measurements

       # plot results
   #   plt.plot(temperatures, 'r-')
   #   plt.axhline(y=mean, color='b', linestyle='--')
   #   plt.savefig(f'{num_measurements}.png')
   #   plt.clf()
       plot_temperatures(temperatures)

- Discuss what we expect before running it (some will expect this not to work
  because variables seem undefined).
- Then try it out (it actually works).
- Discuss problems with this solution (what if we copy-paste the function to a different file?).


Small improvements
------------------

- Abstracting into more functions.
- Notice how the comments got redundant:

.. code-block:: python

  import pandas as pd
  from matplotlib import pyplot as plt


  def plot_data(data, xlabel, ylabel):
      plt.plot(data, 'r-')
      plt.xlabel(xlabel)
      plt.ylabel(ylabel)
      plt.axhline(y=mean, color='b', linestyle='--')
      plt.savefig(f'{num_measurements}.png')
      plt.clf()


  def compute_statistics(data):
      mean = sum(data)/num_measurements
      return mean


  def read_data(file_name, column):
      data = pd.read_csv(file_name, nrows=num_measurements)
      return data[column]


  for num_measurements in [25, 100, 500]:

      temperatures = read_data(file_name='temperatures.csv', column='Air temperature (degC)')

      mean = compute_statistics(temperatures)

      plot_data(data=temperatures, xlabel='measurements', ylabel='air temperature (deg C)')

Discuss what would happen if we copy-paste the functions to another project
(these functions are stateful/time-dependent).


Enemy of the state
------------------

Improve to more stateless functions:

.. code-block:: python
   :emphasize-lines: 6,15,20

   import pandas as pd
   from matplotlib import pyplot as plt
   import click


   def plot_data(data, mean, xlabel, ylabel, file_name):
       plt.plot(data, "r-")
       plt.xlabel(xlabel)
       plt.ylabel(ylabel)
       plt.axhline(y=mean, color="b", linestyle="--")
       plt.savefig(file_name)
       plt.clf()


   def compute_mean(data):
       mean = sum(data) / len(data)
       return mean


   def read_data(file_name, nrows, column):
       data = pd.read_csv(file_name, nrows=nrows)
       return data[column]


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


Unit tests
----------

Design code for testing.

- Move the main scope code into a main function.
- Discuss where to add a test and add a test to the statistics function:

.. code-block:: python
   :emphasize-lines: 3,20-22

   import pandas as pd
   from matplotlib import pyplot as plt
   import pytest


   def plot_data(data, mean, xlabel, ylabel, file_name):
       plt.plot(data, "r-")
       plt.xlabel(xlabel)
       plt.ylabel(ylabel)
       plt.axhline(y=mean, color="b", linestyle="--")
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


Command-line interface
----------------------

- Add a CLI for the input data file, the number of measurements, and the output
  file name.
- Example here is using ``click`` but it can equally well be ``optparse``, ``argparse``,
  or ``docopt``.
- Discuss the motivations for adding a CLI.

.. code-block:: python
   :emphasize-lines: 4,31-37

   import pandas as pd
   from matplotlib import pyplot as plt
   import pytest
   import click


   def plot_data(data, mean, xlabel, ylabel, file_name):
       plt.plot(data, "r-")
       plt.xlabel(xlabel)
       plt.ylabel(ylabel)
       plt.axhline(y=mean, color="b", linestyle="--")
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


   @click.command()
   @click.option(
       "--num-measurements", required=True, type=int, help="Number of measurements."
   )
   @click.option("--in-file", required=True, help="File name where we read from.")
   @click.option("--out-file", required=True, help="File name where we write to.")
   def main(num_measurements, in_file, out_file):

       temperatures = read_data(
           file_name=in_file, nrows=num_measurements, column="Air temperature (degC)",
       )

       mean = compute_mean(temperatures)

       plot_data(
           data=temperatures,
           mean=mean,
           xlabel="measurements",
           ylabel="air temperature (deg C)",
           file_name=out_file,
       )


   if __name__ == "__main__":
       main()


Split long script into modules
------------------------------

- Discuss how you would move some functions out and organize them into separate
  modules which can be imported to other projects: For instance
  ``compute_mean`` can be moved to ``statistics.py``.
- Discuss naming.
- Discuss interface design.


Summarize in the HackMD
-----------------------

Now return to initial questions on the HackMD and discuss questions and comments. If
there is time left, there are additional questions and exercises.
