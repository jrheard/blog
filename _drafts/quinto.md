---
layout: post
title:  "Quinto"
klipse: true
---

Quinto
======

* origin story
* explain rules
  * first show just a few tiles with no highlighting (use css to disable)
  * then show red/green squares

* built that, then wondered how to write an AI that plays the game
* once that was done, couldn't not let the user play against the AI
* and here we are

it's pretty obvious that quinto died out because it's not a very good board game
but it was a fun puzzle to chew on, and i enjoyed spending my time this way
i'd like to talk about the tools and techniques i used when writing this program, because they work very well for me and you might find them useful

tools
=====

clojure/script
learned clojure in 2011, been using it for side projects since then
all the data structures are immutable by default, there's a strong culture of functional programming but you can perform side effects whenever you want to
the language sits on top of java so you get a library ecosystem for free, and clj's libraries are actually really good on top of that
cljs compiles to javascript, so you get the js library ecosystem, and clj/s's libraries, and you also get a UI for free
clj/s is a real sweet spot for writing turn-based games, because you get to focus on happily writing the game's business logic, and your UI is just a pure function of your game state

reagent
would have tried to write this myself if it didn't already exist, saved me a lot of trouble, also is _extremely great_

intellij/cursive
repl, comments

figwheel

spec
rules, is an incredibly great addition to the language, clojure was sorely missing an official way to do this
:rets aren't checked by instrumentation, orchestra solves this

specter
explain what the tool is and give examples of how i used it
mention that writing custom navigators was really really easy (although my code turned out to be hideous for performance reasons)
thank nathan for the help

techniques
==========

dev diary
context dump - any time i notice that i'm not sure what code to write next, i force myself to narrate my thoughts into this text file
immense value, primarily in two categories:
* forces me to clearly articulate my thought process (this extremely helps get to a better solution, faster!)
* historical record - makes it easy for me to jump back into the project after some time has passed. i just look at the last page of my dev diary, and now i know what i was working on when i put this down.

is-grid-valid? fn
read about this somewhere in coders at work, can't remember what chapter
whenever you're working with a novel data structure (mine isn't at all novel but has certain constraints), write a validation function and have an assert somewhere that calls it
this was really really really useful, went off about 15-16 times over the course of development
found three main categories of bug:
* the starting grid i had manually hard-coded didn't actually sum to a multiple of five
* a bug in the AI code was causing the computer to make an invalid move
* a bug in a core quinto.grid function broke validation, so that valid grids were being reported as invalid
each time one of these bugs was introduced, i was immediately notified because an assert failed, and i was able to immediately fix the bug; without that assert, days could have passed during which the program's logic was quietly incorrect
unit tests would have surfaced these categories of bugs too, but this program is small and i didn't feel like writing unit tests for it
