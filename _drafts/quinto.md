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

[Clojure](https://clojure.org/) is my favorite programming language. It's got a strong focus on writing pure functions—all of its built-in data structures are immutable!—but you can still easily perform side effects when you want to. It sits on top of Java, so in addition to the excellent libraries that the Clojure community has created, you can also use any Java library in your Clojure program.

The community's great, too—they're very active on [/r/clojure](https://www.reddit.com/r/Clojure/) and the [Clojurians Slack](http://clojurians.net/), and are just generally a nice, smart, helpful, positive group that I'm proud to be a part of.

Clojure strikes a nice balance between functional purity and actually getting stuff done. It's a particularly excellent language for writing computer programs that transform and filter data[^1]. You should try it out! I'll include some useful links for beginners at the end of this article.

ClojureScript
-------------

I actually wrote my program in [ClojureScript](https://clojurescript.org/), though. ClojureScript is a dialect of Clojure that compiles to JavaScript[^2].

ClojureScript lets you write a Clojure program and then run it in a web browser. This means:

* If you know a little HTML and CSS, your Clojure program now has a GUI.
* You can share your program with other people by just uploading a .js file (and probably an `index.html` and a `style.css`) somewhere and giving your friends a link to it.

ClojureScript programs can use any JavaScript library, as well as the majority of Clojure libraries. ClojureScript programs aren't just limited to the browser—they can run _anywhere_ JavaScript programs can run.

On top of all that, programming in ClojureScript is **fun**, because the community has created a ton of really stellar libraries that make development a pleasure. Let's take a look at some of my favorites.

Reagent
-------
[Reagent](https://reagent-project.github.io/) is a React library for ClojureScript with a beautifully minimal interface. It lets you write code like this:

<script src="https://gist.github.com/jrheard/8c3b19198c36a0efa19be059475e3fa4.js"></script>

<div id="reagent-example"></div>

(Try clicking the square.)

There's not much going on in that code: `cell-class` is an [atom](https://clojure.org/reference/atoms), `@cell-class` is how you read the atom's value, and `reset!` modifies that value. `colorful-cell` is a function that evaluates to a plain old ClojureScript vector. This is all standard stuff.

The remarkable thing about Reagent is that it gives you a _special_ kind of atom, the `r/atom` you see on line 1. When your code modifies one of those special atoms, Reagent notices, and automatically recalculates just the parts of your UI that use that atom. If any of those parts have changed since the last time they were drawn, Reagent redraws just those parts.

In Quinto, I keep the game's entire state in a [single atom](https://github.com/jrheard/quinto/blob/19c14f3b46fc43632d5b73e20c6c658d26a27b7b/src/quinto/core.cljs#L7), and the UI is just a bunch of [Reagent components](https://github.com/jrheard/quinto/blob/fc81ff5c1f381dbfe7bd0658d73594c0c5a0449b/src/quinto/html.cljs#L199) that take the game state as input and return HTML (represented by regular ClojureScript vectors) as output. Whenever the game's state [changes](https://github.com/jrheard/quinto/blob/19c14f3b46fc43632d5b73e20c6c658d26a27b7b/src/quinto/input.cljs#L16) due to user input, the UI automatically redraws only the parts that need to be redrawn.

You just write a bunch of pure functions and Reagent handles the rest. Reagent is fantastic. I adore it.

If you'd like to learn more about Reagent, I recommend [Timothy Pratley's excellent articles](http://timothypratley.blogspot.com/2017/01/reagent-deep-dive-part-1.html) on the library.

Figwheel
-------

[Figwheel](https://github.com/bhauman/lein-figwheel) is a lifechanging tool. It's best explained by its author in [this great talk](https://www.youtube.com/watch?v=j-kj2qwJa_E), but here's the short version.

Frontend JavaScript development usually looks like this: you've got your editor up on one screen and your app up in another; you make a change to your JS; and then you manually reload the browser window and navigate the app—by hand—back to the state it was in before you made your change, so that you can see whether or not the code you just changed does the thing you wanted it to do.

Figwheel makes it so that you don't have to do that any more. When you've got Figwheel running, the changes you make to your code show up _immediately_ in the browser, and your application's state isn't dropped on the ground in the process.

Here's what that looks like. I'm working in my editor off-camera, adding code that attaches a random nonsense CSS class to each cell on the grid. Whenever I save the file I'm working in, Figwheel instantly updates my running game's behavior without clobbering its state.

<img src="https://thumbs.gfycat.com/ImperturbableScientificImperialeagle-size_restricted.gif" />

Spec
----
[Spec](https://clojure.org/guides/spec) is an indispensable tool added in recent versions of Clojure/Script. It lets you formally specify what your program's data looks like.

<script src="https://gist.github.com/jrheard/637d5815786edb8aa44100c018470eb3.js"></script>

Once you've done that, you can also annotate your program's functions. For example, `draw-tiles` is a function that removes `num-tiles` tiles from a `deck` and adds them to a player's `hand`.

<script src="https://gist.github.com/jrheard/7bd6f27cb49240b50a87a391092d2da3.js"></script>

Annotations like this make it easy for a human reader to figure out the shape of your program's data. These annotations can also be **verified** using [`instrument` and `check`](https://clojure.org/guides/spec#_instrumentation_and_testing).[^3]

I'm very happy that spec was added to the language. It makes Clojure/Script programs a lot easier to write, read, understand, and confidently modify.

Specter
-------

[Specter](https://github.com/nathanmarz/specter) is a library that allows you to elegantly and performantly manipulate Clojure data. [This screencast](https://www.youtube.com/watch?v=rh5J4vacG98) was extremely useful when I was first trying to wrap my head around it.

This was my first time using Specter, and I really enjoyed it. I'll be using it often in the future.

IntelliJ and Cursive
---------------

[Cursive](https://cursive-ide.com/) is a plugin that makes [IntelliJ](https://www.jetbrains.com/idea/) into a glorious environment for writing Clojure/Script programs. If you're using Cursive for "non-commercial use, including personal hacking, open-source and student work", then it's [free](https://cursive-ide.com/buy.html).

My favorite feature of Cursive is its REPL integration. Lisp programmers are used to this sort of thing, and often have `comment` blocks in their programs where they stash chunks of code that are useful for debugging. I never understood what that was all about until I tried doing it myself, and now I do this constantly: you just move the cursor over one of those blocks of code, press a keybinding, and you immediately see the result without leaving your editor. It makes for an incredibly tight feedback loop.

Here's what that looks like in action—I recorded this video when I was working on the code featured in my [Drunkard's Walk]({{site.baseurl}}{% post_url 2016-10-31-procedural-dungeon-generation-drunkards-walk-in-clojurescript %}) post.

<iframe class="youtube-embed" width="560" height="315" src="https://www.youtube.com/embed/Ilfk_OpXKgc?rel=0&amp;start=1603" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

I use Cursive with rainbow parentheses and paredit mode enabled. I also have the IdeaVim plugin installed so that I can use Vim keybindings.

Color Picking
-------------
I don't have a good tool for this, and that bothers me. The colors I picked for the Quinto UI are awful, but all of the other combinations I tried were even worse.

What would you have done if you were building this game and had to pick colors for UI elements? Do you have any advice for me?

Techniques
==========

Dev Diary
---------

In the past few personal projects I've worked on, I've created a [`dev-diary.txt`](https://github.com/jrheard/quinto/blob/master/dev-diary.txt) file and used it as a scratchpad. Whenever I notice that I'm not sure what code to write next, I force myself to narrate my thoughts into that text file.

This serves several purposes:

* Expressing my thoughts in written form forces me to actually figure out what problem I'm currently facing and what solutions I'm currently thinking about. This helps me get to a better solution, faster.
* If I can't remember why I made a particular decision, I can just search for it in the text file to see what other options I considered.
* If it's been a little while since the last time I worked on the project and I don't remember what I was working on, I can just look at most recent entry in my dev diary and I'm off to the races.

This habit has been immensely valuable for me. I'm still figuring out the specifics—this system breaks down if I'm working on several projects at once, or on projects where I'm not the sole contributor—but those are solvable problems, and when I do solve them I'll do a brief writeup about my finalized workflow.

Grid Validation Function
-----------------

In [Coders At Work](http://www.codersatwork.com/), an interviewee (can't remember which) has this piece of (paraphrased) advice: when you're working with a novel data structure, you should create a function that inspects the data structure and checks to see if it's "valid", and then you should call that validation function all over the place.

My Quinto grid is just a 2D vector of integers-or-`nil`s, which is not particularly novel. It does have a bunch of invariants that need to be maintained, though: you can never have more than five non-`nil` cells in a row; all contiguous runs of cells have to sum to a multiple of five; etc.

Early on in development, I wrote [a function that verifies these invariants](https://github.com/jrheard/quinto/blob/daed3c3a426f00a5f9c9176b087dedfb8765bff7/src/quinto/grid.cljs#L208), and sprinkled a few asserts in various places in my program[^4]. These asserts failed immediately whenever I introduced a bug into the program, and so I was able to immediately fix the bug instead of finding it hours or days later.

(Unit tests would have surfaced these bugs too.)

That's It!
----------

ClojureScript with Reagent is truly a sweet spot for writing turn-based games. You happily write pure functions that express the game's business logic; your UI is just a pure function of your game state; and Clojure's atom abstraction makes it easy for you to manage that state confidently.

I love these tools and hope you'll consider trying them out yourself.

If you're interested in learning Clojure, I hear that [Clojure for the Brave and True](https://www.braveclojure.com/) is the current best way to do that. I haven't read that book myself, but it has a good reputation. I _can_ confidently recommend [Clojure Programming](http://shop.oreilly.com/product/0636920013754.do) and [The Joy of Clojure](https://www.manning.com/books/the-joy-of-clojure-second-edition), because those are the books that I read when I learned the language.


<h1 id="appendix-a" class="appendix">Appendix A: Quinto Origin Story</h1>

From what I can piece together from [BoardGameGeek](https://boardgamegeek.com/boardgame/2366/quinto), Quinto was printed once in 1964, once in 1968, and then never again. My friend's copy was a purchase from Goodwill.

Several different versions of Quinto were printed, each using different board sizes and tile distributions. For my program, I picked an arbitrary board size I liked, but I used the same [tile distribution](https://github.com/jrheard/quinto/blob/2913a907344d2c016793785badf276c3c86dc04f/src/quinto/deck.cljs#L7) from the particular version I'd played at my friend's house.

To be honest, I think Quinto died out because it's not a very good game. It was fun to program, though!

Appendix B: Quintus Origin Story
================================

The Quinto box looks like this:

{% img quinto_box.jpg width:286 height:400 %}

Those Roman(?) dudes, combined with the name Quinto, reminded me of Latin class. I took Latin in middle school because my mom heard it would help my SAT scores. My teacher, Mr. Brunner, assigned me the "Latin name" Quintus.

I remember liking Mr. Brunner, so when Quinto's name reminded me of his class, I googled his name to see how things ended up going for him. He seems to be doing well, but that's not what I'm writing about here.

In middle school English, I had a teacher named Rick Riordan. I loved his class. I don't remember what English-related material we covered, but I do have fond memories of learning all about Norse mythology and Japanese geography in that class, for reasons which elude me. Anyway, some years later, Rick struck it big: his book [Percy Jackson and the Lightning Thief](https://en.wikipedia.org/wiki/The_Lightning_Thief) was a huge hit and ended up being made into a movie. I heard about this at some point in college and was happy for Mr. Riordan, but never ended up reading the book or seeing the movie.

And so imagine my surprise when I googled Mr. Brunner and learned that he was a character in the book. He's Percy's Latin teacher. Pierce Brosnan plays him in the movie.

{% img brunner_normal.png width:700 height:298 %}

Except it turns out that Mr. Brunner is actually a centaur in disguise named Chiron.

{% img brunner_centaur.jpg width:467 height:300 %}

So that's what I think about when I think about Quinto.

[^1]: This is all computer programs.
[^2]: When I first heard about ClojureScript, I thought it sounded like a wacky idea. I am delighted to have been proven so completely wrong. If you also think that ClojureScript is a wacky idea, you might enjoy [this talk](https://www.youtube.com/watch?v=gsffg5xxFQI).
[^3]: The built-in version of `instrument` [does not verify that your `fdef`s' `:ret` type annotations are respected](https://www.reddit.com/r/Clojure/comments/7g4fl0/are_return_types_a_black_eye_for_clojure/dqglxv5/?context=3). [Orchestra](https://github.com/jeaye/orchestra) has a drop-in replacement for `instrument` that solves this problem nicely.
[^4]: Later on, when I was tracking down a few performance issues, I realized that one of these asserts was getting run in the bottom of a hot loop; moving the assert somewhere less sensitive fixed my performance problem. [Classic](https://thedailywtf.com/articles/The-Speedup-Loop).

{% javascript quinto %}
<script type="text/javascript">quinto.core.main()</script>
