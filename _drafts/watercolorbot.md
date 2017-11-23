---
layout: post
title:  "Painting Pictures and Making Games with a Watercoloring Robot"
---

I'm spending the 2017-18 school year volunteering in a few tech classes in a local high school, including a beginner/intermediate Python course led by a teacher named Tamara O'Malley. She's new to Python, and I have a lot of experience with the language, so I've been helping her come up with [fun projects](http://blog.jrheard.com/python/passwords) for the students to work on.

When we started talking about potential projects, Tamara mentioned that she had a [WaterColorBot](http://watercolorbot.com/) that she'd like to have the students use in some way. She'd already had a lot of success using the bot in another intro-to-programming course via a block-based language called [Snap](https://github.com/evil-mad/WaterColorBlocks), but she wasn't sure how to talk to the bot via Python.

This sounded like a fun project, so I looked into it. It turns out that there are [lot of great ways](http://wiki.evilmadscientist.com/WaterColorBot#Part_II:_Software_for_WaterColorBot) to drive the bot via software, but I couldn't find anything Python-based that did what we wanted. I came up with a few possible approaches and asked [Windell Oskay](https://www.evilmadscientist.com/about/) for advice, and he kindly set us on the right track — thanks, Windell!

madison_wcb
-----------

I ended up writing a library called [`madison_wcb`](http://madison-wcb.readthedocs.io/en/latest/) to solve our problem. (This library was easy to write, thanks to the excellent and well-documented ["Scratch API"](https://github.com/techninja/cncserver/blob/master/scratch/SCRATCH.API.md) that the bot supports.)

The library lets students write code like this:

```python
# Dip the brush in the palette's top-most color.
get_color(0)

# Move the brush to the mid-right side of the page, "face" directly
# "south", and lower the brush so that it touches the paper.
move_to(100, 0)
point_in_direction(-90)
brush_down()

# Paint a circle!
for i in range(360):
	move_forward(2)
	turn_right(1)
```

If you've got a WaterColorBot lying around, you can use this library too! Just check out the [documentation](http://madison-wcb.readthedocs.io/en/latest/) or [source code](https://github.com/jrheard/madison_wcb) and go nuts.

Here's one student's program in action:

<div style='position:relative;padding-bottom:54%;margin-bottom:15px;'><iframe src='https://gfycat.com/ifr/ColdBigAzurevase' frameborder='0' scrolling='no' width='100%' height='100%' style='position:absolute;top:0;left:0' allowfullscreen></iframe></div>

The library also uses Python's built-in [`turtle`](https://docs.python.org/3.3/library/turtle.html?highlight=turtle) module to show you what your program will do.

{% img wcb_turtle.gif %}

This saves users a lot of potential frustration, and also a bunch of paint.

Perhaps Somewhat Impractical
--------

To be honest, this library is a pretty insane way to control the bot. It's needlessly low-level: you're manually controlling the brush's position, you've got to remember to wash and re-ink the brush every so often, etc. If your main goal is to just get the bot to paint a pretty picture, there are lots of [better ways](http://wiki.evilmadscientist.com/WaterColorBot#Part_II:_Software_for_WaterColorBot) to go about it.

As a teaching aid, though, it's been a total success, because it lets students flex their burgeoning Python skills and actually make a real thing in the process! We've been blown away by the stuff our students have created. Here's an N64 logo in seven hundred and fifty hand-crafted lines of Python:

{% img wcb_1.JPG %}

This clock depicts the time at which the program was run:

{% img wcb_2.JPG %}

This student drew an image from scratch in Paint or something, using straight lines and simple curves, and then translated it into Python:

{% img wcb_3.JPG %}

And here's a nice windowsill cat.

{% img wcb_4.JPG %}

These kids haven't learned how to use lists/dicts or write functions yet, and they're already making cool programs like these!

Interactivity
-------------

Once I finished writing the library, I thought it might be fun to use the bot as a "display" for a video game. As a proof of concept, I wrote an embarrassingly basic [text adventure](https://github.com/jrheard/waterventure/blob/master/waterventure.py) that uses the bot as a mini-map, painting in new rooms as you wander around the game world.

{% img waterventure.gif %}

My favorite part about it is that once you've beaten the game, you end up with a completed map: a (slightly splotched) physical artifact that serves as proof of your victory.

{% img waterventure.jpg width:740 height:510 %}

If you're interested in making a game that runs on a watercoloring robot, here are some design constraints to keep in mind:
* You've got an _extremely_ finite amount of screen real estate (one page of printer paper)
* If you want to e.g. start a new page every level (maybe you're writing a dungeon-crawler?), the user has to fiddle with the machine for ten seconds to take off the old page and ensure there's a fresh page ready to go, which could get irritating over time
* You probably don't want to paint on the same "pixel" twice (although I can imagine situations where an intentionally smudged page could make for a cool aesthetic)

Anyway, I thought the idea of an interactive watercolor program was interesting, so I showed the text adventure to the students. A few of them liked the idea and made their projects interactive too. Here's one student's Minesweeper:

TODO gif of zach's program

This student has never used a two-dimensional array before, and he wrote a fully-functioning version of Minesweeper that runs on a watercoloring robot. I probably don't need to point out that this is **insanely cool**.

Here's another student's implementation of Go:

TODO gif of jake's program

So cool.

Lessons Learned
---------------

I've been programming for a long time, but this was my first time writing code that controls a physical object. At first I was worried that a bug in my library could e.g. cause the three-hundred-dollar bot to rip itself apart, but Windell assured me that the bot's "Scratch API" handles bounds checking automatically, and so that's turned out not to be an issue.[^1]

One thing we didn't foresee was that our paints kept getting dirty, because students' rough-draft programs often didn't wash the brush frequently enough — for instance, you may have noticed that the solar system program from earlier in this article depicts an unusually brown sun. We went through a few palettes before solving this problem by setting aside a "production" palette, which we only swap in when we're painting a student's known-good, final-draft program.[^2]

That's All For Now
------------------
We've still got plenty of school year left, and I can't wait to see what crazy antics these kids get up to in future projects!

BTW: If you're a programmer interested in volunteering in a high school coding class, check out [TEALS](https://www.tealsk12.org/), it's how I originally got involved with this school.

[^1]: If `madison_wcb` _does_ kill your bot, I'm very sorry. Use at your own risk 😕

[^2]: I can't find the exact quote, but when I mentioned this in my friends' [IRC channel](https://irc.darwin.network/), one of them had a quip like "good programmers always separate stage and production".
