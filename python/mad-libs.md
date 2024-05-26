---
layout: page
title:  "Madison CS 3-4: Mad Libs"
---

Welcome to your first project in CS 3-4!

In this project, you'll be writing a program that lets the user fill in a [mad lib](https://en.wikipedia.org/wiki/Mad_Libs#Format). When you're done, your program will look something like this:

<asciinema-player src="{{ site.baseurl }}/madlib.json" rows="10" cols="90" autoplay="true" loop="true"></asciinema-player>

My mad lib script isn't very good, though - you should write a better one!


Starter Code
============

This project comes with some starter code to get you started. Download [this file][starter-code] and open it in IDLE.

The starter code comes with a `mad_lib()` function - that's where your code should go.

The starter code has some comments with the word TODO in them, which are just reminders about what you're supposed to do. Delete those comments once you've done the things that they tell you to do.

Requirements
============

Your program should prompt the user for __at least five words__ and then plug them into a mad-lib script you've written. If you'd like to write a longer mad-lib, go ahead and prompt the user for lots more words!

Remember: here's how to use the `input()` function to ask the user for a string of text and then save that string to a variable:

<textarea class="hidden">
word = input("I would like one word, please: ")
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

Submitting your project
=======================

Submit a file called `mad_lib_YOUR_NAME.py`. For example, I'd submit a file called `mad_lib_jr_heard.py`.

On the first line of that file, write a comment with your name on it, like this:

```
# JR Heard
```


A Suggestion
==========

You're probably going to end up writing a lot of code like this:

<textarea class="hidden">
adjective = input("Please give me an adjective: ")
noun = input("Please give me a noun: ")
animal = input("Please give me an animal: ")
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

That can get pretty repetitive. If you want to make this feel a little less gross, you can write a function like this:

<textarea class="hidden">
def get_word(kind_of_word):
    return input("Please give me " + kind_of_word + ":")
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

Then you can use that function in your code like this:

<textarea class="hidden">
adjective = get_word("an adjective")
noun = get_word("a noun")
animal = get_word("an animal")
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

I like this better because it means that I don't have to type out `"Please give me a <something>:"` every time.

You don't have to do this `get_word()` thing, but you can if you want to!


[starter-code]: {{site.baseurl}}/python/mad_lib_starter_code.py

<script src="{{ site.baseurl }}/assets/js/asciinema-player.js"></script>


<script src="{{ site.baseurl }}/assets/js/codemirror.js"></script>
<script src="{{ site.baseurl }}/assets/js/codemirror_python.js"></script>
<script src="{{ site.baseurl }}/assets/js/codemirror_runmode.js"></script>
<script>
var textAreas = document.getElementsByTagName("textarea");
var pres = document.querySelectorAll("pre.cm-s-friendship-bracelet");

for (var i = 0; i < textAreas.length; i++) {
	CodeMirror.runMode(textAreas[i].value, "python", pres[i]);
}
</script>
