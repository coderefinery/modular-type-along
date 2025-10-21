# One possible solution

## Before we start

We **don't have to follow this line by line** but it's important to study
this example well before demonstrating this.

Emphasize that the example is Python but we will try to see "through"
the code and **focus on the bigger picture** and hopefully manage to imagine
other languages in its place.

We **collect ideas and feedback in the collaborative document while coding** and the instructor
tries to react to that without going into the rabbit hole.

Learners can also explore some of these steps in one of the exercise sessions.


## Checklist

- Start with notebook
- Add statistics (mean temperature)
- Add precipitation
- Generalize from January to also February and March data
- Abstract code into functions
- Move from notebook to script
- From functions with side-effects towards stateless functions
- Initialize git
- Add `requirements.txt`
- Add test
- Add command line interface
- Show how a workflow solution could look
- Split into multiple files/modules


## Our initial version

We imagine that we assemble a working script/code
from various internet research/ AI chat
recommendations and arrive at:

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

- We test it out **in a notebook**.


## We add a dashed line representing the mean temperature

This is still only the January data.

:::::{tabs}
  ::::{group-tab} Python
    :::{literalinclude} code/initial-version-with-mean.py
    :language: python
    :emphasize-lines: 27-36
    :::
  ::::

  ::::{group-tab} R
    Work in progress. You can
    [help us](https://github.com/coderefinery/modular-type-along/issues/40)
    by contributing or improving an R solution.
  ::::
:::::


## We add another plot for the precipitation

As a first go, we achieve this by copy pasting the existing code and adjusting
it for the precipitation column.

:::::{tabs}
  ::::{group-tab} Python
    :::{literalinclude} code/initial-version-with-precipitation.py
    :language: python
    :emphasize-lines: 49-68
    :::
  ::::

  ::::{group-tab} R
    Work in progress. You can
    [help us](https://github.com/coderefinery/modular-type-along/issues/40)
    by contributing or improving an R solution.
  ::::
:::::


## Plotting also February and March data

- Copy-pasting very similar code 6 times would be too complicated to maintain.
- We avoid this by iterating over the first 3 months.
- Instead of reusing `data`, we introduce `data_month`.

:::::{tabs}
  ::::{group-tab} Python
    :::{literalinclude} code/add-iteration.py
    :language: python
    :emphasize-lines: 15-16,22-23,28,54-55
    :::
  ::::

  ::::{group-tab} R
    Work in progress. You can
    [help us](https://github.com/coderefinery/modular-type-along/issues/40)
    by contributing or improving an R solution.
  ::::
:::::


## Abstracting the plotting part into a function

:::::{tabs}
  ::::{group-tab} Python
    :::{literalinclude} code/abstracting-plot.py
    :language: python
    :emphasize-lines: 5,53-66
    :::
  ::::

  ::::{group-tab} R
    Work in progress. You can
    [help us](https://github.com/coderefinery/modular-type-along/issues/40)
    by contributing or improving an R solution.
  ::::
:::::

- Discuss the advantages of what we have done here.
- Discuss what we expect before running it (we might expect this not to work
  because `data_month` seems undefined inside the function).
- Then try it out (it actually works).
- Discuss problems with this solution (what if we copy-paste the function to a
  different file?).

The point of this step was that abstracting code into functions can be really
good for re-usability but just the fact that we created a function does not
mean that the function is reusable since in this case it depends on a variable
defined outside the function and hence there are **side-effects**.


## Small improvements

- Abstracting into more functions.
- Notice how some code comments got redundant:

:::::{tabs}
  ::::{group-tab} Python
    :::{literalinclude} code/small-improvements.py
    :language: python
    :emphasize-lines: 5-14,17-19,34,56
    :::
  ::::

  ::::{group-tab} R
    Work in progress. You can
    [help us](https://github.com/coderefinery/modular-type-along/issues/40)
    by contributing or improving an R solution.
  ::::
:::::

Discuss what would happen if we copy-paste the functions to another project
(these functions are stateful/time-dependent).

Emphasize how stateful functions and order of execution in Jupyter notebooks
can produce unexpected results and explain why we motivate to rerun all cells
before sharing the notebook.


## Move from notebook to script

- "File" -> "Save and Export Notebook As ..." -> "Executable Script"
- `git init` and commit the working version.
- Add `requirements.txt` and motivate how that can be useful to have later.

As we continue from here, **create commits after meaningful changes** and later
also share the repository with learners. This nicely connects to other lessons
of the workshop.


## Towards functions without side-effects

In Python we can detect problems by encapsulating all code into functions and
when using a code editor with a static checker (instructor can demonstrate
this by first introducing a main function, then detecting problems, then
fixing the problems):
:::{figure} undefined.png

After we have tucked the "main" code under a main function, an editor with
linter/checker enabled highlights undefined names and variables which are
assigned but never used.  The screenshot was obtained from a vim editor with
[ruff](https://docs.astral.sh/ruff/) language server enabled.
:::

We then improve towards:

:::::{tabs}
  ::::{group-tab} Python
    :::{literalinclude} code/towards-pure.py
    :language: python
    :emphasize-lines: 22,27-28,34,53,56,61,83-84
    :::
  ::::

  ::::{group-tab} R
    Work in progress. You can
    [help us](https://github.com/coderefinery/modular-type-along/issues/40)
    by contributing or improving an R solution.
  ::::
:::::

These functions can now be copy-pasted to a different notebook or project and
they will still work.


## Unit tests

- Discuss what one could mean with "design code for testing".
- Discuss when to test and when not to test.
- Discuss where to add a test and add a test to the `arithmetic_mean` function:

:::::{tabs}
  ::::{group-tab} Python
    :::{literalinclude} code/testing.py
    :language: python
    :emphasize-lines: 3,23-25
    :::
  ::::

  ::::{group-tab} R
    Work in progress. You can
    [help us](https://github.com/coderefinery/modular-type-along/issues/40)
    by contributing or improving an R solution.
  ::::
:::::


## Command-line interface (CLI)

- Add a CLI for the input data file, the month, and the output folder.
- Instructor demonstrates it, for instance:
  ```console
  $ python example.py --month 2024-05 --data-file weather_data.csv --output-directory /home/user/example/results
  ```
- Example here is using [click](https://click.palletsprojects.com/) but it can
  equally well be [optparse](https://docs.python.org/3/library/optparse.html),
  [argparse](https://docs.python.org/3/library/argparse.html),
  [docopt](http://docopt.org/), or [Typer](https://typer.tiangolo.com/).
- Discuss the motivations for adding a CLI:
  - We are able to modify the behavior without changing (or needing to
    understand) the code
  - We can run many of such scripts as part of a workflow

:::::{tabs}
  ::::{group-tab} Python
    :::{literalinclude} code/cli.py
    :language: python
    :emphasize-lines: 1,7,66-84
    :::
  ::::

  ::::{group-tab} R
    Work in progress. You can
    [help us](https://github.com/coderefinery/modular-type-along/issues/40)
    by contributing or improving an R solution.
  ::::
:::::


## Split long script into modules

- Discuss how you would move some functions out and organize them into separate
  modules which can be imported to other projects.
- Discuss naming.
- Discuss interface design.


## Summarize in the collaborative document

- Now return to initial questions on the collaborative document and discuss
  questions and comments. If there is time left, there are additional
  questions and exercises.
- It is easier and more fun to teach this as a pair with somebody else where
  one person can type and the other person helps watching the questions and
  commends and relays them to the co-instructor.
