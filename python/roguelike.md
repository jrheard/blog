---
layout: page
title:  "Madison CS 3-4: Roguelike"
---

This project is going to be kind of an experiment! We're going to give you some starter code for a terminal-based game, and we'll give you some ideas about features you could add to it, and we're going to see what happens. This assignment doesn't have quite as many rules as we've had in previous projects - come up with whatever fun features you want and add them to your game!

What's A Roguelike?
===================

In the old days, there was a game called [Rogue](https://en.wikipedia.org/wiki/Rogue_(video_game)). It looked like this:

{% img rogue.png alt:"via Wikipedia" %}

The player's character is the little yellow smiley face. Wikipedia says:

> In Rogue, players control a character as they explore several levels of a dungeon as they seek the Amulet of Yendor located in the dungeon's lowest level. The player-character must fend off an array of monsters that roam the dungeons. Along the way, they can collect treasures that can help them offensively or defensively, such as weapons, armor, potions, scrolls, and other magical items. Rogue is turn-based taking place on a square grid represented in ASCII.

A lot of the ideas originally found in Rogue have since spread to tons of other video games, and we call those games **roguelikes**. Here's one called Brogue:

{% img Brimstonebattle.png width:800 height:459 %}

Here's a super cool one called Cogmind:

<iframe src="https://giphy.com/embed/DwSVbIKw0R808" width="480" height="340" frameBorder="0" class="giphy-embed" allowFullScreen style="display: block; margin: 40px auto;"></iframe>

In this project, you'll be building a roguelike of your very own.

What We Give You
================

This project comes with code for an extremely basic game. It looks like this:

<asciinema-player src="{{ site.baseurl }}/roguelike_starter.json" rows="32" cols="90" autoplay="true" loop="true"></asciinema-player>

You're the `@` sign, you can move around, you can't go through walls, and you can quit the game when you get bored.

How To Run The Game
===================

TODO jrheard

Reading The Code
================

The starter code comes with three files:

1: `level.txt`
-----------

A simple text file that looks like [this](https://gist.github.com/jrheard/f721c0e9a95b41595e85228273a8b0d5). It's the level! If you want the game's level to look differently, you can go ahead and edit `level.txt`. A `'#'` is a wall, a `' '` is an empty space, and a `'@'` is the player's starting position.

2: `roguelib.py`
----------------

A Python file that contains some useful functions that can be combined together in order to make a simple roguelike game. Go ahead and read through this file - you don't have fully read and understand every single line of code right now before you've started working on the project, but it'd be a good idea to look through the file and see what functions it defines and what their docstrings say the functions do.

You'll have to make changes to some of these functions when you add new features to the game!

3: `game.py`
------------

A small Python file that combines the functions from `roguelib.py` together into a simple game loop. Read the game loop and convince yourself that you understand how it works. Refer back to the code in `roguelib.py` whenever `game.py` uses a function that don't fully understand.

Feel free to add more code to this file. You can also create more files if you want, it's a useful thing to do as your project gets bigger. It's hard to read and understand a big complicated file with 1000 lines of code in it; it's much easier to read and understand several smaller files with 150-200 lines of code in each one.


Seriously, Read Those Files
===========================

This is what programming in real life is like. It's almost never the case that you're starting a new program completely from scratch - you'll almost always be working on a (probably really big!) big program that someone else wrote years ago, or that you wrote a few weeks ago but it's been long enough that you don't really remember what all the code does.

This is what you do: you read through the preexisting code, convince yourself that you understand what it does and how it fits together, and _then_, once you're familiar with the codebase, you can start making changes and adding features.





* encourage git
* show recording of monster branch, show diff, explain steps at a high level
* list ideas
* link to random generation blog posts

* list of roguelikes to check out
	* spelunky
	* qud
	* ftl
	* dead cells
	* slay the spire





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
