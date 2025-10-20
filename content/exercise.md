# Exercise


:::{admonition} You can participate in two ways
- Either by discussing with others and writing your own thoughts via collaborative notes
- Or by coding
- Or a mix of the two that is most meaningful for you or your group
:::


## Discussion track

We share these questions in a common collaborative document:
```
A. What does "modular code development" mean for you?
B. What best practices can you recommend to arrive at well structured,
   modular code in your favourite programming language?
C. What do you know now about programming that you wish somebody told you earlier?
D. Do you design a new code project on paper before coding? Discuss pros
   and cons.
E. Do you build your code top-down (starting from the big picture) or bottom-up
   (starting from components)? Discuss pros and cons.
F. Would you prefer your code to be 2x slower if it was easier to read and understand?
```

They can be answered by individual learners but also discussed within an
exercise group.


## Coding track

You can practice on our [exercise repository](https://github.com/coderefinery/modular-type-along-exercise) which contains:
- Data set
- Python notebook which works but is not super general

How to contribute improvements:
- Open issue at the [exercise repository](https://github.com/coderefinery/modular-type-along-exercise) and in your pull request refer to that issue.

Exercise ideas (sorted from basic to advanced):
- Improve the README
- Add example usage to the README
- Add a result image to the README
- Make it installable and document installation (requirements.txt or environment.yml, pip/conda/...)
- Add a command line interface
- Improve error messages (e.g. input file does not exist or does not contain data we want to plot)
- Draw a call tree for one of your recent projects. Identify the
  functions in your call tree which are "pure" (which have no side-effects).
- Add more automated tests
- Try some of the strategies in this lesson on your own data
- Contribute a notebook/script with weather data from your place **in your
  favorite programming language**
- If you use AI, any tricks you can share to get modular code from it?
- Make the notebook (more) reproducible
- Add support for Snakemake or any other workflow management tool
