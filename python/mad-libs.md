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


[starter-code]: {{site.baseurl}}/python/mad_lib_starter_code.py

{% javascript asciinema-player %}


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
