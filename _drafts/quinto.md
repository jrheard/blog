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
would have tried to write this myself if it didn't already exist, saved me a lot of trouble

intellij/cursive
repl, comments

figwheel

spec

specter

techniques
==========

dev diary

could have sworn there was more stuff
