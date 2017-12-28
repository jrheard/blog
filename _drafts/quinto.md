---
layout: post
title:  "Quinto"
klipse: true
---

Quinto
======

i played a board game at a friend's house, then wrote a computer-program version of it, complete with an AI that plays against you. i enjoyed writing this program, and am proud of the code i wrote, but my primary goal for this article is to showcase the tools i used to write it, because they're very good tools and you might find them useful.

* origin story
* explain rules
  * first show just a few tiles with no highlighting (use css to disable)
  * then show red/green squares

* built that, then wondered how to write an AI that plays the game
* once that was done, letting the user play against the AI seemed like it'd be straightforward, but the UI was surprisingly interesting/difficult to figure out

it's pretty obvious that quinto died out because it's not a very good board game
but it was a fun puzzle to chew on, and i enjoyed spending my time this way
now let's talk about the tools and techniques i used when writing this program.

tools
=====

clojure
-------
learned clojure in 2011, been using it for side projects since then
all the data structures are immutable by default, there's a strong culture of functional programming in the language's community, but you can still easily perform side effects whenever you want to
the language sits on top of java so you get a library ecosystem for free, and the libraries that the clojure community has created a really amazingly good

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
