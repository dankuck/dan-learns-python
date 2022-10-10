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

The board is represented by a list of 5 lists of 5 strings. In a board, an empty space is `' '`,
a dandelion is `'*'`, and a seed is `'.'`.

The compass is represented by a dictionary of abbreviated cardinal directions as the keys and
booleans as the values. A compass starts out with all values `False`, and as turns are taken, values
change to `True`.

Right now I'm unhappy with how complicated `board_to_string` looks. But it works fine, so I'll
probably leave it for a while.

I printed test boards and compasses and got the results above. Now we're cooking!

#### What did I learn in Step 1?

I got a lot of error messages reminding me to put a `:` after `def`, `if`, and `else` statements.

I also learned that the `join` method is found on a string and accepts a list parameter.

Dictionary and list literals look like they do in many other languages and trailing commas are not
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

The function that gives the length of a string or list is `len`.

### Step 4

It's time to take some action. During the game, the wind will blow seeds from dandelions.

Say a player has set down a dandelion in the center of the board:

```
 - - - - -
|         |
 - - - - -
|         |
 - - - - -
|    *    |
 - - - - -
|         |
 - - - - -
|         |
 - - - - -
```

Next suppose the other player blows the wind to the north-east. That would result in a board state
like this:

```
 - - - - -
|        .|
 - - - - -
|      .  |
 - - - - -
|    *    |
 - - - - -
|         |
 - - - - -
|         |
 - - - - -
```

If the first player places a dandelion just below the first and then the wind blows to the west, the
board state would become:

```
 - - - - -
|        .|
 - - - - -
|      .  |
 - - - - -
|. . *    |
 - - - - -
|. . *    |
 - - - - -
|         |
 - - - - -
```

In my [fourth commit](https://github.com/dankuck/dan-learns-python/commit/62e9ef81569593747454b6efd2d4c38bcdae024e),
I created a new module called `wind` with a method called `blow` which takes a board and direction
as parameters and then fills in seeds at the right locations in the board lists.

My first solution had problems if a dandelion was placed at the border. And it overwrote dandelions
with seeds if they happened to be in the way of some other dandelion. Once I worked out those
problems it worked perfectly.

I used recursion to extend the seeds all the way to the border, and it worked without any surprises.

#### What did I learn in Step 4?

You can compare lists with `==`. Even deeply, because comparing lists involves comparing their
elements and if their elements are lists, `==` still works.

The `for` loop only has one form, the one that iterates over iterables. Plus if you want the index
of a list while you loop, you must first convert the list to a dictionary using `enumerate`.

`if` and `else` are easy, but you have to remember `elif`.

`or` is spelled like that.

### Step 5

Brandon Shar showed me how to do ternary expressions so I thought I might as well try it in
`compass_to_string`.

I did it in my [fifth commit](https://github.com/dankuck/dan-learns-python/commit/0bb95fe7dec628f87a6ca8d122c9bd50142a4043),
but I can't tell if it's any easier to look at.

While I was at it, I refactored `board_to_string` and it looks a little better. I took away what
turned out to be a spurious use of `list()` and split parts of the work onto different lines.

#### What did I learn in Step 5?

The ternary expression, the one which yields one value under a true condition and another value
under a false condition, looks like `<true value> if <test expression> else <false value>`.

Because Python has no end-of-statement character, there are just a few ways to spread a statement
onto multiple lines: putting `\` at the end of a line; opening parentheses on one line and only
closing them on a later line; as part of a multiline string.

### Step 6

I really prefer that each action on the game board would produce a new instance of the board list.
That way I could choose to keep a list of states that led to each other.

In my [sixth commit](https://github.com/dankuck/dan-learns-python/commit/206ced08e65719993292029d49ff490b28db6262),
I use the standard library's `deepcopy` function from the `copy` module to copy the board passed
into `blow` before making any changes.

I'm a bit troubled that I'll have to remember to use `deepcopy` again later. The other time a board
can be altered is when a dandelion is placed. Maybe I'll find a better place for it.

#### What did I learn in Step 6?

Apropos of nothing, there are 97,684,392,960,000 different paths the game could take.

Lists have their own `copy` method but it makes a shallow copy and I needed a deep copy. The `copy`
library has `deepcopy`.

### Step 7

I started writing strategy classes, which will generate the moves to play the game, but I stopped
when I realized they need something.

In a way, strategy classes run "on top" of this
Dandelions engine. So the engine needs to respond to mistakes. It also needs to handle as
much boiler plate as it can.

With that in mind, I created `plant` in a new module `dandelion` in my [seventh commit](https://github.com/dankuck/dan-learns-python/commit/a6cb6496d9823f8448fd762c90ea164928928267).
`plant` places a dandelion onto the board, but throws an exception if (a) a dandelion is already
there or (b) the location is outside the board. These are all the illegal moves the Dandelion player
can make.

#### What did I learn in Step 7?

Python has a second array-like structure called a "tuple", which is immutable. Soon, dandelion
strategy classes will return a tuple with `x`, `y` coordinates because that just seems like the
right data structure in Python.

Tuples and lists can be "unpacked". Example: `x, y = move`.

In Python we "raise" exceptions using `raise` and provide an instance of an exception class.

Classes are instantiated by simply calling them like functions. Example:
`raise RuntimeError('BAD')`.

When you catch an exception (using `except`), you don't even have to give it a name if you're not
going to inspect it at all.

Python throws an exception on its own if you attempt to assign to an index beyond the end of a list.
You have to use `append` for that. But if you attempt to assign to a negative index, Python's magic
interprets that as the end of the list - n.

At first, I left it to Python to raise an exception when the x or y coordinates were too large, but
then I remembered that there is unnecessary work we can avoid if the function checks for those
values early.
