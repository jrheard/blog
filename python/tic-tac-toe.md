---
layout: page
title:  "Madison CS 3-4: Tic-Tac-Toe"
---

In this project, you'll write a program that lets you play a game of tic-tac-toe against a computer opponent.

The goal of this project is to get you comfortable with writing **functions**. You've been using functions all year, but in this project you'll write more of them at one time than you have before.

Before we start, I want to spend just a quick second talking about how I think about functions, because I think it's a useful picture to have in your head. It's helped me a lot.

Functions are like LEGO blocks.

<img src="{{ site.baseurl }}/assets/img/lego.jpg" />

A LEGO block is a small, simple thing—but if you put a bunch of those simple blocks together in the right way, you can make the Milennium Falcon, or the Eiffel Tower, or I don't know, a pizza or a dog or something.

Functions are just like that. **The functions you write should each be small, simple, and easy to understand**—but if you put a bunch of your functions together in the right way, you can make a website, or control a robot, or fly a spaceship.

The best part about functions is that they're even better than LEGO blocks, because you can make your own! When you buy a LEGO set, you're stuck with whatever kinds of blocks come with the set; when you use a programming language, you can use its built-in functions to make _your own_ way cooler functions that do whatever you want, and then you can put _those_ functions together to make a program that does something awesome. Functions are basically my favorite thing about programming.

OK, enough philosophy. Let's write some simple functions and put them together to make a tic-tac-toe game!

## Demo

The game we're making will look like this (the "index" stuff will make more sense in a second, keep reading):

<asciinema-player src="{{ site.baseurl }}/tictactoe_cast.json" rows="25" cols="95" autoplay="true" loop="true"></asciinema-player>

