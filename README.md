# Dandelions

## Background

Dandelions is a pen-and-paper game developed by Ben Orlin and included in his amazing 2022 book
"Math Games with Bad Drawings".

To play the game, two players each take a role, either Dandelion or Wind.

Then they draw a 5&times;5 grid and a compass with eight cardinal directions.

They take seven turns. On a turn, first the Dandelion player places one dandelion on the grid,
then the Wind player chooses a direction to blow the wind. When the wind blows, the players draw
seeds in each space from all the dandelions to the border in the direction it blew.

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

Dictionary and array literals look like they do in many other languages and trailing commas are not
a problem.

`True` and `False` are written in that casing.

Python doesn't have the usual ternary expressions. If it has anything like that, I still need to
find it.

Closures are called lambdas and use the `lambda` keyword.

`map` is a freestanding function.

### Step 2

It's never too early to get organized, so in my [second commit](https://github.com/dankuck/dan-learns-python/commit/42000deb5bfaf76817e7d22614eada67e33332f1),
I move the functions into a module called `to_string`, then add the import statements in my main
script.

I ran main.py again and got the same results.

#### What did I learn in Step 2?

Modules are as easy as just putting your functions into a file and using:

`from filename import function_name, other_function_name`

I've heard there's another way too, but the easy way works for now.

### Step 3

Now seems like a good time to build some automated tests.

In my [third commit](https://github.com/dankuck/dan-learns-python/commit/e377d438b18fa4976a56261b6ba39e4aca4a1d54), I create `test.py`, a script that runs all the exercises in `main.py` and also
asserts that the results are equal to some expected values.

After some back and forth that had more to do with learning how to manipulate strings than with the
code under test, I got four tests passing.

I don't use a framework for the tests, not yet anyway. I just include some test functions and run
them, being sure to count how many pass. I use Python's `assert` which throws exceptions, so
the first test that fails stops execution.

#### What did I learn in Step 3?

Python's multiline string literals start and end with triple quotes. Any indentation between those
is preserved, making it uncomfortable to use multiline string literals inside of functions or
blocks.

Python's standard library provides a solution to this in a module called `textwrap` with a function
called `dedent`.

`dedent` didn't help me writing tests because indents weren't the only whitespace I needed to get
exactly right when doing comparisons in my tests. But now I know it's there.

Python has an `assert` function which is like the one from C and Java: it can be used anywhere and
it's usually turned off in production. This represents a sort of "mix your tests with your code"
philosophy that we can just... not do.

For the simple tests I wrote, the `assert` function worked fine. Of course, it doesn't explain why
assertions fail in detail.

The substring features built into Python's strings are really enjoyable. When `string == expected`
started to fail assertions, it was easy to change them to `string[0] == expected[0]` which passed
and then `string[0:15] == expected[0:15]` which failed, and then binary search my way to the
problem character. (It was a whitespace character at index 11 from when I was still trying to use
multiline strings.)

The function for the length of a string or array is `len`.
