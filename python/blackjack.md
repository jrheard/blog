---
layout: page
title:  "Madison CS 3-4: Blackjack"
---

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

<pre><code class="py">
card = [5, "diamonds"]
print(card[0])
print(card[1])
</code></pre>

`[5, "diamonds"]` is a two-item list that **represents** a five of diamonds card. "Representing" something means "getting it out of your head and into a computer program."

There are a lot of different ways to represent a five of diamonds in a Python program. If you know how to use dicts, classes, or tuples, feel free to use one of those instead. If you don't know how to use any of those, then don't worry; a two-item list is just as good as those other things. All that matters is that you choose *some* way of representing playing cards in your Python program. A two-item list works great.

Representing a Deck
-------------------

That's just one card, though, and there are fifty-two cards in a deck.

Each deck of cards has four **suits**: `diamonds`, `hearts`, `spades`, and `clubs`.

Each suit has thirteen cards: an ace, the cards 2 through 10, a jack, a queen, and a king. Jacks, queens, and kings have the value 10. In our version of blackjack, aces have the value 1.

Here's a full suit of diamonds:

<pre><code class="py">
diamonds = [
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
	[10, "diamonds"],
	[10, "diamonds"],
	[10, "diamonds"],
]

print("There are " + str(len(diamonds)) + " cards in this suit.")
print("The sixth card's value is " + str(diamonds[5][0]) + ".")
</code></pre>

Your program's deck should contain fifty-two cards: thirteen cards for each of the four suits.


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
