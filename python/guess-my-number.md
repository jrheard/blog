---
layout: page
title:  "Madison CS 3-4: Guess My Number"
---

In this project, you'll write a guess-my-number game. When you're done, it'll look like this:

<asciinema-player src="{{ site.baseurl }}/guess_my_number_cast.json?v=1" rows="20" cols="105" autoplay="true" loop="true"></asciinema-player>

Instructions
============

You're basically on your own for this one! There's no starter code - write this program from scratch! You can do it!

You'll be using a `while` loop - possibly a `while True:` loop with a `break` statement somewhere in there, possibly some other variant, it's up to you. Go back to the slides to remind yourself how `while` loops work.

You'll definitely be using at least one `if` statement.

**Your program should choose a different number each time it's run** - don't just hardcode the number 7 in there! We'll be checking to make sure that your program picks a different number each time.

You'll also want to use the `random.randrange()` function in order to choose a number. Here's how I might use it in order to pick a number between 5 and 10:

<pre><code class="py">
import random

# `random.randrange()` picks a random number
# in the specified range each time it's called:
print(random.randrange(5, 11))
print(random.randrange(5, 11))
print(random.randrange(5, 11))
print(random.randrange(5, 11))

# To rerun this code snippet: click on this text box,
# hold the Control key, and then press Enter a bunch of times.
</code></pre>

One last tip: While you're working on this project, it's probably a good idea to have the program **print out the secret number** at the start of the game. This way, when you're working on the program, you can see what the number is and use that information to figure out how best to test the program.

For instance, if I know the number's 37, I might test the program by giving it 40 and then 35 and then 37, and seeing if my program does the right thing each time.

If you do that, though, be sure to remove that line before submitting your finished program. The game's no fun if the player knows the number without having to guess!

Submitting your project
=======================

Submit a file called `guess_my_number_<YOUR_NAME>.py`. For instance, I'd submit a file called `guess_my_number_jr_heard.py`.

On the first line of that file, write a comment with your name on it, like this:

```
# JR Heard
```

Remember to follow this class's [style guide](https://docs.google.com/document/d/1UbyhIkxOdhpf-MGna_5dwh0yHXe02HTZ69CfEuYv76Y/edit).

The part about descriptive variable names is really important! For instance:

* `n` is a bad variable name, `username` is a good one.
* `ns` is a bad variable name, `number_of_symbols` is a good one.


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
{% javascript asciinema-player %}
{% javascript klipse.min %}