(The idea for this project was taken from Al Sweigart's excellent book "Invent Your Own Computer Games With Python".)

## Representing The Board

A game of tic-tac-toe takes place on a 3x3 board. A space on the board is either empty, or it has an X in it, or it has an O in it.

We need to **represent** that board in our program somehow - we need to have a variable whose value is a tic-tac-toe board. Python doesn't come with a tic-tac-toe-board data type, so we'll have to make our own!

I think that a good way to represent a tic-tac-toe board in Python would be to use a list of strings, like this:

```python
['X', 'O', ' ', ' ', 'O', 'X', 'X', 'O', ' ']
```

That's a list of nine strings, because that's how many spaces there are on a 3x3 tic-tac-toe board. Each string is either `'X'` or `'O'` or `' '`.

Tic-tac-toe boards are squares, but that list above is just a straight line, it isn't a square. How can we use a list with 9 elements to represent a 3x3 square?

Well, we could just say: the first three elements in the list are the top row of the board, and the second three elements are the middle row, and the last three are the bottom row. Like this:

```python
# This list:
['X', 'O', ' ', ' ', 'O', 'X', 'X', ' ', 'O']

# Represents this board:
# X | O |
#   | O | X
# X |   | O
```

Remember that we can get the value of an element in a list by using its **index**, like this:

<pre class="dont-format-output"><code class="py">
board = ['X', 'O', ' ', ' ', 'O', 'X', 'X', ' ', 'O']

print('The board is a list with {} elements.'.format(len(board)))

# Look up the second element in the list by getting the element
# at index 1. Remember, the first item in the list has index 0!
second_element = board[1]
print('The second element in the list is {}.'.format(second_element))

last_element = board[8]
print('The last (ninth) element in the list is {}.'.format(last_element))
</code></pre>

Here's a visualization of where the indexes of the list end up in the printed board, in case that's helpful for you:

```python
# A nine-element list has these indexes:
[0, 1, 2, 3, 4, 5, 6, 7, 8]

# Those indexes represent these spots on the game board:
# 0 | 1 | 2
# 3 | 4 | 5
# 6 | 7 | 8
```

So, that's our board—we'll be using a list of nine strings, and those strings will either be `'X'`, `'O'`, or `' '`. The board will start off empty (all the strings will be `' '` initally ) and it will change over time as the player and computer make their moves.

# A Note On Grading

Throughout this assignment, I'll be telling you to write specific functions that behave a certain way. I'll tell you what the functions should be named; I'll tell you what inputs the functions should take; and I'll tell you what outputs the function should return.

It's **really important** that your functions have the **exact names** specified in the assignment. If I tell you to write a function named `make_pizza()`, but you write a function named `make_hamburger()` instead, my tests won't be able to find your function and so you won't pass the tests for this assignment. You want to pass the tests for this assignment, because that's how you get a good grade!

## Starter Code

Start by **downloading the [starter code][starter-code] for this project.**

The starter code defines five empty functions. **Your job is to fill in those empty functions using the instructions below**. When you're done, you'll have a working tic-tac-toe game!

Feel free to add more functions of your own if you want! Just be sure not to change the names of the functions provided in the starter code, because my automated tests will be looking for functions with those names.

OK, here's what each of those functions should do!

# Function: `make_board()`

<div class="function-spec">
<p class="function-name">Write a function called <code class="highlighter-rouge">make_board</code>.</p>

<p class="function-inputs">It should take <b>no inputs</b>.</p>

<p class="function-output">It should return as output <b>an empty tic-tac-toe board</b> like the one described above.</p>
</div>

When you call `make_board()`, it should return an empty tic-tac-toe board, which is a list that looks just like this:

```python
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
```

That's it for this one! This function is very simple, it's just a warm-up.

# Function: `print_board(board)`

<div class="function-spec">
<p>Write a function called <code class="highlighter-rouge">print_board</code>.</p>

<p>It should take as input <b>a tic-tac-toe board</b>.</p>

<p>It shouldn't return anything.</p>
</div>

This function should take a game board as input, and it should print that board out to the screen.

Here's what its output should look like when you pass it a fresh new empty board:

```
>>> print_board([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
  |   |
  |   |
  |   |
```

And here's what it should look like when you pass it the board that we saw earlier:

```
>>> print_board(['X', 'O', ' ', ' ', 'O', 'X', 'X', ' ', 'O'])
X | O |
  | O | X
X |   | O
```

You'll want to use several `print()` calls. Notice how each time you call `print()`, Python ends the current line of output and starts a new line. How many `print()` calls do you think you'll need in order to print out a 3x3 tic-tac-toe board? The answer isn't 9! :)

Remember that if e.g. I wanted to find the value of the third element in the list, I could do `board[2]` (assuming my board lived in a variable named `board`).

Remember that you can use the `+` sign to concatenate small strings together to make a bigger string.

**Hint:** When you're working on this function (and all the other ones in this assignment!), **try it out** as you work on it. Use the IDLE shell to call your function with a particular input (an empty board, a half-full board, a full board—you can write all of these boards by hand, they're just lists of nine strings!), and see how your function behaves when it's given that input. **This trick really, really helps**. You'll end up with working code much faster, and you'll have more fun doing it.

Next, let's think about how we'll handle the player's move.

# Function: `get_player_move(board)`

<div class="function-spec">
<p>Write a function called <code class="highlighter-rouge">get_player_move</code>.</p>

<p>It should take as input <b>a tic-tac-toe board</b>.</p>

<p>It should return as output <b>a number between <code class="highlighter-rouge">0</code> and <code class="highlighter-rouge">8</code></b>, indicating where the player wants to move.</p>
</div>

When you call `get_player_move(board)`, the function should ask the player where they'd like to make their next move (see the demo video from earlier for an example).

**If the player chooses a spot that's off the board or that isn't empty, tell them to try again!** You'll need to write code that notices that the player has made a mistake like this and figures out how to handle it!

