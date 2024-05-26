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

Let's focus on the `num == 5 or 6 or 7` part, because that's the part that isn't doing what the student expects. Here's what Python sees when you write that code:

<div class="boolean-diagram">
<div class="expression">num == 5</div>
<div class="conjunction">or</div>
<div class="expression">6</div>
<div class="conjunction">or</div>
<div class="expression">7</div>
</div>

I'm going to be using a lot of diagrams like this throughout this article. In these diagrams, a yellow box is a **chunk of code that Python hasn't evaluated yet**. ("Evaluated" basically means "run".)

Notice how the first yellow box in that diagram is

<div class="boolean-diagram"><div class="expression">num == 5</div></div>

and the second box is

<div class="boolean-diagram"><div class="expression">6</div></div>

That second box isn't `num == 6`—it's **just `6`**. That's kind of weird! What does the number `6` do if you put it in an `if` statement? Read on to find out!

OK, so we're trying to decipher this code:

<textarea class="hidden">
num == 5 or 6 or 7
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

Let's start our analysis by figuring out what that code does when the `num` variable has the value `10`.

Python starts by evaluating `10 == 5`, which turns into `False`.

<div class="boolean-diagram">
<div class="expression falsey">False</div>
<div class="conjunction">or</div>
<div class="expression">6</div>
<div class="conjunction">or</div>
<div class="expression">7</div>
</div>

So at this point, our partly-evaluated expression is `False or 6 or 7`, and Python has to figure out whether or not that whole thing ends up evaluating to `True`, because we're running this code as the condition part of an `if` statement.

What does Python do when it sees `False or 6 or 7`? In order to answer that question, we'll need to know about **truthiness** and **short-circuiting**.

# Truthiness

You're familiar with the values `True` and `False`. We call them "Booleans", and we use them most often in `if` statements.

<pre class="dont-format-output"><code class="py">
hungry = True

if hungry:
	print('try eating a slice of pizza')
else:
	print('must be nice')
</code></pre>

Python doesn't limit us to just using `True` and `False` as the condition for `if` statements, though—you can put _any_ expression in there. If you put something in an `if` statement's condition section and it's not `True` or `False`, Python will look at it and decide whether or not it's "truthy".

