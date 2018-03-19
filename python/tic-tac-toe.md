---
layout: page
title:  "Madison CS 3-4: Tic-Tac-Toe"
---

In this project, you'll write a program that lets you play a game of tic-tac-toe against a computer opponent.

The goal of this project is to get you comfortable with writing **functions**.

Functions are like LEGO blocks.

{% img lego.jpg %}

A LEGO block is a small, simple thing—but if you put a bunch of those simple blocks together in the right way, you can make the Milennium Falcon, or the Eiffel Tower, or a goofy-looking dog.

Functions are just like that. The functions you write should each be small, simple, and easy to understand—but if you put a bunch of your functions together in the right way, you can make a website, or control a robot, or fly a spaceship.

The best part about functions is that they're even better than LEGO blocks, because you can make your own! When you buy a LEGO set, you're stuck with whatever kinds of blocks come with the set; when you use a programming language, you can use its built-in functions to make _your own_ way cooler functions that do whatever you want, and then you can put _those_ functions together to make a program that does something awesome. Functions are basically my favorite thing about programming.

Let's write some simple functions and put them together to make a tic-tac-toe game!

## Demo

The game we're making will look like this:

<asciinema-player src="{{ site.baseurl }}/tictactoe_cast.json" rows="25" cols="85" autoplay="true" loop="true"></asciinema-player>

(The idea for this project was taken from Al Sweigart's excellent book "Invent Your Own Computer Games With Python".)

## First Steps

Like in the demo video above, your program should start by asking the player if they want to be `X` or `O`, and then it should flip a coin to decide who goes first. You can figure this stuff out on your own, I won't explain it—if you have trouble figuring out how to randomly choose who goes first, try Googling around until you find an answer!

## Representing The Board

A game of tic-tac-toe takes place on a 3x3 board. A space on the board is either empty, or it has an X in it, or it has an O in it.

At this point I'd like you to think back to the [blackjack][blackjack] assignment. In that project, we talked about _representing_ stuff. We wanted to teach our computer program about the concept of a playing card like "the five of diamonds", and we ended up using a two-item list like `[5, 'diamonds']` to do that. You'll also remember that in order to represent a deck of cards, we made a list that had a bunch of items in it, and each of _those_ items was a two-item list like `['4', 'hearts']`.

In _this_ project, we now have to figure out: how do we represent the concept of a tic-tac-toe game board? Think about it for a second before you scroll down.

<p class="lots-of-space">How would you represent a 3x3 tic-tac-toe board in a Python program?</p>

<p class="lots-of-space">Seriously, think about it!</p>

<p class="lots-of-space">OK, here's what I recommend doing. Is it the same as what you were thinking?</p>

I think we should use a list of lists of strings (also called a "two-dimensional list of strings", or a "2D list of strings"). It'll look like this:

```python
[['X', ' ', 'O'],
 ['O', 'O', ' '],
 ['X', 'O', 'X']]
```

Let's play around with this list to make sure that we completely understand it.

<pre class="dont-format-output"><code class="py">
board = [['X', ' ', 'O'],
		 ['O', ' ', 'O'],
		 ['X', 'O', 'X']]

print('The board is a list with {0} elements.'.format(len(board)))
print('Each of those elements is a list.')

second_element = board[1]

print('The second element in the board is {0}'.format(repr(second_element)))
print("That's a list with three strings in it.")
print('The last string in that list is {0}.'.format(second_element[2]))
print("Here's the same string: {0}.".format(board[1][2]))
</code></pre>

So, that's our board—we'll be using a 2D list of strings, and those strings will either be `'X'`, `'O'`, or `' '`. The board will start off empty (all the strings will be `' '` initally ) and it will change over time as the player and computer make their moves.

# A Note On Grading

Throughout this assignment, I'll be telling you to write specific functions that behave a certain way. I'll tell you what the functions should be named; I'll tell you what inputs the functions should take; and I'll tell you what outputs the function should return.

That's because now that you're writing functions, I'll be able to test them directly. Just like you might, say, import Python's built-in `random` module and call the `random.choice()` function in order to decide who goes first, I'll be importing the `tictactoe_your_name` module from your program, and in my automated tests I'll be writing code like `tictactoe_your_name.a_function()` in order to make sure each one of your functions works the way it's supposed to.

What this means is that it's really important that your functions have the **exact names** specified in the assignment. If I tell you to write a function named `make_pizza()`, but you write a function named `make_hamburger()` instead, my tests won't be able to find your function and so you won't pass the tests for this assignment.

That might sound restrictive and lame, but there's some good news: now that my tests can use your functions directly, the stuff your program __prints out__ can look __however you want__! You don't have to use the exact same text from the demo videos any more, your program can be as weird and creative as you like. Enjoy!

OK, let's write some functions!

# Function: `make_board()`

<div class="function-spec">
<p class="function-name">Write a function called <code class="highlighter-rouge">make_board</code>.</p>

<p class="function-inputs">It should take <b>no inputs</b>.</p>

<p class="function-output">It should return as output <b>an empty 3x3 tic-tac-toe board</b> like the one described above.</p>
</div>

When you call `make_board()`, it should return a list that looks just like this:

```python
[[' ', ' ', ' '],
 [' ', ' ', ' '],
 [' ', ' ', ' ']]
```

That's it for this one!

# Function: `print_board(board)`

<div class="function-spec">
<p>Write a function called <code class="highlighter-rouge">print_board</code>.</p>

<p>It should take as input <b>a game board, represented by a 2D list of strings</b>.</p>

<p>It should return as output <b><code class="highlighter-rouge">None</code></b>, which is a special value that we haven't really talked about yet.</p>

<p>In Python, a function will return <code class="highlighter-rouge">None</code> by default if the function doesn't have a <code class="highlighter-rouge">return</code> statement in it, so you don't really need to worry about this—just don't put a <code class="highlighter-rouge">return</code> statement in your function and you're all set.</p>
</div>

This function should take a game board as input, and it should print that board out to the screen. Don't just do `print(board)`—make it look nice!

You'll want to use a nested `for` loop for this (one `for` loop inside another `for` loop). You'll probably be doing `range(len(SOMETHING))` once or twice, too.

Check out the demo video from earlier if you'd like an example of what your board might look like when it's printed out. I didn't make my board look particularly good, so try to make yours better-looking than mine!

I used colors in my printed-out board, but you don't have to. If you're interested in using colors, my advice is to start simple and then add colors later. When you finish the no-colors version of this function, there's a note at the end of this assignment that'll tell you how to add colors if you want.

Next, let's think about how we'll handle the player's move.

# Function: `get_player_move()`

<div class="function-spec">
<p>Write a function called <code class="highlighter-rouge">get_player_move</code>.</p>

<p>It should take <b>no inputs</b>.</p>

<p>It should return as output <b>a two-item list like <code class="highlighter-rouge">[0, 2]</code></b>.</p>
</div>

When you call `get_player_move()`, the function should ask the player where they'd like to make their next move (see the demo video from earlier for an example).

If the player chooses a spot that's off the board or isn't empty, tell them to try again.

When you prompt the player for their move, you should let them put in a number betwen `1` and `3` for their move's X position, and another number between `1` and `3` for their move's Y position. You should then convert those X/Y coordinates so that they're between `0` and `2` instead of being between `1` and `3`. Here's why you need to convert those numbers:

<pre class="dont-format-output"><code class="py">
board = [['X', ' ', 'O'],
		 ['O', ' ', 'O'],
		 ['X', 'O', 'X']]

print(board[0][0])

# This line crashes!
print(board[1][3])
</code></pre>

Our board is a 3x3 grid. If you try to do `a_three_by_three_grid[1][3]`, Python crashes, because you've asked for the fourth item in the second list, and the second list only has three items. Does that make sense? If not, reread the past few paragraphs one more time, you'll get it.

2D lists take a little getting used to, but really they're just like regular lists.

Anyway, what I'm getting at here is that if your `get_player_move()` function asks a user for their move's X/Y coordinates and the user enters `1` and `3`, then your function should return `[0, 2]`. If it returns `[1, 3]` in that situation, then that's a **bug**, and I'll find it! :)

