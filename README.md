# Dandelions

## Background

Dandelions is a pen-and-paper game developed by Ben Orlin and included in his amazing 2022 book
"Math Games with Bad Drawings".

To play the game, two players each take a role, either Dandelion or Wind.

Then they draw a 5&times;5 grid and a compass with eight cardinal directions.

They take seven turns. On a turn, first the Dandelion player places one dandelion on the grid,
then the Wind player chooses a direction to blow the wind. When the wind blows, the players draw
seeds in each space from the dandelion to the border in the direction it blew.

On each turn, the Dandelion player places a new dandelion and the Wind player blows in a new
direction. The Wind cannot blow in the same direction twice, but new Dandelions can grow where seeds
already exist.

At the end of the game, if the board is full of dandelions and seeds, the Dandelion player wins. If
even one space is empty, the Wind wins.

## Learning Python

To help me learn Python, I'm programming an automatic version of this game.

### Step 1

The first step is to represent the data. And while I'm at it I should make functions to visualize
the data.

The board looks like this when it's blank:

```
 - - - - -
|         |
 - - - - -
|         |
 - - - - -
|         |
 - - - - -
|         |
 - - - - -
|         |
 - - - - -
```

And it looks like this when it's full of dandelions:

```
 - - - - -
|* * * * *|
 - - - - -
|* * * * *|
 - - - - -
|* * * * *|
 - - - - -
|* * * * *|
 - - - - -
|* * * * *|
 - - - - -
```

It's not a valid board state for the board to be full of dandelions, but we want to visualize any
state, even invalid ones.

The compass looks like this when the game starts:

```

 +

```

And it looks like this after 8 turns:

```
\|/
-+-
/|\
```

Again, this is an invalid state, because only 7 turns are allowed.

In my [first commit](https://github.com/dankuck/dan-learns-python/commit/b70678701aa3ccab74792be325fa41d0a3e110d1),
in main.py, I've laid out the functions `board_to_string` and
`compass_to_string`.

The board is represented by an array of 5 arrays of 5 strings. In a board, an empty space is `' '`,
a dandelion is `'*'`, and a seed is `'.'`.

The compass is represented by a dictionary of abbreviated cardinal directions as the keys and
booleans as the values. A compass starts out with all values `False`, and as turns are taken, values
change to `True`.

Right now I'm unhappy with how complicated `board_to_string` looks. But it works fine, so I'll
probably leave it for a while.

I printed test boards and compasses and got the results above. Now we're cooking!

#### What did I learn in Step 1?

I got a lot of error messages reminding me to put a `:` after `def`, `if`, and `else` statements.

I also learned that the `join` method is found on a string and accepts an array parameter.

Dictionaries look like they do in many other languages and trailing commas are not a problem.

`True` and `False` are written in that casing.

Python doesn't have the usual ternary expressions. If it has anything like that, I still need to
find it.

Closures are called lambdas and use the `lambda` keyword.

`map` is a freestanding function.

