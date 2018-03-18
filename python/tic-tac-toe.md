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

Like in the demo video above, your program should start by asking the player if they want to be `X` or `O`, and then it should flip a coin to decide who goes first. You can figure this stuff out by now, I won't explain it—if you have trouble figuring out how to randomly choose who goes first, try Googling around until you find an answer!

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
</code></pre>

So, that's our board—we'll be using a 2D list of strings, and those strings will either be `'X'`, `'O'`, or `' '`. The board will start off empty (all the strings will be `' '` initally ) and it will change over time as the player and computer make their moves.

# A Note On Grading

Throughout this assignment, I'll be telling you to write specific functions that behave a certain way. I'll tell you what the functions should be named; I'll tell you what inputs the functions should take; and I'll tell you what outputs the function should return.

That's because now that you're writing functions, I'll be able to test them directly. Just like you might, say, import the `random` module and call the `random.choice()` function in order to decide who goes first, I'll be importing the `tictactoe_your_name` module from your program, and in my automated tests I'll be calling `tictactoe_your_name.a_function()` in order to make sure each one of your functions works the way it's supposed to.

What this means is that it's really important that your functions have the **exact names** specified in the assignment. If I tell you to write a function named `make_pizza()`, but you write a function named `make_hamburger()` instead, my tests won't be able to find your function and so you won't pass the tests for this assignment.

That might sound restrictive and lame, but there's some good news: now that my tests can use your functions directly, your program's __output__ can look however you want! You don't have to use the exact same text from the demo videos any more, your program can be as weird and creative as you like. Enjoy!

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

That's it for this one! Next, let's think about how we'll handle the player's move.

# Function: `get_player_move()`

<div class="function-spec">
<p>Write a function called <code class="highlighter-rouge">get_player_move</code>.</p>

<p>It should take <b>no inputs</b>.</p>

<p>It should return as output <b>a two-item list like <code class="highlighter-rouge">[0, 2]</code></b>.</p>
</div>

When you call `get_player_move()`, the function should ask the player where they'd like to make their next move (see the demo video from earlier for an example).

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

**This function is your game's AI opponent!** If you want to have a really smart AI that totally destroys the human player at tic-tac-toe, then this function is where that code should go.

**Note:** this function takes a game board (represented by a 2D list) as input. This function **should not modify that board** (e.g. the function shouldn't do something like `input_board[1][2] = 'X'`). I've written a test that checks for this.

In general, functions shouldn't modify their inputs. If a program has fucntions that modify their inputs, that quickly becomes hard to understand and make changes to. When you're using a function, you want to just figure out what data it takes as input and what data it returns—you **don't** want to also have to ask questions like: "Will this function mangle the list I'm passing it as input?"



[blackjack]: {{site.baseurl}}/python/blackjack


outline

* checking for wins
* checking for ties
* mention crayons library
* when i write tests, look in this file for any usage oft he word 'test' to make sure that i actually implement the tests i promise to







Nitty Gritty
============

If the user inputs an invalid mode (i.e. something that's not "encrypt" or "decrypt"), it's fine if your program crashes.

If the user inputs an invalid key (i.e. something that's not a number between 0 and 26), it's fine if your program crashes.

Submitting your project
=======================

Submit a file called `tictactoe_<YOUR_NAME>.py`.

For instance, I'd submit a file called `tictactoe_jr_heard.py`.

On the first line of that file, write a comment with your name on it, like this:

```
# JR Heard
```

Remember to follow this class's [style guide](https://docs.google.com/document/d/1UbyhIkxOdhpf-MGna_5dwh0yHXe02HTZ69CfEuYv76Y/edit).

Other Features
==========

Here are some more features to add to your program once you get basic encryption and decryption working. Do any or all of them!

Lowercase Letters
-----------------

Make your program work with uppercase _and_ lowercase characters, like this:

<asciinema-player src="{{ site.baseurl }}/caesar_upper_and_lower_cast.json" rows="19" cols="80" autoplay="true" loop="true"></asciinema-player>

When I did this, I ended up switching away from `ord()` and `chr()`, and instead made a string like `transformable_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'` and had my code do stuff based on the position of each letter of the message in my `transformable_characters` string. Here's how you can find the first position of a letter in a string in Python:

<pre><code class="py">
# 'l' is in 'Hello', so this evaluates to number 2.
print('Hello'.find('l'))

# 'z' isn't in 'Hello', so this evalutes to -1, which is
# Python's way of saying: I looked for this but couldn't find it!
print('Hello'.find('z'))
</code></pre>

Brute Force
-----------

Add a "brute force" mode that lets you try to decrypt a message even if you don't know the right key for it - notice the correct translation on Line 5:

<asciinema-player src="{{ site.baseurl }}/caesar_brute_cast.json" rows="30" cols="80" autoplay="true" loop="true"></asciinema-player>

This can be done using nested for loops or functions (we haven't officially covered functions in class yet, but you are welcome to use them if you know how).

Smart Brute Force
-----------------

This is my favorite one: enhance your program's "brute force" mode so that it can _automatically detect_ the correct key:

<asciinema-player src="{{ site.baseurl }}/caesar_brute_smart_cast.json" rows="15" cols="80" autoplay="true" loop="true"></asciinema-player>

You can do this however you want. Be creative! My solution involved using [this text file](https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co), which is a list of all of the English words in the 1934 edition of Webster's Second International Dictionary.

Since internet use will be limited for the final project, if you don't know how to work with text files you will probably want to stick with the other features for today. You can also come back and add smart brute force another day if it seems intriguing.

If you'd like to figure out how to open a text file in Python and get all the lines out of it, Google around until you find a solution - you can always ask me for help if you get stuck, but I think you'd be surprised how far you can get by just Googling stuff!


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