OK, now let's implement our AI opponent!

# Function: `get_computer_move(board)`

<div class="function-spec">
<p>Write a function called <code class="highlighter-rouge">get_computer_move</code>.</p>

<p>It should take as input <b>a game board, represented by a 2D list of strings</b>.</p>

<p>It should return as output <b>a two-item list like <code class="highlighter-rouge">[0, 2]</code></b>.</p>
</div>

This function should look at the board and choose an empty space where the computer should make its next move.

This function should only choose an __empty__ space. If it chooses a space that already has an `'X'` or an `'O'` in it, then that's a bug.

**This function is your game's AI opponent!** Your goal here is to write some code that looks at the passed-in board, thinks really hard, and then picks the best possible space where the computer should make its next move. Make this as crazy as you want—the goal is for this function to crush the human player (or at least force a tie)!

Hint: you don't have to do this, but a good trick is to check to see if the player's about to win on their next move. If that's the case, the computer should make a move on the spot the player needs so that the player isn't able to use it!

**Note:** this function takes a game board as input. This function **should not modify that board** (e.g. the function shouldn't do something like `input_board[1][2] = 'X'`). I've written a test that checks for this.

In general, functions shouldn't modify their inputs. If a program has functions that modify their inputs, that program quickly becomes hard to understand and make changes to. When you're using a function, you want to just figure out what data it takes as input and what data it returns—you **don't** want to also have to ask questions like: "Will this function mangle the list I'm passing to it?"

We're almost done with our program now—just one more function to go!

# Function: `check_for_winner(board)`

<div class="function-spec">
<p>Write a function called <code class="highlighter-rouge">check_for_winner</code>.</p>

<p>It should take as input <b>a game board, represented by a 2D list of strings</b>.</p>

<p>It should return as output one of the following values:<b><code class="highlighter-rouge">'X'</code>, <code class="highlighter-rouge">'O'</code>, <code class="highlighter-rouge">'tie'</code>, or <code class="highlighter-rouge">False</code></b>.</p>
</div>

This function's job is to take a board as input and return as output a value that indicates whether or not the game's over. If the function returns `'X'`, that means X wins; if the function returns `'O'`, that means O wins; if the function returns `'tie'`, that means the game's over and there's a tie; and if the function returns `False`, that means that the game isn't over yet.

There are eight possible ways to win at tic-tac-toe: there are three possible horizontal lines, three possible vertical lines, and two possible diagonal lines. Be sure to check for all of them!

(A note for advanced students: this function returns one of three special strings or `False`. That's just kind of clunky. It'd be much better if our program defined an [Enum](https://docs.python.org/3/library/enum.html#creating-an-enum) with a name like `WinStatus`; then we could have this function return something like `WinStatus.NO_WINNER_YET`, `WinStatus.X`, `WinStatus.O`, or `WinStatus.TIE`. We're not covering `Enum`s in this class, though, so for now let's just live with the fact that this function has a weird return value.)

# Now Glue Them All Together

At this point you've got all of the basic functions you need:

* `make_board()`
* `print_board(board)`
* `get_player_move()`
* `get_computer_move(board)`
* `check_for_winner(board)`

All you need to do is write some code that _uses_ these functions in order to play the game. You can do it!

If you have trouble getting started, look back at the code from your Blackjack project—this project will have a lot of similar features (`input()` calls, a `while True:` loop, etc). The only difference is that some of your code lives in functions this time, and the rest of your code will need to call those functions and use the values that they return.

Remember to ask the player if they'd like to play as Xs or Os. Remember to flip a coin to see who goes first.

If you'd like to add cool features like keeping score and allowing the player to play multiple games without re-running the program, go right ahead! Feel free to write more functions, too!

# One More Thing You Need To Do Before You Turn Your Project In

In order for me to be able to import your functions and test them, I need you to do something in your program that's going to seem kind of weird.

I need your program to look like this:

<textarea class="hidden">
import random

def make_board():
	# TODO: write this

def print_board(board):
	# TODO: write this

def get_player_move():
	# TODO: write this

def get_computer_move(board):
	# TODO: write this

def check_for_winner(board):
	# TODO: write this

# THIS LINE IS THE IMPORTANT ONE
if __name__ == '__main__':

	print('Welcome to Tic-Tac-Toe!')
	team = input('Do you want to be X or O? ')

	# code for the rest of the game goes here
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

Your program should define a bunch of functions, and then it should have an `if` statement _exactly_ like the one you see in the code snippet above. The rest of your program's code should go inside that `if` statement.

If you'd like to learn about _why_ I need you to do this, [this StackOverflow answer](https://stackoverflow.com/questions/419163/what-does-if-name-main-do) is pretty good. The short version is that this `if` statement is what allows me to do `import tictactoe_your_name` in my automated tests.

This `if` statement is super important, and **if you don't include it then your program won't be able to pass any of the assignment's tests**—so be sure to include it! It's easy, you can copy-paste it into your program. Remember: after your imports and function definititions (those should be _outside_ the `if` statement like they are in the example code above), _everything_ else in your program should go inside of this `if` statement.



[blackjack]: {{site.baseurl}}/python/blackjack

# One Last Note: Colors

The tic-tac-toe program from my demo video had colorful `X`s and `O`s. If you'd like to do this in your program too, then check out the [crayons](https://github.com/kennethreitz/crayons) library; you can install it by running `pip install --user crayons` at the command line.

The colors won't work in IDLE, so you'll need to run your program from the command line if you use the `crayons` library. Let me know if you'd like help figuring out how to do that.

Submitting your project
=======================

Submit a file called `tictactoe_<YOUR_NAME>.py`.

For instance, I'd submit a file called `tictactoe_jr_heard.py`.

On the first line of that file, write a comment with your name on it, like this:

```
# JR Heard
```

Remember to follow this class's [style guide](https://docs.google.com/document/d/1UbyhIkxOdhpf-MGna_5dwh0yHXe02HTZ69CfEuYv76Y/edit).



{% javascript codemirror %}
{% javascript codemirror_python %}
{% javascript codemirror_runmode %}
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
{% javascript asciinema-player %}
{% javascript klipse.min %}
