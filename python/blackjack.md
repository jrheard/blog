---
layout: page
title:  "Madison CS 3-4: Blackjack"
---

<style>
.cm-s-friendship-bracelet {
	font-size: 16px;
}
</style>

In this project, you'll write a Python program that lets a user play blackjack.

How It's Played
===============

Blackjack is a card game. The player starts with two cards, and can choose to draw more cards ("hit") or to end their turn ("stay"). Once the player is done drawing cards, it's the **dealer**'s turn. Once the dealer's turn is over, the game tells the player whether they won or lost.

A card has a **suit** (a string like `'spades'` or `'diamonds'`), and a **value** (a number between `1` and `10`). Each player has a **count**, which is the sum of all of their cards' values. If I have a five of diamonds, a three of hearts, and a ten of spades, my count is 18.

The goal of the game is to "**beat the dealer by getting a count as close to 21 as possible, without going over 21**"[^1].

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
card = [5, "diamonds"]
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

`[5, "diamonds"]` is a two-item list that **represents** a five of diamonds card.

"Representing" something means "getting it out of your head and into a computer program." In this example, I took the nebulous concept of \<a five of diamonds card\> and turned it into \<a list with two things in it; the first thing is a number that represents the card's value, and the second thing is a string that represents the card's suit\>. This is important because Python doesn't really know what you mean when you say "a five of diamonds card", but it *does* understand `[5, "diamonds"]`.

There are a lot of different ways to represent a five of diamonds in a Python program. If you know how to use dicts, classes, or tuples, feel free to use any of those instead. If you don't know what those are yet, don't worry: a two-item list is just as good as those other things. All that matters is that you choose *some* way of representing playing cards in your Python program. A two-item list works great.

Representing a Deck
-------------------

That's just one card, though, and there are fifty-two cards in a deck.

A deck of cards has four **suits**: `diamonds`, `hearts`, `spades`, and `clubs`.

Each suit has thirteen cards:

* an ace,
* the cards 2 through 10,
* and a jack, a queen, and a king.

Jacks, queens, and kings have the value 10. In the simple version of blackjack that you're building in this project, aces always have the value 1.

Here's a full suit of diamonds:

<pre><code class="py">
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

Notice that `diamonds` is a list of cards, and a "card" is a list like `[5, "diamonds"]` - so `diamonds` is a list of lists.

Your program's deck should contain fifty-two cards: thirteen cards for each of the four suits.

Shuffling the Deck
-------------
Once you've got a deck of cards, you should shuffle the deck. Your game's deck is likely represented by a list. Here's how you can randomize the order of the items in a list:

<pre><code class="py">
import random

my_favorite_foods = ["Fried Rice", "Red Curry", "Pizza", "Sandwiches"]

# This line is the important one!
random.shuffle(my_favorite_foods)

print(my_favorite_foods)
</code></pre>

Dealing Hands
-------------

Now that your deck's shuffled, you should give two cards to the player and two cards to the dealer. The player should have a **hand**, which is a list of cards; the dealer should have a hand, too.

Here's an example of what a hand might look like:

<textarea class="hidden">
[[10, "spades"], [5, "clubs"]]
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

Make sure that whenever you deal a card to someone, that card is removed from the deck. There should only ever be fifty-two cards at a time throughout your program—if the player has two cards and the dealer has two cards, then the deck should have forty-eight cards.

Milestone 1: Displaying Output
==============================

You've done a lot of good stuff so far! Now add some `print()` calls that tell the player about their hand and the dealer's hand. Add another `print()` call that prints out the number of cards left in the deck.

At this point, your program should look exactly like this when it's run:

<asciinema-player src="{{ site.baseurl }}/blackjack_cast_milestone_1.json" rows="13" cols="90" autoplay="true" loop="true"></asciinema-player>

The cards and counts your program prints out will be different every time the program is run, so it's fine that they'll be different from the output in my demo above.


Player's Turn
=============

Once the cards have been dealt, it's the player's turn. In our simple version of Blackjack, the player has two options:

1. The player can draw another card by saying `"hit"`. They can do this as many times as they want, as long as their **count** is below 21.
1. The player can end their turn by saying `"stand"`.

Your program should prompt the user for input over and over until they say `"stand"`, at which point their turn is over. You'll want to use a `while` loop to do this. Here's some starter code that you might find useful:

<textarea class="hidden">
while True:
	move = input("Do you want to 'hit' or 'stay'? ")

	if move == 'hit':
		# TODO: Remove a card from the deck,
		# add it to the player's hand,
		# and update their count.

		# TODO: If the player's count is
		# greater than 21, end the game
		# and tell them that they lost.

	if move == 'stay':
		break
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

Notice the part where you should end the loop (and the game!) if the player's count exceeds 21. That's called "busting", and it's game over for the player.

TODO

dealer's turn

end-game summary

demo

submission notes

extra credit suggestions


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
