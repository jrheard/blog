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

At this point I'd like you to think back to the [blackjack][blackjack] assignment. In that project, we talked about _representing_ stuff. We wanted to teach our computer program about the concept of a playing card like "the five of diamonds", and we ended up using a two-item list like `[5, 'diamonds']` to do that. You'll also remember that in order to represent a deck of cards, we made a list that had a bunch of items in it, and each of _those_ items was a two-item list like `['4', 'hearts']` that represented a card.

In _this_ project, we now have to figure out: how do we represent the concept of the game board? Think about it for a second before you scroll down. How would you represent a 3x3 tic-tac-toe board in a Python program?

<p class="lots-of-space"> Seriously, think about it!</p>

<p class="lots-of-space">OK, here's what I recommend doing. Is it the same as what you were thinking?</p>

I think we should use a two-dimensional list of strings. It'll look like this:

```python
[['X', ' ', 'X'],
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

## A Quick Note

Throughout this assignment, I'll be telling you to write specific functions that behave a certain way. I'll tell you what the functions should be named; I'll tell you what inputs the functions should take; and I'll tell you what outputs the function should return.

That's because now that you're writing functions, I'll be able to test them directly. Just like you might, say, import the `random` module and call the `random.choice()` function in order to decide who goes first, I'll be importing the `tic_tac_toe_your_name` module, and in my automated tests I'll be calling `tic_tac_toe_your_name.a_function()` in order to make sure each one of your functions works the way it's supposed to.

What this means is that it's really important that your functions have the **exact names** specified in the assignment. If I tell you to write a function named `make_pizza()`, but you write a function named `make_hamburger()` instead, my tests won't be able to find your function and so you won't pass the tests for this assignment.

That might sound restrictive and lame, and maybe it is. But there's some good news: now that my tests can use your functions directly, your program's __output__ can look however you want! You don't have to use the exact same text from the demo videos any more, your program can be as weird and whimsical as you like. Enjoy!

Now that that's out of the way, let's write some functions.

# Function: `make_board()`

Write a function called `make_board()`. It should take no inputs. It should return as output an empty 3x3 tic-tac-toe board like the one described above.

When you call `make_board()`, it should return a list that looks just like this:

```python
[[' ', ' ', ' '],
 [' ', ' ', ' '],
 [' ', ' ', ' '],
```



[blackjack]: {{site.baseurl}}/python/blackjack


outline

* representing the board as a 2d list
* function to make a new board
* player's move
* computer's move
* checking for wins
* checking for ties
* somewhere: credit al
* somewhere: explain that we'll be testing their functions, and spec out each function's API; maybe do this at each step of the way i guess






<div class="message update">
<p>All of the words and pictures between this yellow box and the next yellow box have been copy-pasted directly from Al Sweigart's excellent book "Invent Your Own Computer Games With Python". I've made a few very minor edits.</p>

<p>This is OK because Al has graciously made his book available under a <a href="https://creativecommons.org/licenses/by-nc-sa/3.0/us/">Creative Commons license</a>. Thanks, Al!</p>
</div>

Encryption
==========

The science of writing secret codes is called **cryptography**. For thousands of years cryptography has made secret messages that only the sender and recipient could read, even if someone captured the messenger and read the coded message. A secret code system is called a **cipher**. The cipher used by the program you're about to build is called the Caesar cipher.

In cryptography, we call the message that we want to be secret the **plaintext**. The plaintext could look like this:

`HELLO THERE! THE KEYS TO THE HOUSE ARE HIDDEN UNDER THE FLOWER POT.`

Converting the plaintext into the encoded message is called **encrypting** the plaintext. The plaintext is encrypted into the **ciphertext**. The ciphertext looks like random letters, and we cannot understand what the original plaintext was just by looking at the ciphertext. Here is the previous example encrypted into ciphertext:

`YVCCF KYVIV! KYV BVPJ KF KYV YFLJV RIV YZUUVE LEUVI KYV WCFNVI GFK.`

But if you know about the cipher used to encrypt the message, you can **decrypt** the ciphertext back to the plaintext. (Decryption is the opposite of encryption.)

Many ciphers also use keys. **Keys** are secret values that let you decrypt ciphertext that was encrypted using a specific cipher. Think of the cipher as being like a door lock. You can only unlock it with a particular key.

The Caesar Cipher
=================

The key for the Caesar Cipher will be a number from 1 to 26. Unless you know the key (that is, know the number used to encrypt the message), you won’t be able to decrypt the secret code.

The Caesar Cipher was one of the earliest ciphers ever invented. In this cipher, you encrypt a message by taking each letter in the message (in cryptography, these letters are called symbols because they can be letters, numbers, or any other sign) and replacing it with a “shifted” letter. If you shift the letter A by one space, you get the letter B. If you shift the letter A by two spaces, you get the letter C.

Here's a picture of some letters shifted over by three spaces:

{% img caesar_1.jpg %}

To get each shifted letter, draw out a row of boxes with each letter of the alphabet. Then draw a second row of boxes under it, but start a certain number (this number is the key) of spaces over. After the letters at the end, **wrap around** back to the start of the boxes.

Here's an example with the letters shifted by three spaces:

{% img caesar_2.png %}

**The number of spaces you shift is the key in the Caesar Cipher**. The example above shows the letter translations for the key 3.

If you encrypt the plaintext `“HOWDY”` with a key of 3, then:

* The “H” becomes “K”.
* The letter “O” becomes “R”.
* The letter “W” becomes “Z”.
* The letter “D” becomes “G”.
* The letter “Y” becomes “B”.

The ciphertext of `“HOWDY”` with key 3 becomes `“KRZGB”`.

We will keep any non-letter characters the same. To decrypt `“KRZGB”` with the key 3, we go from the bottom boxes back to the top:

* The letter “K” becomes “H”.
* The letter “R” becomes “O”.
* The letter “Z” becomes “W”.
* The letter “G” becomes “D”.
* The letter “B” becomes “Y”.

ASCII, and Using Numbers for Letters
====================================

How do we implement this shifting of the letters as code? We can do this by representing each letter as a number called an **ordinal**, and then adding or subtracting from this number to form a new ordinal (and a new letter). ASCII (pronounced “ask-ee” and stands for American Standard Code for Information Interchange) is a code that **connects each character to a number between 32 and 126**.

The capital letters “A” through “Z” have the ASCII numbers **65 through 90**. The lowercase letters “a” through “z” have the ASCII numbers **97 through 122**. The numeric digits “0” through “9” have the ASCII numbers **48 through 57**.

So if you wanted to shift “A” by three spaces, you would do the following:

* Convert “A” to an ordinal (65).
* Add 3 to 65, to get 68.
* Convert the ordinal 68 back to a letter (“D”).

<div class="message update">
<p>That's the end of the copy-pasted section of Al's book. Everything after this box was written by JR like usual.</p>
</div>

Letters A-Z Don't Have ASCII Codes 1-26
===========================================

This might feel weird at first, but you'll get used to it. Most of the ASCII codes between 0 and 31 are junk left over from the days when computers were giant room-sized machines controlled by jury-rigged typewriters.

Here's the full ASCII table from [asciitable.com](http://www.asciitable.com) - don't worry, you don't need to memorize this or anything, I'm just showing it to you in case you find it helpful. I've highlighted the section of the table that concerns the uppercase letters A-Z. You only care about the "Dec" (decimal) and "Char" (character) columns in this table.

{% img ascii_table.jpg %}

That's the whole thing! Notice how e.g. uppercase `J` has the ASCII code 74, and lowercase `j` has the ASCII code 106.

Converting between letters and numbers
======================================

Python comes with the `ord()` function, which lets you convert a letter to its corresponding ordinal number:

<pre><code class="py">
print(ord('J'))
</code></pre>

To go from an ordinal number back to a letter, you can use the `chr()` function.

<pre><code class="py">
print(chr(74))
</code></pre>

Let's try shifting the letter `H` over by 3, like we did in the `"Howdy"` example above:

<pre><code class="py">
print(chr(ord('H') + 3))
</code></pre>
It turns into `K`, just like we expected! `ord()` and `chr()` are going to be your best friends while you're working on this project.

String Manipulation Tip
=======================

You'll probably want to use a `for` loop at some point in your program - here's how you can use a `for` loop to do _something_ to each letter of a string:

<pre><code class="py">
some_letters = "ABCDEFG"
lowercased_letters = ""

for letter in some_letters:
	lowercased_letters = lowercased_letters + chr(ord(letter) + 32)

print(lowercased_letters)
</code></pre>

That chunk of code lowercases a string, one letter at a time - you might end up doing something similar (but **different!**) when you're building up your program's `ciphertext` variable.

Your Program Should Only Change Uppercase Letters
=====================

If your program is given some plaintext that includes numbers, or lowercase letters, or punctuation marks like `!` or `.` or `$` or _anything_ that's not a letter from `A` to `Z`, **it should leave that character unmodified**. For example, if given a plaintext string of `HOWDY! Hello.` and a key of `5`, your program should output the ciphertext `MTBID! Mello.`

Note that in that message, the `W` ends up "wrapping around" to become a `B` when it's encrypted.

Demo
====

Your program should allow the user to both encrypt messages **and** decrypt them. Your program should look **exactly** like this when it's run:

<asciinema-player src="{{ site.baseurl }}/caesar_cast_1.json" rows="19" cols="80" autoplay="true" loop="true"></asciinema-player>

Nitty Gritty
============

If the user inputs an invalid mode (i.e. something that's not "encrypt" or "decrypt"), it's fine if your program crashes.

If the user inputs an invalid key (i.e. something that's not a number between 0 and 26), it's fine if your program crashes.

Submitting your project
=======================

Submit a file called `caesar.py`.

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
