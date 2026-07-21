# Encapsulation
Encapsulation in software development refers to isolating a piece of software and its dependencies from the external environment so that it can function, be reused, or moved independently.
It can happen at different levels — within code (e.g., functions, classes, or modules), within environments (e.g., virtual environments, containers), or even at the system level (e.g., portable workflows and data management).

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