**Note:** this function takes a game board as input. This function **should not modify that board** (e.g. the function shouldn't do something like `board[5] = 'X'`). I've written a test that checks for this.

(In general, functions shouldn't modify their inputs, and should instead just return an output. If a program has functions that modify their inputs, that program quickly becomes hard to understand and make changes to. When you're using a function, you want to just figure out what data it takes as input and what data it returns—you **don't** want to also have to ask questions like: "Will this function delete parts of the list I'm passing to it?".)

OK, now let's implement our AI opponent!

# Function: `get_computer_move(board, computer_team)`

<div class="function-spec">
<p>Write a function called <code class="highlighter-rouge">get_computer_move</code>.</p>

<p>It should take as input <b>a tic-tac-toe board</b> and <b>a string like <code class="highlighter-rouge">'X'</code> or <code class="highlighter-rouge">'O'</code> that indicates which team the computer is on</b>.</p>

<p>It should return as output <b>a number between <code class="highlighter-rouge">0</code> and <code class="highlighter-rouge">8</code></b>, indicating where the computer wants to move.</p>
</div>

This function should look at the board and choose an empty space where the computer should make its next move. The function should pay attention to the value of `computer_team` so it knows which team it's playing for!

This function should only choose an __empty__ space. If it chooses a space that already has an `'X'` or an `'O'` in it, then that's a bug, and my tests will find it.

**This function is your game's AI opponent!** Your goal here is to write some code that looks at the passed-in board, thinks really hard, and then picks the best possible space where the computer should make its next move.

Start by making a super-simple AI that picks the first empty space it finds on the board. Once you've got a completely working tic-tac-toe game, come back to this function and make it as crazy as you want. The goal is for this function to crush the human player (or at least force a tie)!

**Note**: Just like `get_player_move(board)`, this function **should not modify its input board**. This function's job is to take a board, look at it and figure out the space where the computer should move, and *return* that space. It should **not** change the board in the process.

**Hint:** A good trick is to check to see if the player's about to win on their next move. If that's the case, the computer should make a move on the spot the player needs so that the player isn't able to use it!

We're almost done with our program now—just one more function to go!

# Function: `check_for_winner(board)`

<div class="function-spec">
<p>Write a function called <code class="highlighter-rouge">check_for_winner</code>.</p>

<p>It should take as input <b>a tic-tac-toe board</b>.</p>

<p>It should return as output one of the following values:<b><code class="highlighter-rouge">'X'</code>, <code class="highlighter-rouge">'O'</code>, <code class="highlighter-rouge">'tie'</code>, or <code class="highlighter-rouge">'keep playing'</code></b>.</p>
</div>

This function's job is to take a board as input and return as output a value that indicates whether or not the game's over. If the function returns `'X'`, that means X wins; if the function returns `'O'`, that means O wins; if the function returns `'tie'`, that means the game's over and there's a tie; and if the function returns `'keep playing'`, that means that the game isn't over yet.

**Double-check to make sure that you're returning the right values**:
* if you return `'x'` instead of `'X'`, that's a bug.
* If you return `'keepplaying'` instead of `'keep playing'`, that's a bug.
* You get the idea!

There are eight possible ways to win at tic-tac-toe: there are three possible horizontal lines, three possible vertical lines, and two possible diagonal lines. Be sure to check for all of them! I'll be testing to make sure that you do!

Submitting your project
=======================

Submit a file called `tictactoe_<YOUR_NAME>.py`.

For instance, I'd submit a file called `tictactoe_jr_heard.py`.

On the first line of that file, write a comment with your name on it, like this:

```
# JR Heard
```

Remember to follow this class's [style guide](https://docs.google.com/document/d/1UbyhIkxOdhpf-MGna_5dwh0yHXe02HTZ69CfEuYv76Y/edit).


[starter-code]: {{site.baseurl}}/python/tictactoe_starter_code.py



<script src="{{ site.baseurl }}/assets/js/codemirror.js"></script>
<script src="{{ site.baseurl }}/assets/js/codemirror_python.js"></script>
<script src="{{ site.baseurl }}/assets/js/codemirror_runmode.js"></script>
<script>
var textAreas = document.getElementsByTagName("textarea");
var pres = document.querySelectorAll("pre.cm-s-friendship-bracelet");

for (var i = 0; i < textAreas.length; i++) {
	CodeMirror.runMode(textAreas[i].value, "python", pres[i]);
}
</script>


<script>
window.klipse_settings = {
	selector_eval_python_client: '.py',
	codemirror_options_in: {
		theme: "friendship-bracelet"
	},
	codemirror_options_out: {
		theme: "friendship-bracelet"
	}
};
</script>
<script src="{{ site.baseurl }}/assets/js/asciinema-player.js"></script>
<script src="{{ site.baseurl }}/assets/js/klipse.min.js"></script>
