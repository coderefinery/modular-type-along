(guide)=

# Instructor guide (spoiler alert!)


## Before we start

We **don't have to follow this line by line** but it's important to study
this example well before demonstrating this.

Emphasize that the example is Python but we will try to see "through"
the code and **focus on the bigger picture** and hopefully manage to imagine
other languages in its place.

We **collect ideas and feedback in the collaborative document while coding** and the instructor
tries to react to that without going into the rabbit hole.

We recommend to go through this together where the instructor(s) demonstrate(s)
and learners can commend, suggest, and ask questions, and we are either all in
the same video room or everybody is watching via stream. In other words, for
this lesson, **learners are not in separate breakout-rooms**.


## Checklist

- Start with notebook
- Generalize from 1 figure to 3 figures
- Abstract code into functions
- From functions with side-effects towards stateless functions
- Move from notebook to script
- Initialize git
- Add `requirements.txt`
- Add test
- Add command line interface
- Split into multiple files/modules


## Our initial version

We imagine that we assemble a working script from various StackOverflow
recommendations and arrive at:

```{literalinclude} code/initial-version.py
:language: python
```

- We test it out **in a notebook**.


## We add axis labels

It's not the best placement but it works and later it will bite us (only the
first plot will have labels) and we will improve it:

```{literalinclude} code/with-axis-labels.py
:language: python
:emphasize-lines: 4,5
```

Once we get this working for 25 measurements, our task changes to also
plot the first 100 and the first 500 measurements in two additional
plots.


## Plotting also 100 and 500 measurements

- Next idea is perhaps code duplication.
- Then a for-loop to iterate over `[25, 100, 500]`:

```{literalinclude} code/add-iteration.py
:language: python
:emphasize-lines: 7
```


## Abstracting the plotting part into a function

```{literalinclude} code/abstracting-plot.py
:language: python
:emphasize-lines: 8-13,26-30
```

- Discuss what we expect before running it (some will expect this not to work
  because variables seem undefined).
- Then try it out (it actually works).
- Discuss problems with this solution (what if we copy-paste the function to a different file?).

The point of this step was that abstracting code into functions can be really
good for reusability but just the fact that we created a function does not mean
that the function is reusable since in this case it depends on a variable
defined outside the function and hence there are side-effects.


## Small improvements

- Abstracting into more functions.
- Notice how the comments got redundant:

```{literalinclude} code/small-improvements.py
:language: python
:emphasize-lines: 27,29,31
```

Discuss what would happen if we copy-paste the functions to another project
(these functions are stateful/time-dependent).

Emphasize how stateful functions and order of execution in Jupyter notebooks
can produce unexpected results and explain why we motivate to rerun all cells
before sharing the notebook.


## Towards functions without side-effects

Improve to more stateless functions:

```{literalinclude} code/towards-pure.py
:language: python
:emphasize-lines: 6,15,20
```

These functions can now be copy-pasted to a different notebook or project and
they will still work.


## Move from notebook to script

Adding unit tests is often the moment when notebook is not the right fit
anymore.

But before we add tests:
- "File" -> "Save and Export Notebook As ..." -> "Executable Script"
- `git init` and commit the working version.
- Add `requirements.txt` and motivate how that can be useful to have later.

As we continue from here, **create commits after meaningful changes** and later
also share the repository with learners.  This nicely connects to other lessons
of the workshop.


## Unit tests

Design code for testing.

- Move the main scope code into a main function.
- Discuss where to add a test and add a test to the statistics function:

```{literalinclude} code/testing.py
:language: python
:emphasize-lines: 3,11,21-23
```


## Command-line interface

- Add a CLI for the input data file, the number of measurements, and the output
  file name.
- Example here is using [click](https://click.palletsprojects.com/) but it can
  equally well be [optparse](https://docs.python.org/3/library/optparse.html),
  [argparse](https://docs.python.org/3/library/argparse.html),
  [docopt](http://docopt.org/), or [Typer](https://typer.tiangolo.com/).
- Discuss the motivations for adding a CLI:
   - We are able to modify the behavior without changing the code
   - We can run many of such scripts as part of a workflow

```{literalinclude} code/cli.py
:language: python
:emphasize-lines: 4,31-37
```


## Split long script into modules

- Discuss how you would move some functions out and organize them into separate
  modules which can be imported to other projects: For instance
  `compute_mean` can be moved to `statistics.py`.
- Discuss naming.
- Discuss interface design.


## Summarize in the collaborative document

- Now return to initial questions on the collaborative document and discuss questions and comments. If
  there is time left, there are additional questions and exercises.
- It is easier and more fun to teach this as a pair with somebody else where
  one person can type and the other person helps watching the questions and
  commends and relays them to the co-instructor.
