---
layout: post
title:  "Getting High Schoolers To Write A Tiny 'Roguelike' In An Intro Python Class"
---

I spent the past couple years volunteering in a couple of tech classes at a local high school, primarily in an introductory Python class led by an excellent teacher named Tamara O'Malley. I've written about this a [few](https://blog.jrheard.com/watercolorbot) [times](https://blog.jrheard.com/hypothesis-and-pexpect) [before](https://blog.jrheard.com/truthiness-and-short-circuit-evaluation-in-python). [^1] It was really, really fun, and it still hasn't really sunk in that it's over now.

Anyway, the students in this Python class were beginners - they had all had some exposure to programming before in block-based languages like [Snap!](https://snap.berkeley.edu/), but none of them had taken AP CS yet, to give you an idea of where they were at experience-wise.

As one of the final projects of the year, we had them write a little roguelike.[^2] We gave them some [starter code](https://repl.it/@jrheard/roguelike) and one of my usual [project writeups](https://blog.jrheard.com/python/roguelike) and turned them loose.

This is what the starter code does when you run it:

<asciinema-player src="{{ site.baseurl }}/roguelike_starter.json" rows="32" cols="90" autoplay="true" loop="true"></asciinema-player>

You're the @ sign, you can move around, you can't go through walls. Great game, right?

We had the kids start by changing my terrible controls to be WASD-based, which turned out to be a good way for them to get their bearings - this was their first time being dumped into a (tiny) legacy codebase, and having to change the controls forced them to read the code and figure out where the relevant moving parts were.

After that, we walked them through how to add a "[goal space](https://blog.jrheard.com/python/roguelike#adding-a-goal-space)" that ends the game if you get to it, then showed them how to add some [dumb monsters](https://blog.jrheard.com/python/roguelike#implementing-dumb-monsters) that just sit there and don't do anything. Once they had done that, we were like: okay, now make a game!

Here's some of the cool stuff they made.

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

King Of The Thing
-----------------

This one's great. The levels are pretty big, so this is going to take up most of your screen, but it's so cool that I couldn't not include it.

You're the `☻`, the `∩`s are harmless barrels that you effortlessly smash through, the `r`s are rats, the `g`s are goblins. You can kill the rats and goblins, but it's hard and you take a lot of damage doing it. If you pick up a `†`, though, now you have a dagger and can wreck 'em easily!

Once you make it to the next level, you can pick up a `✟` (sword) to really boost your damage, and if your HP is low after fighting some goblins you can chug a `✚` (health potion) to heal up. Be careful of the `✠` you'll pass on your way to the next floor of the dungeon - it's a chainsaw, and if you touch it, you'll die!

After that, it's time to fight the big boss himself: you've gotta beat the king and take his crown! I love how this third level is structured, it's so simple but somehow, like, evocative. It starts with a traditional ammo room so you just _know_ you're about to fight a scary boss, and I love the little corridor you have to squeeze through to get to the king - I actually got kinda scared on my way through it to fight the king.

<asciinema-player src="{{ site.baseurl }}/roguelike_king_thing.json" rows="45" cols="90" autoplay="true" loop="true"></asciinema-player>

Favorite parts: the little heart in the congratulations message, and also the `Kings Killed: 0` output in the HUD. So good.

Backing Up A Bit
----------------

This do-whatever-you-want approach was super different from what we had done in previous projects. Before this project, these kids had built:

* [mad libs](https://blog.jrheard.com/python/mad-libs)
* [a guess-my-number game](https://blog.jrheard.com/python/guess-my-number)
* [generated art with a pen plotter](https://blog.jrheard.com/python/plotter)
* [a password generator](https://blog.jrheard.com/python/password-generator)
* [a password strength checker](https://blog.jrheard.com/python/password-checker)
* [a caesar cipher program](https://blog.jrheard.com/python/caesar)
* [tic-tac-toe](https://blog.jrheard.com/python/tic-tac-toe)
* [blackjack](https://blog.jrheard.com/python/blackjack)

All of these projects (except the generated art one) had a rigorous spec: we gave them some extremely minimal starter code, showed them what the finished program should look like, gave them some hints about how to write it, and that was it - their task was to write a program that implemented the spec.[^3]

For this roguelike thing, there wasn't a spec at all! We had them play a little [Brogue](https://sites.google.com/site/broguegame/) to give them some ideas and then sat back and waited to see what would happen.

What Happened
-------------

Going into the project, I was kinda nervous! What if they got bored or thought the assignment was dumb?

Surprise: they loved it, it was great, definitely one of the best projects of the year. Kids love playing around and making weird stuff. Let me show you some of the stuff they made.


[^1]: I was originally placed in this high school through an organization called [TEALS](https://www.tealsk12.org/), which is accepting applications for the coming school year, so you should apply if this sounds like fun. It _is_ fun!

[^2]: Okay, okay, these games aren't anywhere near sophisticated enough to be called roguelikes, don't @ me. They use ASCII art and the player (usually) explores a dungeon, it's close enough.

[^3]: Don't worry, they were free to experiment and do crazy extensions once they had finished the basic program - some kids implemented complicated betting systems in their blackjack games, that sort of thing.

{% javascript asciinema-player %}
