# Exercise 2


:::{admonition} You can participate in two ways
- Either by discussing with others and writing your own thoughts via collaborative notes
- Or by coding
- Or a mix of the two that is most meaningful for you or your group
:::


## Discussion track

The topic of this discussion session is encapsulation.
Can you please comment on these recommendations in the collaborative notes and perhaps suggest
other recommendations which have helped in your work and others could find useful?


:::{discussion} Types of encapsulation
Let's say you want to move a code from one system to another.  What are the things that can go wrong?

- **In-language dependencies**, e.g. Python. Can they all be expressed *only* in
  ``requirements.txt``?  Do you wrap everything in a container?
- **Paths**: Can you always use relative paths?
- **Operating-system (OS) dependencies, libraries, etc.**: Can you eliminate them?
- **Data files**: Are they controlled or few that you can migrate, or if you wanted
  to move it, are you forced to copy the whole directory without regard to what
  the file is (thus creating a lot of duplicates, and a big mess?)
- Are you using something that is **OS-specific** (GNU/Linux vs BSD)?
- Do you use support programs only available on certain computers?  Fewer
  external utilities you use = easier portability.
:::


:::{discussion} What needs to be global vs what needs to be local?
- Global data can be "seen"/accessed in the entire code.
- Local data is only available in the local vicinity of its definition.
- Try to have as little global data as possible.
- Global data are often input parameters, configuration parameters, command-line arguments.
- But try to localize these to the "main" code/function.
:::



## Coding track

Here you can continue either with some of the coding tasks from the first
exercise session or you can program something inspired by our live-coding
session.
