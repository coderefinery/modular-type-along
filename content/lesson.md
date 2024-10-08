# Our task


## Data

The file [temperatures.csv](https://github.com/coderefinery/modular-type-along/blob/main/data/temperatures.csv) ([raw csv file](https://raw.githubusercontent.com/coderefinery/modular-type-along/main/data/temperatures.csv))
contains hourly air temperature measurements for the observation station
"Vantaa Helsinki-Vantaan lentoasema" (Helsinki airport) during 2022.

```{admonition} Origin of the data
Data obtained from
<https://en.ilmatieteenlaitos.fi/download-observations#!/> on 2023-09-27.

Data has been provided by the Finnish Meteorological Institute
under the Creative Commons Attribution 4.0 International license (CC BY 4.0):
<https://en.ilmatieteenlaitos.fi/open-data-licence>
```


## Our initial goal

Our initial goal for this exercise is to plot a series of temperatures
for **25 measurements** and to compute and plot the **arithmetic mean**. We
imagine that we assemble a working script from various StackOverflow/ChatGPT
recommendations and arrive at:

```{literalinclude} code/initial-version.py
:language: python
```

This example is in Python but we will try to see "through" the code and
focus on the bigger picture and hopefully manage to imagine other
languages in its place. For the Python experts: we will not see the most
elegant Python.


## Further goals

- Once we get this working for **25 measurements**, our task changes to also
  plot the **first 100** and the **first 500 measurements** in two additional
  plots.
- Then we wish to generalize the code so that a user can compute and plot this
  for **any number**, **without changing the code** (with a command line interface).


## How we plan to solve it

Before we attempt to do this, we discuss with workshop participants how
they would tackle this problem.

Together we improve the code based on suggestions from learners towards
more modularity and re-usability.

```{instructor-note}
Participants give suggestions and ask questions via collaborative document
and instructor(s) try to follow and answer. They can also roughly follow
the ideas and steps in the {ref}`guide`.

It is OK and good if mistakes happen and it is fun if the instructor(s) can
convey a bit of "improv" feel to this lesson.
```


## Additional exercises

Draw a call tree for one of your recent projects. Identify the
functions in your call tree which are "pure" (which have no side-effects).
