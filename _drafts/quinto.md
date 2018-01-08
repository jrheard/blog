---
layout: post
title:  "Quinto"
---

{% stylesheet quinto %}

I played an old board game called Quinto when I was visiting a friend this past Thanksgiving. Afterward, I developed a strange fixation on the game and wrote a program that lets you play it against a computer opponent. I'd like to show you that program, and also tell you a little bit about the tools I used to build it.

I'll start by teaching you how to play the game. Don't worry, there are just like three rules. If you'd like to skip ahead, [here's the game](http://jrheard.com/quinto/) and [here's the box](quinto.jpg).

How It's Played
==============

Quinto is basically Scrabble, except with numbers instead of letters. In Scrabble, your goal is to place several tiles in a row or column, and have them spell a word; you get extra points if your freshly placed tiles contact pre-existing words. Quinto's the same thing, except that instead of trying to make words, **you're trying to make a run of tiles whose sum is a multiple of five**. For example, this move would earn you 20 points.

<div class="grid-container small" id="grid-1"></div>

This move is *invalid*, though, because these tiles sum to 17, which is not a multiple of five.

<div class="grid-container small" id="grid-2"></div>

That's really most of the game. If you're making the first move, your move must begin in the middle of the board; otherwise, your move must begin next to at least one previously placed tile.

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

There's one more rule: you can never make a move that would cause there to be a run of more than five tiles in a row. For instance, this move is invalid!

<div class="grid-container medium" id="grid-6"></div>

Placing that 0 there would result in there being six tiles in a row, which is illegal. If you try to put that zero there, your opponent will heckle you, and you'll have to come up with another move that actually works.

That Rule Is Infuriating
------------------------

It turns out that this last rule makes the game really hard to play. When I'm deep into a game and there are a ton of tiles on the board, it takes _all_ of my brainpower to try to look at the tiles in my hand, look back at the board, and feverishly check to see if placing these three tiles over _here_ would - no, that's not a multiple of five. Hm, maybe over here! Yes, perfect! Except — oh no, I can't put a tile down on _that_ space, because that would break the no-more-than-five-tiles-in-a-row rule!

This some-cells-are-implicitly-verboten rule drove me just completely nuts. I was like: if you can't make a move on a space, the board should light that space up in red! But of course the board couldn't do that, because it's just a dumb piece of cardboard.

So I decided to write a computer program that would light up invalid cells in red and playable cells in green.

<div class="grid-container large" id="grid-7"></div>

While I was at it, I added a few more features that your cardboard copy of Quinto doesn't have:

* An AI opponent that plays against you (and will beat you).
* Automatic score tracking.
* If you play an "optimal" move — the highest-scoring move you could have made with the hand you had — your score for that move will be drawn in green to celebrate your achievement.
* If you mouse over the score for one of your non-optimal moves, the game will show you what the optimal move *would have been*. You can use this information to learn how to get better at the game! The AI will probably still beat you, though.

[Give it a try](http://jrheard.com/quinto/). Have a good old time, and then come back so I can tell you about the tools I used to build this game.

Tools
=====

Clojure
-------
learned clojure in 2011, been using it for side projects since then
all the data structures are immutable by default, there's a strong culture of functional programming in the language's community, but you can still easily perform side effects whenever you want to
the language sits on top of java so you get a library ecosystem for free, and the libraries that the clojure community has created a really amazingly good

clojure is a fantastic language for writing programs that transform and filter data[1]
[1] this is all programs

clojurescript
-------------
but i actually wrote my program in clojurescript, which is a version of clojure that compiles to javascript. cljs sounded like a goofy idea to me when i first heard about it, but i've been using it for years now and i completely love it, because in addition to all the benefits you get with clojure, cljs has two additional great things going for it:

* cljs programs are almost always written to be run inside of a web browser, which means that if you already know how to write HTML and CSS, using cljs gives your clojure program a UI for free!
* because cljs programs can easily be run inside of a web browser, you can just upload your program somewhere and send your friend a link to it, and they can use your program without having to install anything!

on top of that, you can also use any javascript library as well as most clj libraries, and again the libraries that the clojurescript community has written are really really good.

clj/s is truly a sweet spot for writing turn-based games, because you get to focus on happily writing simple pure functions that express the game's business logic, and your UI is just a pure function of your "game state", and clojure's "atom" abstraction makes it easy for you to manage that state confidently.

reagent
-------
would have tried to write this myself if it didn't already exist, saved me a lot of trouble, also is _extremely great_

intellij/cursive
---------------
i used vim for years to write clojure, but i figured i'd try cursive because a personal license is free, and i loved it, never looked back.
i use the vim plugin and paredit

repl, comment blocks - maybe a gif about this?

figwheel
-------
somehow express haumann's thing about how usually you have to make a change to your code, then restart your program and navigate it back to the same state that you were looking at before you made your change, and how figwheel solves that problem

and also just feels extremely extremely good to use

spec
----
spec rules, is an incredibly great addition to the language; before spec people used a great community library called schema, but having an official way to do this is a fantastic thing for the language
:rets aren't checked by instrumentation, orchestra solves this

specter
-------
explain what the tool is and give examples of how i used it
mainly for selects, didn't use transformations
mention that writing custom navigators was really really easy (although my code turned out to be hideous for performance reasons)
thank nathan for the help

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
if you'd like to get started with clojure, consider XYZ resources (brave and true?)



TODO refer to https://lambdaisland.com/blog/29-12-2017-the-bare-minimum-clojure-mayonnaise somewhere
or maybe don't


TODO if it turns out to be a good story, talk about how i tracked down the heisenbug by writing a program that played the game's UI




appendix

quinto origin story
brunner

{% javascript quinto %}
<script type="text/javascript">quinto.core.main()</script>
