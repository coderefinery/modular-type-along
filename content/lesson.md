# Our task


## Data

The file [temperatures.csv](https://github.com/coderefinery/modular-type-along/blob/master/data/temperatures.csv)
contains hourly air temperature measurements for the time range November 1,
2019 12:00 AM - November 30, 2019 11:59 PM for the observation station "Vantaa
Helsinki-Vantaan lentoasema".

Data obtained from
<https://en.ilmatieteenlaitos.fi/download-observations#!/> on 2019-12-09.


## Our initial goal

Our initial goal for this exercise is to plot a series of temperatures
for 25 measurements and to compute and plot the arithmetic mean. We
imagine that we assemble a working script from various StackOverflow
recommendations and arrive at:

```python
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
```

This example is in Python but we will try to see "through" the code and
focus on the bigger picture and hopefully manage to imagine other
languages in its place. For the Python experts: we will not see the most
elegant Python.


## Further goal

Once we get this working for **25 measurements**, our task changes to also
plot the **first 100** and the **first 500 measurements** in two additional
plots.

Before we attempt to do this, we discuss with workshop participants how
they would tackle this problem.

Together we improve the code based on suggestions from learners towards
more modularity and re-usability.

```{instructor-note}
Participants give suggestions and ask questions via collaborative document
and instructor(s) try to follow and answer. They can also roughly follow
the ideas and steps in the instructor guide.

It is OK and good if mistakes happen and it is fun if the instructor(s) can
convey a bit of "improv" feel to this lesson.
```


## Additional exercises

Draw a call tree for one of your recent projects. Identify the
functions in your call tree which are "pure" (which have no side-effects).
