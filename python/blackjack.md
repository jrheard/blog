---
layout: page
title:  "Madison CS 3-4: Blackjack"
---

<style>
.cm-s-friendship-bracelet {
	font-size: 16px;
}
</style>

In this project, you'll write a Python program that lets a user play Blackjack.

**You will be using starter code for this project! Download [this file][starter-code] and use it as the basis for your program.**

How It's Played
===============

Blackjack is a card game. We'll be making a simple version of it. In our version, there's a **player** (controlled by a human) and a **dealer** (a computer-controlled opponent).

The player starts with two cards, and can choose to draw more cards ("hit") or to end their turn ("stand"). Once the player is done drawing cards, it's the **dealer**'s turn. Once the dealer's turn is over, the game tells the player whether they won or lost.

A card has a **suit** (a string like `'spades'` or `'diamonds'`), and a **value** (a number between `1` and `10`). Each player has a **count**, which is the sum of all of their cards' values. If I have a five of diamonds, a three of hearts, and a ten of spades, my count is 18.

The goal of the game is to **beat the dealer by getting a count as close to 21 as possible without going over 21**[^1].

I'll go into a lot more detail about all this later on. First, though, let's figure out how to write a Python program that has playing cards in it.

[^1]: [How to play: Blackjack](https://www.bicyclecards.com/how-to-play/blackjack/)

How to Program a Card Game
==========================

Representing a Card
-------------------

Here's what a five of diamonds looks like in real life:

{% img five_of_diamonds.png width:295px height:400px %}

Here's what a five of diamonds looks like in a Python program:

<textarea class="hidden">
[5, "diamonds"]
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

That's a two-item list that **represents** a five of diamonds card.

"Representing" something means "getting it out of your head and into a computer program." In this example, I took the concept of \<a five of diamonds card\> and turned it into \<a list with two things in it; the first thing is a number that represents the card's value, and the second thing is a string that represents the card's suit\>. This is important because Python doesn't really know what you mean when you say "a five of diamonds card", but it *does* understand `[5, "diamonds"]`.

There are a lot of different ways to represent a five of diamonds in a Python program. If you know how to use dicts, classes, or tuples, feel free to use any of those instead. If you don't know what those are yet, don't worry: a two-item list is just as good as those other things. All that matters is that you choose *some* way of representing playing cards in your Python program. A two-item list of `[value, suit]` works great.

Representing a Deck
-------------------

That's just one card, though, and there are fifty-two cards in a deck.

A deck of cards has four **suits**: `diamonds`, `hearts`, `spades`, and `clubs`.

Each suit has thirteen cards:

* an ace,
* the cards 2 through 10,
* and a jack, a queen, and a king.

Jacks, queens, and kings have the value 10. In the simple version of Blackjack that you're building in this project, aces always have the value 1.

Here's a full suit of diamonds:

<pre class="dont-format-output"><code class="py">
diamonds = [
	# The ace has value 1.
	[1, "diamonds"],
	[2, "diamonds"],
	[3, "diamonds"],
	[4, "diamonds"],
	[5, "diamonds"],
	[6, "diamonds"],
	[7, "diamonds"],
	[8, "diamonds"],
	[9, "diamonds"],
	[10, "diamonds"],
	# The jack, queen, and king
	# all have value 10.
	[10, "diamonds"],
	[10, "diamonds"],
	[10, "diamonds"],
]

print("There are " + str(len(diamonds)) + " cards in this suit.")
print("The sixth card's value is " + str(diamonds[5][0]) + ".")
print("The twelfth card's value is " + str(diamonds[11][0]) + ".")
</code></pre>

Notice that `diamonds` is a list of **cards**, and a **card** is a list like `[5, "diamonds"]` - so `diamonds` is a list of lists. It's totally fine and normal for lists to contain other lists, you'll do this a lot in future projects.

Your program's deck should be a list with fifty-two elements: thirteen cards for each of the four suits.

Shuffling the Deck
-------------
Once you've got a deck of cards, you should shuffle the deck. Here's how you can randomize the order of the items in a list:

<pre><code class="py">
import random

my_favorite_foods = ["Fried Rice", "Red Curry", "Pizza", "Sandwiches"]

# This line is the important one!
random.shuffle(my_favorite_foods)

print(my_favorite_foods)
</code></pre>

Dealing Hands
-------------

Now that your deck's shuffled, you should give two cards to the player and two cards to the dealer. The player and dealer should each have a **hand**, which is a list of cards.

Here's an example of what a hand might look like:

<textarea class="hidden">
[[10, "spades"], [5, "clubs"]]
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

Make sure that whenever you deal a card to someone, that card is removed from the deck. There should only ever be fifty-two cards at a time throughout your program—if the player has two cards and the dealer has two cards, then the deck should have forty-eight cards.

Milestone 1: Displaying Output
==============================

You've done a lot of good stuff so far!

The [starter code][starter-code] for this project contains a function called `print_game_status()`. Add a line to your program that uses this function.

At this point, your program should look exactly like this when it's run:

<asciinema-player src="{{ site.baseurl }}/blackjack_cast_milestone_1.json" rows="13" cols="90" autoplay="true" loop="true"></asciinema-player>

The cards and counts your program prints out will be different every time the program is run, so it's fine that they'll be different from what you see in my demo above.

Player's Turn
=============

Once the cards have been dealt, it's the player's turn. In our simple version of Blackjack, the player has two options:

1. The player can draw another card by saying `"hit"`. They can do this as many times as they want, as long as their **count** is below 21.
1. The player can end their turn by saying `"stand"`.

Your program should prompt the user for input over and over until they say `"stand"`, at which point their turn is over. You'll want to use a `while` loop to do this. Here's some starter code that you might find useful:

<textarea class="hidden">
while True:
	move = input("Do you want to 'hit' or 'stand'? ")

	if move == 'hit':
		# TODO: Remove a card from the deck,
		# add it to the player's hand,
		# and update their count.

		# TODO: Once you've done that, print out
		# the current state of the game so that
		# the player can see their new hand and count.

		# TODO: If the player's count is
		# greater than 21, _end the game_
		# and tell the player that they lost.

		# Print out the new state of the game.
		print_game_status(player_hand, player_count, dealer_hand, dealer_count, deck)

	if move == 'stand':
		break
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

Each time the player says `"hit"`, you should call `print_game_status()` after giving them a new card, so that they can see their updated hand.

Notice the TODO that says that you should end the game if the player's count exceeds 21. That's called "busting", and it's game over for the player - don't forget to implement it in your program!

Dealer's Turn
=============

Once the player has said `"stand"`, it's time for the dealer's turn.

Here's what should happen during the dealer's turn:

* If the dealer's count is less than **17**, the dealer should draw cards until its count is **17 or higher**.
* If at any point dealer's count is 17 or higher, the dealer's turn immediately ends.
* If the dealer's count goes over 21, the dealer busts and the player wins.

Once the dealer's turn is over, you should call `print_game_status()` so that the player can see what happened. You should only call it a single time at the end of the dealer's turn, you don't need to call it every time the dealer draws a card.

**Note**: If the player busted during their turn, the game should end immediately and you should **skip the dealer's turn**.

Check Counts
============

Once the dealer's turn is over, compare the player's count to the dealer's count. If the player's count is *higher* than the dealer's count, the player wins. If the player's count is *lower* than the dealer's count, the player loses. If the two counts are *equal*, it's a tie!

The last line of your program's output should be something like `You won!` or `It's a tie!`. The [starter code][starter-code] for this project has the specific strings that you should use - be sure to use them, because we'll be running an automated test program that'll be looking for them!

**Note**: If the player busted during their turn, you should skip the dealer's turn _as well as_ this count-checking phase. If the player busted, they lost the game, so there's no need to check their count against the dealer's count.

**Note**: If the *dealer* busted during its turn, you should skip this count-checking phase. If the dealer busted, the player won the game, so there's no need to check the player's count against the dealer's count.

Milestone 2: Completed Game
=============================

Congratulations, you've implemented Blackjack!

Go through your program and double-check to make sure that you didn't forget to implement anything. If you forgot something, we _will_ find it and make you fix it :)

Our automated test program will be reading your program's output, so **it's really important that you call `print_game_status()` every time the state of the game changes**.

Your program should look **exactly like this** when it's run. Check carefully to make sure that your output is formatted exactly like what you see below!

<asciinema-player src="{{ site.baseurl }}/blackjack_cast_milestone_2.json" rows="35" cols="90" autoplay="true" loop="true"></asciinema-player>

Submitting your project
=======================
Submit a file called `blackjack_<YOUR_NAME>.py`.

For instance, I'd submit a file called `blackjack_jr_heard.py`.

On the first line of that file, write a comment with your name on it, like this:

```
# JR Heard
```

This might seem redundant, but it really is helpful for us when we're grading your programs.

Remember to follow this class's [style guide](https://docs.google.com/document/d/1UbyhIkxOdhpf-MGna_5dwh0yHXe02HTZ69CfEuYv76Y/edit).

Other Features
==============

In real life, Blackjack can be much more complicated than the version we've built. Check out the [Wikipedia page](https://en.wikipedia.org/wiki/Blackjack) - if any features jump out at you (e.g. aces being worth 1 _or_ 11; splitting; betting), go ahead and implement them!

[starter-code]: {{site.baseurl}}/python/blackjack_starter_code.py













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
