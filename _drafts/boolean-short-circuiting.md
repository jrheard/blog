---
layout: post
title:  "Boolean Short-Circuiting in Python"
---

<style>
.target-audience {
	background-color: #EEE;
	font-family: sans-serif;
	padding: 10px;
	margin: -20px 0 20px;
	display: inline-block;
	font-size: 15px;
}
</style>

<div class="target-audience">
Target audience: beginner programmers
</div>

In the [high school Python class][wcb] I'm helping out with, I've noticed that students often write code like this:

<textarea class="hidden">
num = int(input())

if num == 5 or 6 or 7:
	# do something
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

In this example, the student has a `num` variable whose value is some integer, and they'd like to write some code that checks whether the integer is `5` or `6` or `7` or none of those numbers. The code they wrote seems reasonable at first glance, but it actually does something completely different from what the student would expect.

Let's forget the `if:` part of the code for now and focus on the `num == 5 or 6 or 7` part. Here's what Python sees when you give it that code:

<div class="boolean-diagram">
<div class="expression">num == 5</div>
<div class="conjunction">or</div>
<div class="expression">6</div>
<div class="conjunction">or</div>
<div class="expression">7</div>
</div>

It looks at each of those yellow boxes, each one by itself, one at a time: first the `num == 5`, then the `6`, then the `7`. It looks at each one of those until it finds one that's "truthy".

# Truthiness

You're familiar with the values `True` and `False`. We call them "Booleans", and we use them in `if` statements all the time.

<pre class="dont-format-output"><code class="py">
hungry = True

if hungry:
	print('try eating a slice of pizza')
else:
	print('must be nice')
</code></pre>

Python doesn't just limit us to using `True` and `False` in `if` statements, though—you can put _anything_ in there, and that's where the concept of "truthiness" comes in.

According to the [official documentation](https://docs.python.org/3/library/stdtypes.html#truth-value-testing), these things are "considered false":

* `False`
* `None`
* `0`
* Empty sequences, e.g. `[]`, `''`, `()`, `{}`

Everything else is "considered true", a.k.a. "truthy".

You can use the built-in `bool()` function to see if something is truthy. Here are some examples:

<pre><code class="py">
print(bool(True))
print(bool(False))
print(bool('cat'))
print(bool([]))
print(bool(['pizza', 'tacos']))
</code></pre>

That code snippet is interactive, so go ahead and mess around with those examples to convince yourself that you understand how truthiness works. Is `15` truthy?

# Back to our example

TODO red, green boxes





outline (not in particular order)

students write code like `num == 5 or 6 or 7`

that doesn't do what they think it does; they should write `num == 5 or num == 6 or num == 7` instead, or better yet `num in [5, 6, 7]`, or `5 <= num <= 7`

maybe make some diagrams
you want to show that python looks at each of the parts of the statement in isolation
so like in `num == 5 or 6 or 7`, highlight each part

talk about truthiness

notes

* wikipedia page https://en.wikipedia.org/wiki/Short-circuit_evaluation
    * "when the first argument of the AND function evaluates to false, the overall value must be false; and when the first argument of the OR function evaluates to true, the overall value must be true"
* official docs https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
    * "This is a short-circuit operator, so it only evaluates the second argument if the first one is false."
	* "This is a short-circuit operator, so it only evaluates the second argument if the first one is true."
* https://stackoverflow.com/a/14892812 good stackoverflow answer
* this is good too https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Boolean_Expressions

* https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_Operators tons of examples

* official docs on python truthiness https://docs.python.org/3/library/stdtypes.html#truth-value-testing

* essay on truthy/falsey https://gist.github.com/jfarmer/2647362

<pre><code class="py">
True or  5 / 0
</code></pre>



[wcb]: {{site.baseurl}}{% post_url 2017-11-30-watercolorbot %}



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

<script>
window.klipse_settings = {
	selector_eval_python_client: '.py',
	codemirror_options_in: {
		theme: "friendship-bracelet"
	},
	codemirror_options_out: {
		theme: "friendship-bracelet"
	}
};
</script>
{% javascript klipse.min %}
