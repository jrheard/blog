---
layout: page
title:  "Madison CS 3-4: Generated Art with a Pen Plotter"
---

In this project, you'll learn how to install and use a Python library to write a program that generates cool art that can be drawn on a pen plotter.

What's a pen plotter?
=====================

A pen plotter's an electronic gadget that holds a pen and draws stuff with it. The particular pen plotter we'll be using is called an [AxiDraw](http://axidraw.com), and it looks like this:

{% img axidraw.jpg width:720 height:540 %}

The basic idea is that the device holds a pen, we put a piece of paper under the pen, and you write a computer program that tells the plotter to move the pen around so that it draws stuff on the piece of paper.

If you've used the [WaterColorBot]({{site.baseurl}}/watercolorbot), this is a lot like that - except it's simpler, because you don't have to worry about writing code to wash the brush and dip it in different kinds of paint!

Getting Started
===============

I've written a library called `madison_axi` that'll let you write Python code to control our classroom's plotter. When you run your program on _your_ computer, it'll draw a preview of what you can expect to see on the plotter; once that preview looks the way you want it to, you can submit your program and we'll run it on the plotter for you.

Start by reading the library's [QuickStart guide](https://madison-axi.readthedocs.io/en/latest/quickstart.html). Read the example program on that page and make sure you understand it. There are [some more example programs](https://github.com/jrheard/madison_axi/tree/master/madison_axi/examples) if you want to read those too - `spiky_circle.py` is my favorite, try running it on your computer later on once you're all set up.

When you run a program that uses this library, you'll see a window appear on your screen, and it'll draw a preview of what your program would do on the plotter. The window is a particular size, and I did that on purpose: **make sure that your program doesn't draw stuff outside the bounds of that window**, or otherwise it won't get drawn on the plotter's piece of paper. Don't resize the window - you can move it around on your screen, just don't change its size.

If your program draws stuff within the bounds of the demo window, that stuff'll appear on the plotter's piece of paper; if your program tries to go outside the window, that'll make the plotter try to draw stuff outside of the piece of paper, and that's no good.

**NOTE:** In order to install the library on your classroom computer, you'll need to run `pip install --user madison_axi` at the command line. If you don't include the `--user` in there, it won't work.

**NOTE:** You should call `initialize()` at the start of your program and `cleanup()` at the end of it.

How to use the library
======================

Start by importing it, like this:

<textarea class="hidden">
from madison_axi import axi
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

After that, you can call functions from the library like this:

<textarea class="hidden">
# Remember: you MUST call initialize() at the start of your program.
axi.initialize()

# Move to the middle of the page, point to the right,
# make the pen touch the page, and go forward a little.
axi.move_to(0, 0)
axi.point_in_direction(0)
axi.pen_down()
axi.move_forward(50)

# Be sure to call cleanup() at the end of your program.
axi.cleanup()
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

Controlling the plotter is a lot like controlling a turtle - the library gives you access to functions with like `turn_right(45)`, `turn_left(90)`, `move_forward(100)`, etc. This will feel very familiar from previous assignments.

[This page](https://madison-axi.readthedocs.io/en/latest/madison_axi.html) has a list of all of the functions that the library gives you. Read the whole page, there aren't very many functions. You can probably ignore `get_position()`, `get_y()`, and `get_x()`, but I bet you'll use all of the other ones.


Requirements
============

* You must define at least one function that takes some inputs. For example, you could make a function like `draw_box(x, y)` that draws a box at a particular location, or `draw_circle(x, y)`, etc. You can make as many functions as you want, and they can do whatever you want - just make sure that you have at least one function that takes inputs.
* You are **strongly encouraged** to use randomness somehow in your program. Make a program that randomly draws circles of random sizes, that'd be cool! Just make sure that the program stays within the bounds of the demo window like I mentioned earlier.


Submitting
==========

TODO tomalley please advise


Advanced
========

TODO jrheard mention minesweeper, plotterventure










{% javascript codemirror %}
{% javascript codemirror_python %}
{% javascript codemirror_runmode %}
<script>
var textAreas = document.getElementsByTagName("textarea");
var pres = document.querySelectorAll("pre.cm-s-friendship-bracelet");

for (var i = 0; i < textAreas.length; i++) {
	CodeMirror.runMode(textAreas[i].value, "python", pres[i]);
}
</script>
