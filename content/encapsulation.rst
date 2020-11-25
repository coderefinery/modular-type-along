Types of encapsulation
======================

Let's say you want to move a code from one system to another.  What are the things that can go wrong?

- In-language dependencies, e.g. Python. Can they all be expressed *only* in
  ``requirements.txt``?  Do you wrap everything in a container?
- Paths. Can you always use relative paths?
- OS dependencies, libraries, etc. Can you eliminate them?
- Data files. Are they controlled or few that you can migrate, or if you wanted
  to move it, are you forced to copy the whole directory without regard to what
  the file is (thus creating a lot of duplicates, and a big mess?)
- Are you using something that is OS-specific (GNU/Linux vs BSD)?
- Do you use support programs only available on certain computers?  Fewer
  external utilities you use = easier portability.
