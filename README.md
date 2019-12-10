

# Lesson material for "modular code development" lesson

Type-along/demo where we discuss and experience aspects of (un)modular code development.


## Starting questions for the hackpad

We share these questions in a common hackpad (https://hackmd.io) and we wait until we have sufficiently many
answers to question 1. But we also encourage answering questions 2-4 which we revisit at the end of the demo.

1. What does "modular code development" mean for you?
2. What best practices can you recommend to arrive at well structured, modular code in your favourite programming language?
3. What would you recommend your colleague who starts in the same programming language?
4. How do you deal with code complexity in your projects?


## Data

The file [temperatures.csv](temperatures.csv) contains hourly air temperature measurements
for the time range November 1, 2019 12:00 AM - November 30, 2019 11:59 PM
for the observation station "Vantaa Helsinki-Vantaan lentoasema".

Data obtained from https://en.ilmatieteenlaitos.fi/download-observations#!/ on
2019-12-09.


## Our initial goal

Our initial goal for this exercise is to plot a series of temperatures for 25
measurements and to compute and plot the arithmetic mean. We imagine that we
assemble a working script from various StackOverflow recommendations and arrive
at [compute.py](compute.py) (not a good name but we will discuss naming later).

This example is in Python but we will try to see "through" the code and focus on the bigger
picture and hopefully manage to imagine other languages in its place.
For the Python experts: we will not see the most elegant Python.

Once we get this working for 25 measurements, our task changes to also plot the
first 100 and the first 500 measurements in two additional plots.

Before we attempt to do this, we discuss with workshop participants how they
would tackle this problem.


## Learning topics

- Know about pure functions (functions without side effects).
- Learn why and how to limit side effects of functions.
- Discuss why and how to limit side effects of data. Also discuss when mutable data may be preferable.
- The Zen of Python: https://www.python.org/dev/peps/pep-0020/
- Discuss why single-purpose functions are often preferred over multi-purpose functions.


## Additional questions

1. Do you design a new code project on paper before coding? Discuss pros and cons.
2. Do you build your code top-down or bottom-up? Discuss pros and cons.
3. Would you prefer your code to be 2x slower if it was easier to read it?


## Additional exercises

1. Draw a call tree for one of your recent projects. Identify the functions in your call tree which are pure.


## For instructors (spoiler alert!)

One possible walk-through is presented here:
https://github.com/coderefinery/modular-type-along/commits/a-solution/compute.py

We don't have to follow this line by line but it's important to study this example
well before demonstrating this.

Emphasize that the example is Python but we will try to see "through" the code and focus on the bigger
picture and hopefully manage to imagine other languages in its place.

1. Start with code duplication and discuss the possible problems with this approach.
2. Abstract code into two functions, one for reading data, one for computing and plotting.
3. Convert the latter into a multi-purpose functions which can be used to get only the statistics without a plot using an optional argument. Discuss the pros and cons (cohesion, increased dependency graph, future refactoring).
4. Generalize towards single-purpose functions by abstracting out the statistics function.
5. Discuss what would happen if we copy-paste the statistics function to another project (this function is stateful/time-dependent).
6. Improve to more stateless functions.
7. Discuss where to add a test and add a test to the statistics function.
8. Discuss how you would move that function out and organize into a separate module.

Now return to initial questions on the hackpad and discuss them. If there is
time left, there are additional questions and exercises (above).
