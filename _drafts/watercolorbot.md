---
layout: post
title:  "Drawing Pictures and Making Games with a WaterColorBot"
---

I'm spending the 2017-18 school year volunteering in a few tech classes in a local high school. One of those classes is a beginner/intermediate Python course led by a teacher named Tamara Gray. It's her first time teaching Python, and I have a lot of experience in the language, so I've been helping her come up with [fun projects](http://blog.jrheard.com/python/passwords) for the students to work on.

When we started talking about potential projects, Tamara mentioned that she had a [watercoloring robot](http://watercolorbot.com/) that she'd like to have the students use somehow. She said she'd already had a lot of success using it in another intro-to-programming course via a block-based language called [Snap](https://github.com/evil-mad/WaterColorBlocks), but she wasn't sure how to talk to it via Python.

This sounded like a fun idea, so I looked into it. It turns out that there are [lot of great ways](http://wiki.evilmadscientist.com/WaterColorBot) to drive the bot via software, but I couldn't find anything Python-based that did what we wanted. I came up with a few possible approaches and asked [Windell Oskay](https://www.evilmadscientist.com/about/) for advice, and he kindly set us on the right track — thanks, Windell!

madison_wcb
-----------

I ended up writing a library called [`madison_wcb`](http://madison-wcb.readthedocs.io/en/latest/) to solve our problem. (This library was _extremely_ simple to write, thanks to the excellent ["Scratch API"](https://github.com/techninja/cncserver/blob/master/scratch/SCRATCH.API.md) that the WaterColorBot supports.)

The library lets students write code like this:

```python
# Dip the brush in the palette's top-most color.
get_color(0)

# Move to our origin point, face directly "south",
# and lower the brush so that it touches the paper.
move_to(100, 0)
point_in_direction(-90)
brush_down()

# Draw a circle!
for i in range(360):
	move_forward(2)
	turn_right(1)
```

If you've got a WaterColorBot lying around, you can use this library too! Just check out the [documentation](http://madison-wcb.readthedocs.io/en/latest/) and go nuts.

Here's what it looks like in action:

<div style='position:relative;padding-bottom:54%;margin-bottom:15px;'><iframe src='https://gfycat.com/ifr/ColdBigAzurevase' frameborder='0' scrolling='no' width='100%' height='100%' style='position:absolute;top:0;left:0' allowfullscreen></iframe></div>

The library uses Python's built-in [`turtle`](https://docs.python.org/3.3/library/turtle.html?highlight=turtle) module to let you see what your program will do when it runs on the bot, like so:

{% img wcb_turtle.gif %}

This feature saves a lot of paint!

...but why?
--------

In the grand scheme of things, this library is a pretty insane way to control the bot, because it's really low-level: you're manually controlling the brush's position, you've got to remember to wash it and re-ink the brush every so often, etc. If your main goal is to just get the bot to draw a pretty picture, there are lots of [better ways](http://wiki.evilmadscientist.com/WaterColorBot#Part_II:_Software_for_WaterColorBot) to go about it.

As a teaching aid, though, we've found this approach to be great! I've really been blown away by the stuff our students have created.

TODO put examples here

Interactivity
-------------

blat


Lessons Learned
---------------

working with physical object

paint gets muddy, we set aside a clean palette for known-good programs
