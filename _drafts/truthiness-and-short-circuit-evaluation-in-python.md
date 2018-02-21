---
layout: post
title:  "Truthiness and Short-Circuit Evaluation in Python"
---

<style>
.target-audience {
	background-color: #EEE;
	font-family: sans-serif;
	padding: 5px 10px;
	margin: -20px 0 20px;
	display: inline-block;
	font-size: 15px;
	font-weight: bold;
}
</style>

<div class="target-audience">
Target audience: beginner programmers
</div>

In the [high school Python class][wcb] I'm helping out with, I've noticed that students will often write a chunk of code that looks like this:

<textarea class="hidden">
num = int(input())

if num == 5 or 6 or 7:
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

In this example, the student has a `num` variable whose value is some integer, and they're trying to write some code that gets run if the integer is `5` or `6` or `7`. The code snippet above seems reasonable at first glance, but it actually does something **completely different** from what the student would expect.

Let's forget the `if:` part of the code for now and focus on the `num == 5 or 6 or 7` part. Here's what Python sees when you write that:

<div class="boolean-diagram">
<div class="expression">num == 5</div>
<div class="conjunction">or</div>
<div class="expression">6</div>
<div class="conjunction">or</div>
<div class="expression">7</div>
</div>

I'm going to be using a lot of diagrams like this throughout this post. In these diagrams, a yellow box is a **chunk of code that Python hasn't evaluated yet**. ("Evaluated" basically means "run".)

Notice how the first yellow box in our expression is

<div class="boolean-diagram"><div class="expression">num == 5</div></div>

and the second box is

<div class="boolean-diagram"><div class="expression">6</div></div>

The second box isn't `num == 6`—it's **just `6`**. That's kind of weird! What does the number `6` do if you put it in an `if` statement? Read on to find out!

Okay, let's take one more look at the chunk of code we're trying to decipher:

<textarea class="hidden">
num == 5 or 6 or 7
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

Let's start by figuring out what this code does when the `num` variable has the value `10`. Python starts by evaluating `10 == 5`, which turns into `False`.

<div class="boolean-diagram">
<div class="expression falsey">False</div>
<div class="conjunction">or</div>
<div class="expression">6</div>
<div class="conjunction">or</div>
<div class="expression">7</div>
</div>

So at this point, our partly-evaluated expression is `False or 6 or 7`, and Python has to figure out whether or not that whole thing ends up evaluating to `True`, because we're running this code as the condition part of an `if` statement.

What does Python do when it sees that weird-looking `False or 6 or 7` expression? In order to answer that question, we'll need to know about **truthiness** and **short-circuiting**.

# Truthiness

You're familiar with the values `True` and `False`. We call them "Booleans", and we use them most often in `if` statements.

<pre class="dont-format-output"><code class="py">
hungry = True

if hungry:
	print('try eating a slice of pizza')
else:
	print('must be nice')
</code></pre>

Python doesn't limit us to just using `True` and `False` in `if` statements, though—you can put _any_ expression in there. If you put something in an `if` statement's condition and it's not `True` or `False`, Python will look at it and decide whether or not it's "truthy".

