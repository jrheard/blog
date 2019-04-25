---
layout: page
title:  "Madison CS 3-4: Roguelike"
---

This project is going to be kind of an experiment! We're going to give you some starter code for a terminal-based game, and we'll give you some ideas about features you could add to it, and we're going to see what happens.

This assignment doesn't have quite as many rules as we've had in previous projects - the goal is for you to come up with some fun features and add them to your game!

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

1. **Download the starter code [here]({{ site.baseurl }}/roguelike_starter_code.zip).**
1. Unzip it somewhere (e.g. to a folder in your Y: drive)
1. Double-click on `game.py`

That should be it! You'll be making changes to these files over the course of this project.

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

Feel free to add more code to this file. You can also create more files if you want, it's a useful thing to do as your project gets bigger.

As a general rule of thumb: it's hard to read and understand a big complicated file with 1000 lines of code in it and a vague name like `program.py`; it's much easier to read and understand several smaller files, each of which has 150-200 lines of code and a good clear name like `ai.py` or `physics.py` or `quest.py`.


Seriously, Read Those Files
===========================

This is what programming in real life is like. It's almost never the case that you're starting a new program completely from scratch - you'll almost always be working on a (probably really big!) program that someone else wrote years ago, or that you wrote a few weeks ago but it's been long enough that now you don't really remember what all the code does.

This is what you do: you read through the preexisting code, convince yourself that you understand what it does and how it fits together, and _then_, once you're familiar with the codebase, you can start making changes and adding features.

One Last Thing Before We Really Get Started
===========================================
This project is going to be bigger than the ones we've worked on so far. When you're working on a big program, it's important to use something called "version control".

You've probably already had an experience where you were in the middle of a project, and your program was working totally great, but then you spent half an hour working on a new feature and now your program's totally broken and you just cannot figure out how to fix it. Version control systems exist to solve this problem. A version control system lets you say: okay, my program is working great _right now_, so let's save this version of it for later. Then, if you go off and make some changes to it that totally break your program, you can both a) _see what those changes were_ and b) get rid of those changes and go back to the last working version of your program.

This might not sound like a big deal, but it's really really important - it lets you confidently work on cool experimental features, because you know that if you accidentally trash your program, you can always easily go back to the last working version.

`git` is a very good version control system. I use it every single time I write a program. If you'd like to learn how to use it, I recommend [Codecademy's git tutorial](https://www.codecademy.com/learn/learn-git). You don't need to work through parts 3 and 4, the first two parts are fine for now; you don't need the paid parts of the tutorial, the free parts are totally fine.

**You don't have to work through that tutorial and use git for this project if you don't want to**, I'm just telling you about it in case this sounds useful and you'd like to learn it and try it out!

Using git is a really, really, really good idea when working on a complicated program.

The Goal
========

The point of this project is for you to come up with some cool features and then build them. Here are some ideas:

* Monsters that just sit there and don't do anything
* A goal space (if the player makes it to this space, they've beaten the game!)
* A combat system (when you bump into a monster, you fight it!)
* XP / leveling up / stats
* Monster AI (monsters follow you around!)
* A combat log that says stuff like "you strike the skeleton for 3 damage!"
* A dog that you can pet
* Items / power-ups
* Doors / traps
* Spells / ranged combat
* Puzzles
* Quests
* Randomly generated levels

That's just some stuff off the top of my head. If you come up with an idea you like better, you can do that instead!


Implementing Dumb Monsters
==========================

To give you an idea of how to get started, I'm going to show you how I would write code that adds dumb goblins to the level. They just sit there and don't do anything, and the player can't move into a space if it has a goblin in it. Here's what that looks like:

<asciinema-player src="{{ site.baseurl }}/roguelike_monster.json" rows="32" cols="90" autoplay="true" loop="true"></asciinema-player>

Here are the things I did in order to add that feature to the game:

1. Added a couple of `g`s to `level.txt`.
1. Updated `load_level()` to look for `'g'`s in `level.txt`; every time we find a `'g'` we make a goblin dictionary, add that dictionary to a list, and include that list in the returned "game dictionary".
1. Updated `draw_game()` so that it prints out a `g` on spaces that have a goblin in them.
1. Updated `move()` so that it doesn't allow the player to move into a space that has a goblin in it.

Does that make sense? Reread `roguelib.py` until you're sure that the things I did make sense.

Once I had done all of those things, I had a working goblin feature! Notice that this involved messing around with a lot of the code in `roguelib.py` - you'll have to do this too when you add your own features. It's going to involve reading code and figuring out what it does and figuring out what you want to do and where you should make your changes. This is what programming is like! :)

**[Here's the code I wrote to make that happen](https://gist.github.com/jrheard/cb609d57e3b41ff622c790bdf337a7cc).** You don't have to read it if you don't want to, but it's there as a reference in case you find it useful when adding your own features. This file is a "diff", which stands for "the difference between an old version of a program and a new version of that program" - red lines are old lines that I removed, green lines are new lines that I added.

Submitting your project
=======================
TODO TAMARA how should they submit their project? it involves multiple files! i feel like if we ask them to make a .zip file and submit that, we'll have to hold their hands through the whole process. alternatively we could ask them to have files like roguelib_jr_heard.py, game_jr_heard.py, and text_jr_heard.txt, but that sounds awful. aaaaa! what should we do?


Assorted Notes
==============

I've written a couple of really neat articles on how to generate simple random levels using a couple of different algorithms:

* [Drunkard's Walk](https://blog.jrheard.com/procedural-dungeon-generation-drunkards-walk-in-clojurescript)
* [Cellular Automata](https://blog.jrheard.com/procedural-dungeon-generation-cellular-automata)

Here's a list of some of my favorite roguelikes (in no particular order):

* Risk of Rain
* FTL
* Dead Cells
* Slay the Spire
* Isaac
* Spelunky
* Teleglitch
* Crypt of the Necrodancer
* Cogmind
* Caves of Qud





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
