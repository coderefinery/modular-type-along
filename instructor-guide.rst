

Instructor guide (spoiler alert!)
=================================


Before we start
---------------

We don't have to follow this line by line but it's important to study
this example well before demonstrating this.

Emphasize that the example is Python but we will try to see "through"
the code and focus on the bigger picture and hopefully manage to imagine
other languages in its place.


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


We test it.


We added axis labels
--------------------

.. code-block:: python

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

...


Rest
----

1.  Start with code duplication and discuss the possible problems with
    this approach.
2.  Abstract code into two functions, one for reading data, one for
    computing and plotting.
3.  Convert the latter into a multi-purpose functions which can be used
    to get only the statistics without a plot using an optional
    argument. Discuss the pros and cons (cohesion, increased dependency
    graph, future refactoring).
4.  Generalize towards single-purpose functions by abstracting out the
    statistics function.
5.  Discuss what would happen if we copy-paste the statistics function
    to another project (this function is stateful/time-dependent).
6.  Improve to more stateless functions.
7.  Discuss where to add a test and add a test to the statistics
    function.
8.  Discuss how you would move that function out and organize into a
    separate module.
9.  Discuss naming.
10. Discuss inteface design.

Now return to initial questions on the hackpad and discuss them. If
there is time left, there are additional questions and exercises
(above).
