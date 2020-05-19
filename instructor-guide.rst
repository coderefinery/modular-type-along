

Instructor guide (spoiler alert!)
=================================

One possible walk-through is presented here:
https://github.com/coderefinery/modular-type-along/commits/a-solution/compute.py

We don't have to follow this line by line but it's important to study
this example well before demonstrating this.

Emphasize that the example is Python but we will try to see "through"
the code and focus on the bigger picture and hopefully manage to imagine
other languages in its place.

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
