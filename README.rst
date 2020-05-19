

Lesson material for "modular code development" lesson
=====================================================

Type-along/demo where we discuss and experience aspects of (un)modular
code development.

.. contents:: Table of contents


Starting questions for the `HackMD <https://hackmd.io>`__
---------------------------------------------------------

We share these questions in a common `HackMD <https://hackmd.io>`__ and we
wait until we have sufficiently many answers to question 1. But we also
encourage answering questions 2-5 which we revisit at the end of the
demo.

1. What does "modular code development" mean for you?
2. What best practices can you recommend to arrive at well structured,
   modular code in your favourite programming language?
3. What would you recommend your colleague who starts in the same
   programming language?
4. How do you deal with code complexity in your projects?
5. What do you know now that you wish somebody told you earlier?


Additional questions
--------------------

1. Do you design a new code project on paper before coding? Discuss pros
   and cons.
2. Do you build your code top-down or bottom-up? Discuss pros and cons.
3. Would you prefer your code to be 2x slower if it was easier to read
   it?


Learning topics
---------------

-  Know about pure functions (functions without side effects).
-  Learn why and how to limit side effects of functions.
-  Discuss why and how to limit side effects of data. Also discuss when
   mutable data may be preferable.
-  The Zen of Python: https://www.python.org/dev/peps/pep-0020/
-  Discuss why single-purpose functions are often preferred over
   multi-purpose functions.


Data
----

The file `temperatures.csv <temperatures.csv>`__ contains hourly air
temperature measurements for the time range November 1, 2019 12:00 AM -
November 30, 2019 11:59 PM for the observation station "Vantaa
Helsinki-Vantaan lentoasema".

Data obtained from
https://en.ilmatieteenlaitos.fi/download-observations#!/ on 2019-12-09.


Our initial goal
----------------

Our initial goal for this exercise is to plot a series of temperatures
for 25 measurements and to compute and plot the arithmetic mean. We
imagine that we assemble a working script from various StackOverflow
recommendations and arrive at `compute.py <compute.py>`__ (not a good
name but we will discuss naming later).

This example is in Python but we will try to see "through" the code and
focus on the bigger picture and hopefully manage to imagine other
languages in its place. For the Python experts: we will not see the most
elegant Python.

Once we get this working for 25 measurements, our task changes to also
plot the first 100 and the first 500 measurements in two additional
plots.

Before we attempt to do this, we discuss with workshop participants how
they would tackle this problem.


Additional exercises
--------------------

1. Draw a call tree for one of your recent projects. Identify the
   functions in your call tree which are pure.


For instructors (spoiler alert!)
--------------------------------

- `Instructor guide <instructor-guide.rst>`__
