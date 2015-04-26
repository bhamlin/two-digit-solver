# two-digit-solver
A solver for http://cleverweek.itch.io/two-digits

### Why?
Why not?

### What is it?
This program finds solutions for the game Two Digits on itch.io.  It was a more interesting problem than the puzzle in the game itself.

### Use
This application is used by running it with the numbers as command line arguments.

**`python3`** `solve.py` *`8 19 71 36 55 39 42 14 56`*

This will print out a list of solutions.  The solution line consists of the total of each group, and then each group.

```
50 (8, 42) (36, 14)
58 (8, 36, 14) (19, 39)
...
166 (19, 36, 55, 56) (71, 39, 42, 14)
170 (19, 39, 42, 14, 56) (8, 71, 36, 55)
```

Just select the sets as directed for whichever sum you want.

![Example](http://i.imgur.com/BAMArjO.png)