According to the [official documentation](https://docs.python.org/3/library/stdtypes.html#truth-value-testing), everything in Python is considered truthy except for these things:

* `False`
* `None`
* `0`
* Empty sequences, e.g. `[]`, `''`, `()`, `{}`

You can use the built-in `bool()` function to see if something is truthy. Here are some examples:

<pre><code class="py">
print(bool(True))
print(bool(False))
print(bool('cat'))
print(bool([]))
print(bool(['pizza', 'tacos']))
</code></pre>

That code snippet is interactive, so go ahead and mess around with those examples to convince yourself that you understand how truthiness works. Is `15` truthy?

Now that we know what truthiness is, let's talk about short-circuit evaluation.

# Short-Circuit Evaluation

The `and` and `or` operators in Python are [short-circuit operators](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not). To see what this means, let's look at an example use of the `or` operator.

<textarea class="hidden">
1 == 1 or 1 == 2
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

This is what Python sees:

<div class="boolean-diagram">
<div class="expression">1 == 1</div>
<div class="conjunction">or</div>
<div class="expression">1 == 2</div>
</div>

Remember that if a box is yellow, that means that Python hasn't evaluated it yet.

When Python sees this line of code, it evaluates each of the yellow boxes in order until it finds one that's truthy. It starts by evaluating `1 == 1`, which turns into `True`.

<div class="boolean-diagram">
<div class="expression truthy">True</div>
<div class="conjunction">or</div>
<div class="expression">1 == 2</div>
</div>

At this point, Python stops! That's what short-circuiting means. Here's how the official documentation describes `or`'s behavior:

> it only evaluates the second argument if the first one is false.

Here, I'll prove it to you. First, it's important to know that if you divide a non-zero number by zero, Python will throw an exception:

<pre><code class="py">
1 / 0
</code></pre>

Now, check out what happens if I put a `1 / 0` _after_ a truthy thing in an `or`:

<pre><code class="py">
print(True or 1 / 0)
</code></pre>

The program prints `True` and exits **without evaluating the `1 / 0`**! To convince yourself that this works the way I claim it does, try changing that `True` to a `False`.

This matches the behavior we saw in the diagram above—remember how the `1 == 2` box stayed yellow to indicate that Python hadn't evaluated (run) the code inside of it.

`and` works similarly to `or`, except that the official documentation says that

> it only evaluates the second argument if the first one is true.

Here are more examples that show how `and` and `or`'s short-circuiting behavior works. Do they all behave the way you expect?

<div class="boolean-diagram">
<div class="expression falsey">1 == 2</div>
<div class="conjunction">and</div>
<div class="expression">2 == 2</div>
</div>

<div class="boolean-diagram">
<div class="expression truthy">1 == 1</div>
<div class="conjunction">and</div>
<div class="expression falsey">1 == 2</div>
</div>

<div class="boolean-diagram">
<div class="expression truthy">1 == 1</div>
<div class="conjunction">and</div>
<div class="expression truthy">2 == 2</div>
</div>

<div class="boolean-diagram">
<div class="expression falsey">1 == 2</div>
<div class="conjunction">or</div>
<div class="expression truthy">1 == 1</div>
</div>


# Back to our buggy buggy `num` code

Now that we know what truthiness is, we can figure out how this expression is evaluated when `num` has the value `10`.

<div class="boolean-diagram">
<div class="expression">num == 5</div>
<div class="conjunction">or</div>
<div class="expression">6</div>
<div class="conjunction">or</div>
<div class="expression">7</div>
</div>

Python is going to look at these yellow boxes and evaluate them, one at a time, until it finds one that's truthy.

Python starts by looking at the `num == 5`—and like we saw before, that evaluates to `False`, which is not truthy. I'll mark that box as red to indicate that Python has evaluated it and determined that it's falsey.

<div class="boolean-diagram">
<div class="expression falsey">num == 5</div>
<div class="conjunction">or</div>
<div class="expression">6</div>
<div class="conjunction">or</div>
<div class="expression">7</div>
</div>

Next up, Python looks at `6`. We learned earlier that `0` is falsey, and all other numbers are truthy. `6` is a number and it's not `0`, so it's truthy. If you don't believe me, here's another interactive code snippet that proves it:

<pre><code class="py">
print(bool(6))
</code></pre>

So, great, we've determined that `6` is truthy! Now our expression looks like this:

<div class="boolean-diagram">
<div class="expression falsey">num == 5</div>
<div class="conjunction">or</div>
<div class="expression truthy">6</div>
<div class="conjunction">or</div>
<div class="expression">7</div>
</div>

I said earlier that Python is going to look at our yellow boxes and evaluate them, one at a time, until it finds one that's truthy. Well, **it's found one that's truthy**! What happens now?

# Short-circuiting

What happens now is that Python stops, because it's job is done! It says "hey, I found a truthy thing", and 


<pre><code class="py">
num = 10

print(num == 5 or 6 or 7)
</code></pre>

Here are a few more examples:

<pre><code class="py">
print(False or 2)
print(2 or False)
print(False or 0 or "hello")
</code></pre>


<pre><code class="py">
print(False or 0)
</code></pre>




outline (not in particular order)

students write code like `num == 5 or 6 or 7`

that doesn't do what they think it does; they should write `num == 5 or num == 6 or num == 7` instead, or better yet `num in [5, 6, 7]`, or `5 <= num <= 7`

maybe make some diagrams
you want to show that python looks at each of the parts of the statement in isolation
so like in `num == 5 or 6 or 7`, highlight each part

talk about truthiness

TODO: `num == (5 or 6 or 7)` won't do what the student wants, either. knowing what you know now, can you figure out what that code actually does?

notes

* wikipedia page https://en.wikipedia.org/wiki/Short-circuit_evaluation
    * "when the first argument of the AND function evaluates to false, the overall value must be false; and when the first argument of the OR function evaluates to true, the overall value must be true"
* official docs https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
    * "This is a short-circuit operator, so it only evaluates the second argument if the first one is false."
	* "This is a short-circuit operator, so it only evaluates the second argument if the first one is true."
* https://stackoverflow.com/a/14892812 good stackoverflow answer
* this is good too https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Boolean_Expressions

* https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_Operators tons of examples

# Resources

* https://gist.github.com/jfarmer/2647362

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