According to the [official documentation](https://docs.python.org/3/library/stdtypes.html#truth-value-testing), **everything** in Python is considered truthy except for these things:

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

This is what Python sees before it starts evaluating that code:

<div class="boolean-diagram">
<div class="expression">1 == 1</div>
<div class="conjunction">or</div>
<div class="expression">1 == 2</div>
</div>

Remember that if a box is yellow, that means that Python hasn't evaluated it yet.

An `or` expression is truthy if _at least one_ thing in it is truthy. An `and` expression is truthy if _all_ things in it are truthy.

Since this is an `or`, Python evaluates each of the yellow boxes in order until it finds **one** that's truthy. It starts by evaluating `1 == 1`, which turns into `True`.

<div class="boolean-diagram">
<div class="expression truthy">True</div>
<div class="conjunction">or</div>
<div class="expression">1 == 2</div>
</div>

At this point, Python **stops**, because you're in an `or` and it's found something truthy! That's what short-circuiting means. The whole `or` expression evaluates to `True`, because that's the value of the first truthy thing in it.

Here's how the official documentation describes `or`'s behavior:

> it only evaluates the second argument if the first one is false.

Here, I'll prove it to you.

If you divide a non-zero number by zero, Python will throw an exception:

<pre><code class="py">
1 / 0
</code></pre>

Now check out what happens if I put a `1 / 0` _after_ a truthy thing in an `or`:

<pre><code class="py">
print(True or 1 / 0)
</code></pre>

The program prints `True` and **doesn't evaluate the `1 / 0`**! To convince yourself that this works the way I claim it does, try changing that `True` to a `False`.

This matches the behavior we saw in our most recent diagram. Do you remember how the `1 == 2` box stayed yellow to indicate that Python hadn't evaluated the code inside of it?

So, that's what "short-circuiting" means when you're using the `or` operator. The `and` operator is pretty similar to `or`, except that the official documentation says that `and`

> only evaluates the second argument if the first one is true.

That makes sense, because `and` wants to make sure that both of its operands are truthy. If the sub-expression on the left-hand side of an `and` is falsey, then **the whole `and` expression is falsey!** In that situation, there's no need to evaluate the sub-expression on the right-hand side.

Here are some more examples. Do they all behave the way that you expect?

<div class="boolean-diagram falsey">
<div class="expression falsey">1 == 2</div>
<div class="conjunction">and</div>
<div class="expression">2 == 2</div>
</div>

<div class="boolean-diagram falsey">
<div class="expression truthy">1 == 1</div>
<div class="conjunction">and</div>
<div class="expression falsey">1 == 2</div>
</div>

<div class="boolean-diagram truthy">
<div class="expression truthy">1 == 1</div>
<div class="conjunction">and</div>
<div class="expression truthy">2 == 2</div>
</div>

<div class="boolean-diagram falsey">
<div class="expression falsey">1 == 2</div>
<div class="conjunction">or</div>
<div class="expression truthy">1 == 1</div>
</div>


# Back to our buggy `num` code

Now that we know about truthiness and short-circuit evaluation, we can finally figure out what this code does!

<textarea class="hidden">
num = 10

print(num == 5 or 6 or 7)
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

What do you think will be printed out when that code is run?

Before we run it and find out for sure, let's walk through one last set of diagrams using what we've learned. Here's what Python sees before it starts evaluating anything:

<div class="boolean-diagram">
<div class="expression">num == 5</div>
<div class="conjunction">or</div>
<div class="expression">6</div>
<div class="conjunction">or</div>
<div class="expression">7</div>
</div>

Python begins by evaluating `10 == 5`, which turns into `False`.

<div class="boolean-diagram">
<div class="expression falsey">False</div>
<div class="conjunction">or</div>
<div class="expression">6</div>
<div class="conjunction">or</div>
<div class="expression">7</div>
</div>

Next up, it evaluates `6`. We saw earlier that all non-zero numbers are truthy, so now our diagram looks like this:

<div class="boolean-diagram">
<div class="expression falsey">False</div>
<div class="conjunction">or</div>
<div class="expression truthy">6</div>
<div class="conjunction">or</div>
<div class="expression">7</div>
</div>

At this point, Python stops and says: hey, I found something truthy! And that's what the entire expression evaluates to. The answer is `6`!

<pre><code class="py">
num = 10

print(num == 5 or 6 or 7)
</code></pre>

And so that's why the code from the beginning of this article doesn't do what our student expects. `num == 5 or 6 or 7` **will always evaluate to either `True` or `6`**, and so the code inside that `if` statement will **always** be run!

<pre><code class="py">
num = 10

if num == 5 or 6 or 7:
       1 / 0
else:
       print('safe!')
</code></pre>

# Wrapping up

Here are a few more examples—play around with them and try adding some of your own!

<pre><code class="py">
print(False or [])
print(2 or False)
print(False or 0 or "hello")
</code></pre>

Notice how if everything in an **`or`** is **falsey**, then the whole `or` expression will evaluate to the rightmost sub-expression.

<pre><code class="py">
print(False or 0)
</code></pre>

If everything in an **`and`** is **truthy**, then the whole `and` expression will evaluate to the rightmost sub-expression.

<pre><code class="py">
print('cat' and 'dog')
</code></pre>

Oh, and if you want to write some code that does what the student in our example actually wanted, try one of these:


<pre><code class="py">
num = 7

print(num == 5 or num == 6 or num == 7)
print(num in [5, 6, 7])
print(5 <= num <= 7)
</code></pre>

By the way—what do you think this code does? Will it evaluate to `True`? If not, why not?

<textarea class="hidden">
num = 7

num == (5 or 6 or 7)
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

# Resources

* [This walkthrough](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Boolean_Expressions) is great.
* So is [this StackOverflow answer](https://stackoverflow.com/questions/2580136/does-python-support-short-circuiting/14892812#14892812).
* [@codewithanthony](https://twitter.com/codewithanthony) has [this fascinating video](https://www.youtube.com/watch?v=mRPU3l54Z7I&app=desktop) about `False == False in [False]`.



[wcb]: {% post_url 2017-11-30-watercolorbot %}



<script src="{{ site.baseurl }}/assets/js/asciinema-player.js?v={{ site.time }}"></script>
<script src="{{ site.baseurl }}/assets/js/codemirror.js?v={{ site.time }}"></script>
<script src="{{ site.baseurl }}/assets/js/codemirror_python.js?v={{ site.time }}"></script>
<script src="{{ site.baseurl }}/assets/js/codemirror_runmode.js?v={{ site.time }}"></script>


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
<script src="{{ site.baseurl }}/assets/js/klipse.min.js?v={{ site.time }}"></script>
