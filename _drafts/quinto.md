---
layout: post
title:  "Quinto: Resurrecting an Abandoned Board Game"
---

{% stylesheet quinto %}

I played an old board game called Quinto when I was visiting a friend this past Thanksgiving. I developed a strange fixation on the game and wrote a program that lets you play it against a computer opponent. I'd like to show you that program, and also tell you about the tools I used to build it.

I'll start by teaching you how to play the game. Don't worry, there are just like three rules. If you'd like to skip ahead, [here's the game](http://jrheard.com/quinto/) and [here's the box]({% asset_path quinto.jpg %}).

How It's Played
==============

Quinto is basically Scrabble, except with numbers instead of letters. In Scrabble, your goal is to place several tiles in a row or column, and have them spell a word; you get extra points if your freshly placed tiles contact pre-existing words. Quinto's the same thing, except that instead of trying to make words, **you're trying to make a run of tiles whose sum is a multiple of five**. For example, this move would earn you 20 points.

<div class="grid-container small" id="grid-1"></div>

This next move is *invalid*, though, because these tiles sum to 17, which is not a multiple of five.

<div class="grid-container small" id="grid-2"></div>

That's really most of the game. If you're making the first move, your move must begin in the middle of the board; otherwise, your move must begin next to a previously placed tile.

Now that you know how to make a move, let's talk about how scores work. It's easiest to explain that with examples. Let's say it's your turn, and the board currently looks like this:

<div class="grid-container small" id="grid-3"></div>

If you place the 3 and 5 shown below, you'll get 10 points.

<div class="grid-container small" id="grid-4"></div>

That's because 2 + **3** + **5** = 10.

Now it's your opponent's turn.

If they place the 5 and 7 shown below, they'll get **35** points.

<div class="grid-container small" id="grid-5"></div>

That's because:

* **5** + 5 = 10
* **7** + 3 = 10
* **5** + **7** + 3 = 15

And 10 + 10 + 15 = 35.


Now you know how to play Quinto! The game ends when you run out of tiles; whoever has the highest score at the end of the game wins.

But Wait!
---------

There's one last rule: you can never make a move that would cause there to be a run of more than five tiles in a row. For instance, this move is invalid!

<div class="grid-container medium" id="grid-6"></div>

If you try to put that zero there, your opponent will heckle you, and you'll have to come up with another move instead.

That Rule Is Infuriating
------------------------

It turns out that this last rule makes the game really hard to play, because it adds this whole extra category of stuff that you need to keep track of in your head. When I'm deep into a game and there are a ton of tiles on the board, it takes _all_ of my brainpower to look at the tiles in my hand, look back at the board, and feverishly think about whether placing these three tiles over _here_ would—no, that's not a multiple of five. Hm, maybe over here! Yes, perfect! Except—oh no, I can't put a tile down on _that_ space, because that would break the no-more-than-five-tiles-in-a-row rule!

This some-cells-are-implicitly-verboten rule drove me just completely nuts. I was like: if you can't make a move on a space, the board should light that space up in red! But of course the board couldn't do that, because it's just a dumb piece of cardboard.

So I decided to write a computer program that would light up invalid cells in red and playable cells in green.

<div class="grid-container large" id="grid-7"></div>

While I was at it, I added a few more features that your cardboard copy of Quinto doesn't have:

* An AI opponent that plays against you (and will beat you).
* Automatic score tracking.
* If you play an "optimal" move—the highest-scoring move you could have made with the hand you had—your score for that move will be drawn in green to celebrate your achievement.
* If you mouse over the score for one of your past non-optimal moves, the game will show you what the optimal move *would have been*. You can use this information to learn how to get better at the game! The AI will still beat you, though.

[Give it a try](http://jrheard.com/quinto/). You can also read the [source code](https://github.com/jrheard/quinto/tree/master/src/quinto) if you like. Have a good old time, and then come back so I can tell you about the tools I used to build this game.

Tools
=====

Clojure
-------

[Clojure](https://clojure.org/) is my favorite programming language. It's got a strong focus on writing pure functions—all of its built-in data structures are immutable by default!—but you can still easily perform side effects in it when you want to. It sits on top of Java, so in addition to the excellent libraries that the Clojure community has created, you can also use any Java library in your Clojure program.

The community's great, too—they're very active on [/r/clojure](https://www.reddit.com/r/Clojure/) and the [Clojurians Slack](http://clojurians.net/), and are just generally a really nice, smart, helpful, positive group that I'm proud to be a part of.

Clojure strikes a really nice balance between functional purity and actually getting stuff done. It's a particularly excellent language for writing computer programs that transform and filter data[^1]. You should try it out! I'll include some useful links for beginners at the bottom of this article.

ClojureScript
-------------

I actually wrote my program in [ClojureScript](https://clojurescript.org/), though. ClojureScript is a dialect of Clojure that compiles to JavaScript.

ClojureScript lets you write a Clojure program and then run it in a web browser. This means:

* If you know a little HTML and CSS, your Clojure program now has a GUI.
* You can share your program with other people by just uploading a .js file (and probably an `index.html` and a `style.css`) somewhere and giving your friends a link to it.

ClojureScript programs can also use any JavaScript library, as well as the majority of Clojure libraries. ClojureScript programs aren't just limited to the browser—they can run _anywhere_ that JavaScript programs can run.

On top of all that, programming in ClojureScript is **fun**, because the community has created a ton of really stellar libraries that make development a pleasure. Let's take a look at some of my favorites.

Reagent
-------
[Reagent](https://reagent-project.github.io/) is an extremely minimal React wrapper for ClojureScript. It lets you write code like this:

<script src="https://gist.github.com/jrheard/8c3b19198c36a0efa19be059475e3fa4.js"></script>

<div id="reagent-example"></div>

(Try clicking the square.)

There's not much going on in that code: `cell-class` is an [atom](https://clojure.org/reference/atoms), `@cell-class` is how you read the atom's value, and `reset!` modifies that value. `colorful-cell` is a function that evaluates to a plain old ClojureScript vector. This is all standard stuff.

The remarkable thing about Reagent is that it gives you a _special_ kind of atom, the `r/atom` you see on line 1. When you modify one of those special atoms, Reagent notices, and automatically recalculates just the parts of your UI that use that atom. If any of those parts have changed since the last time they were drawn, Reagent redraws just those parts.

In Quinto, I keep the game's entire state in a [single atom](https://github.com/jrheard/quinto/blob/19c14f3b46fc43632d5b73e20c6c658d26a27b7b/src/quinto/core.cljs#L7), and the UI is just a bunch of [Reagent components](https://github.com/jrheard/quinto/blob/fc81ff5c1f381dbfe7bd0658d73594c0c5a0449b/src/quinto/html.cljs#L199) that take the game state as input and return HTML (represented by regular ClojureScript vectors) as output. Whenever the game's state [changes](https://github.com/jrheard/quinto/blob/19c14f3b46fc43632d5b73e20c6c658d26a27b7b/src/quinto/input.cljs#L16) due to user input, the UI automatically redraws only the parts that need to be redrawn.

You just write a bunch of pure functions and Reagent does the rest. Reagent is fantastic. I adore it.

Figwheel
-------

[Figwheel](https://github.com/bhauman/lein-figwheel) is a lifechanging tool. It's best explained by its author in [this great talk](https://www.youtube.com/watch?v=j-kj2qwJa_E), but here's the short version.

Frontend JavaScript development usually looks like this: you've got your editor up in one window and your app up in another window; you make a change to your JS; and then you manually reload the browser window and navigate the app—by hand—back to the state it was in before you made your change, so that you can see whether or not the code you just changed does the thing you wanted it to do.

If you're working on a game and you're trying to change something that happens halfway through a level, then you have to navigate the hero back to that halfway point, and—oh no, that behavior still isn't right! Better change the JS again and reload the page.

Figwheel makes it so that you don't have to do that any more. When you've got Figwheel running, the changes you make to your code show up _immediately_ in the browser, and your application's state isn't dropped on the ground.

Here's what that looks like. I'm working in my editor off-camera, adding code that attaches a random nonsense CSS class to each cell on the grid. Whenever I save the file I'm working in, Figwheel instantly reloads the code runnning in my browser, leaving my game's state intact.

<img src="https://thumbs.gfycat.com/ImperturbableScientificImperialeagle-size_restricted.gif" />

Spec
----
[Spec](https://clojure.org/guides/spec) is an indispensable tool added in recent versions of Clojure/Script. It lets you formally define what your data looks like:

<script src="https://gist.github.com/jrheard/637d5815786edb8aa44100c018470eb3.js"></script>

spec rules, is an incredibly great addition to the language; before spec people used a great community library called schema, but having an official way to do this is a fantastic thing for the language
:rets aren't checked by instrumentation, orchestra solves this

specter
-------
explain what the tool is and give examples of how i used it
mainly for selects, didn't use transformations
mention that writing custom navigators was really really easy (although my code turned out to be hideous for performance reasons)
thank nathan for the help

intellij/cursive
---------------
i used vim for years to write clojure, but i figured i'd try cursive because a personal license is free, and i loved it, never looked back.
i use the vim plugin and paredit

repl, comment blocks - maybe a gif about this?

color picking
-------------
I don't have a good tool for this, and that really bothers me. The colors I picked are awful, but all the other combinations I tried were even worse. What would you have done if you were building this game and had to pick colors for UI elements? Do you have any advice?

techniques
==========

dev diary
---------
context dump - any time i notice that i'm not sure what code to write next, i force myself to narrate my thoughts into this text file
immense value, primarily in two categories:
* forces me to clearly articulate my thought process (this extremely helps get to a better solution, faster!)
* historical record - makes it easy for me to jump back into the project after some time has passed. i just look at the last page of my dev diary, and now i know what i was working on when i put this down.

i haven't completely figured this out - i sometimes run into issues when i'm working on multiple projects, or on multiple branches within the same project; i'm confident that i'll end up with a working system, and when i do i'll write about it

is-grid-valid? fn
-----------------
read about this somewhere in coders at work, can't remember what chapter
whenever you're working with a novel data structure (mine isn't at all novel but has certain constraints), write a validation function and have an assert somewhere that calls it
this was really really really useful, went off about 15-16 times over the course of development
found three main categories of bug:
* the starting grid i had manually hard-coded didn't actually sum to a multiple of five
* a bug in the AI code was causing the computer to make an invalid move
* a bug in a core quinto.grid function broke validation, so that valid grids were being reported as invalid
each time one of these bugs was introduced, i was immediately notified because an assert failed, and i was able to immediately fix the bug; without that assert, days could have passed during which the program's logic was quietly incorrect
unit tests would have surfaced these categories of bugs too, but this program is small and i didn't feel like writing unit tests for it

at the end of development i realized that this was running way way more often than it needed to, so i removed that call and my perf sped up 10x, whoops

that's it!
----------

cljs is truly a sweet spot for writing turn-based games, because you get to focus on happily writing simple pure functions that express the game's business logic, and your UI is just a pure function of your "game state", and clojure's "atom" abstraction makes it easy for you to manage that state confidently.

if you'd like to get started with clojure, consider XYZ resources (brave and true?)



TODO refer to https://lambdaisland.com/blog/29-12-2017-the-bare-minimum-clojure-mayonnaise somewhere
or maybe don't


TODO if it turns out to be a good story, talk about how i tracked down the heisenbug by writing a program that played the game's UI
it didn't turn out to be a good story but whatever

TODO see if there's a good place to link to clojurescript for skeptics
https://www.youtube.com/watch?v=gsffg5xxFQI




appendix

quinto origin story
printed once in 64, once in 68, then never again
several different versions were printed, each using different board sizes and tile distributions; i picked an arbitrary board size that i liked, and used the tile distribution that went with the version of the game that i played at my friend's house

brunner

[^1]: This is all computer programs.

{% javascript quinto %}
<script type="text/javascript">quinto.core.main()</script>


TODO link to http://timothypratley.blogspot.com/2017/01/reagent-deep-dive-part-1.html ?
