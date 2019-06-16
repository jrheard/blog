---
layout: post
title:  "Getting High Schoolers To Write A Tiny 'Roguelike' In An Intro Python Class"
---

I spent the past couple years volunteering in a couple of tech classes at a local high school, primarily in an introductory Python class led by an excellent teacher named Tamara O'Malley. I've written about this a [few](https://blog.jrheard.com/watercolorbot) [times](https://blog.jrheard.com/hypothesis-and-pexpect) [before](https://blog.jrheard.com/truthiness-and-short-circuit-evaluation-in-python).[^1] It was extremely fun, and it still hasn't really sunk in that it's over now.

The students in this Python class were beginners - they had all done some programming in block-based languages like [Snap!](https://snap.berkeley.edu/), but none of them had taken AP CS yet, to give you an idea of where they were at experience-wise.

As one of the final projects of the year, we had them write a little roguelike (a term with many definitions, which here I'm using to mean "a game where you're an `@` sign and you wander around an ASCII art world"). We gave them some [starter code](https://repl.it/@jrheard/roguelike) and one of my usual [project writeups](https://blog.jrheard.com/python/roguelike) and turned them loose.

This is what the starter code does when you run it:

<asciinema-player src="{{ site.baseurl }}/roguelike_starter.json" rows="32" cols="90" autoplay="true" loop="true"></asciinema-player>

You're the @ sign, you can move around, you can't go through walls. Great game, right?

We had the kids start by changing my terrible controls to be WASD-based, which turned out to be a good way for them to get their bearings - this was their first time being dumped into a (tiny) legacy codebase, and having to change the controls forced them to read the code and figure out where the relevant moving parts were.

After that, we walked them through how to add a [goal space](https://blog.jrheard.com/python/roguelike#adding-a-goal-space) that ends the game if you get to it, then showed them how to add some [dumb monsters](https://blog.jrheard.com/python/roguelike#implementing-dumb-monsters) that just sit there and don't do anything. Once they had done that, we were like: okay, now make a game!

Here's some of the cool stuff they made!
========================================

Coin Getter
----------

You're the smiley face, you want to get to the X, but there's a door blocking the way to it - the door doesn't open until you get all the coins first.

<asciinema-player src="{{ site.baseurl }}/roguelike_coin_getter.json" rows="34" cols="90" autoplay="true" loop="true"></asciinema-player>

The program uses the © symbol for its coins, and so when we were having the kids demo each other's games on the projector at the end of the project, some kid in the peanut gallery shouted "if you get all five copyright strikes, your channel gets taken down!".

I thought that was pretty good.

Bait-And-Switch
---------------

In this one, you're the `Ö`, the `Ӂ`s are enemy squids, the `ᵹ`s are health potions, and your goal is to get to the next level, which is too big to fit on this page so I'll just show you the first level.

The squids don't do anything, but notice how if you pick up a health potion, your health increases!

If you pick up the second health potion, though, your health _decreases_. This puzzled me for a bit, but I pieced it together - if you pick up the farthest-down health potion on the level, the game gets confused and thinks it's a health potion and _also_ a monster, and so it increments your health by 10 but then decrements it by 20 because that's what bumping into a squid is supposed to do. Interesting little bug.

<asciinema-player src="{{ site.baseurl }}/roguelike_bait_and_switch.json" rows="30" cols="90" autoplay="true" loop="true"></asciinema-player>

This game has a little trick to it - the door to the next level is actually the `▐`, but if you get confused and hit the `+` instead, the game insults you in big ASCII art and unceremoniously exits. I love it.

King Of THING
-----------------

You're the `☻`, the `∩`s are harmless barrels that you effortlessly smash through, the `r`s are rats, the `g`s are goblins. You can kill the rats and goblins, but it's hard and you take a lot of damage doing it because you start off with really low attack power. If you pick up a `†`, though, now you have a dagger and can wreck 'em easily!

Once you make it to the next level, you can pick up a `✟` (sword) to really boost your damage, and if your HP is low after fighting some goblins you can chug a `✚` (health potion) to heal up. Be careful of the `✠` you'll pass on your way to the next floor of the dungeon - it's a chainsaw, and if you touch it, you'll die!

After that, it's time to fight the big boss himself: you've gotta beat the king and take his crown! I love how this third level is structured, it's so simple but somehow, like, evocative. It starts with a traditional ammo room so you just _know_ you're about to fight a scary boss, and I love the little corridor you have to squeeze through to get to the king - I actually got kinda scared on my way through it. It felt like anything could happen!

<asciinema-player src="{{ site.baseurl }}/roguelike_king_thing.json" rows="37" cols="90" autoplay="true" loop="true"></asciinema-player>

Favorite parts:
* The little heart in the congratulations message
* `Kings Killed: 0`

A-Maze-Ing
----

Look, I didn't come up with these names, it's not my fault.

<asciinema-player src="{{ site.baseurl }}/roguelike_maze.json" rows="30" cols="90" autoplay="true" loop="true"></asciinema-player>

I think I have RSI now.

Soccer
------

One kid made the starter code into a soccer game!

You're the `%`, the `$` is the AI enemy player and it chases the ball, the `@` is the ball, and when you kick the ball there's some randomness involved so sometimes you find yourself chasing after it and trying to get there before the AI does.

<asciinema-player src="{{ site.baseurl }}/roguelike_soccer.json" rows="38" cols="90" autoplay="true" loop="true"></asciinema-player>

Other Cool Projects We Did This Year
------------------------------------

Here are all the projects I put together for this class, in increasing order of difficulty. They start off assuming basically zero knowledge of Python, and slowly require more and more over time as the students learn about if-statements, loops, lists, etc.

* [Mad Libs](https://blog.jrheard.com/python/mad-libs)
* [A guess-my-number game](https://blog.jrheard.com/python/guess-my-number)
* [Generated art with a pen plotter](https://blog.jrheard.com/python/plotter)
* [A password generator](https://blog.jrheard.com/python/password-generator)
* [A password strength checker](https://blog.jrheard.com/python/password-checker)
* [A Caesar cipher program](https://blog.jrheard.com/python/caesar)
* [Tic-Tac-Toe with an AI opponent](https://blog.jrheard.com/python/tic-tac-toe)
* [Blackjack against an AI dealer](https://blog.jrheard.com/python/blackjack)
* [Roguelike](https://blog.jrheard.com/python/roguelike) ([starter code](https://repl.it/@jrheard/roguelike))

I put a lot of time into these over the course of two years, and I'm really proud of how they turned out. Many many thanks to Tamara for her help and feedback.

If you'd like to use these projects in a classroom or for practice on your own, please feel free! Hit me up at jrrrheard@gmail.com if you have questions or want me to review your code, I'd be delighted to hear from you.


What's Next For Me
------------------

This has been a really great time, but I feel like having a regular job again and having coworkers to hang out with, so I'm joining [Ride Report](https://www.ridereport.com/) as a senior engineer. They offered me the job back in April, and were kind enough to let me finish out the school year before my start date.

I've been looking forward to this for a while, it's going to be fun and I'm going to learn a lot. Down with cars!


[^1]: I was originally placed in this high school through an organization called [TEALS](https://www.tealsk12.org/). They're accepting applications for the coming school year, so you should apply if this sounds like fun. It _is_ fun!

{% javascript asciinema-player %}
