# Our task


## Data

The file [weather_data.csv](https://github.com/coderefinery/modular-type-along/blob/main/data/weather_data.csv)
([raw csv file](https://raw.githubusercontent.com/coderefinery/modular-type-along/main/data/weather_data.csv))
contains hourly air temperature measurements for the observation station
"Vantaa Helsinki-Vantaan lentoasema" (Helsinki airport) during 2024.

```{admonition} Origin of the data
Data obtained from
<https://en.ilmatieteenlaitos.fi/download-observations#!/> on 2025-09-18.

Data has been provided by the Finnish Meteorological Institute
under the Creative Commons Attribution 4.0 International license (CC BY 4.0):
<https://en.ilmatieteenlaitos.fi/open-data-licence>
```


## Our initial goal

Our initial goal for this exercise is to plot a series of temperatures and
precipitations for **January** and to compute and plot the **mean temperture**
averaged over the month. We imagine that we assemble a working script from
various internet research/ AI chat recommendations and arrive at:
:::::{tabs}
  ::::{group-tab} Python
    :::{literalinclude} code/initial-version.py
    :language: python
    :::
  ::::

  ::::{group-tab} R
    Work in progress. You can
    [help us](https://github.com/coderefinery/modular-type-along/issues/40)
    by contributing or improving an R solution.
  ::::
:::::

This example is in Python but we will try to see "through" the code and
focus on the bigger picture and hopefully manage to imagine other
languages in its place. For the Python experts: we will not see the most
elegant Python.


## Further goals

- Once we get this working for **January**, our task changes to also
  plot the **February** and the **March** in two additional
  plots.
- Later, we wish to generalize the code so that a user can compute and plot
  this for **any month**, **without changing the code** (with a command line
  interface).


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
