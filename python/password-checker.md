---
layout: page
title:  "Madison CS 3-4: Password Checker"
---

In a previous project, we wrote a [password generator]({{site.baseurl}}/python/password-generator). Our generator created random passwords that met the PPS standard, which is: passwords should be **at least 8 characters long, and they should include at least 3 of these 4 categories: number, uppercase letter, lowercase letter, symbol.**

(A "symbol" is one of these: `!@#$%^&*()-_=+,.`)

In this project, we'll be writing a program that lets the user type in a password to see whether it's good or not. If the password is good, the program will print out `GOOD`; otherwise, the program will print out `BAD`.

One extra rule that we're adding in this project is that **passwords should not contain your PPS username or student ID number**.

When you're done, your program should look exactly like this:

<asciinema-player src="{{ site.baseurl }}/password_checker_cast.json?v=1" rows="12" cols="90" autoplay="true" loop="true"></asciinema-player>

Getting Started
===============

**Download this project's [starter code][starter-code] and open it in IDLE.**

The starter code has two functions: `is_password_good(password, username, student_id)` and `main()`.

**`is_password_good(password, username, student_id)`** is where your password-strength-checking code will go.

This function should take a password like `'hello there'`, a username like `'jrheard'`, and a student ID number like `'12345'` and return `True` if the password meets the PPS password requirements listed at the top of this assignment. If the password does _not_ meet those requirements, then this function should return `False`.

(Remember that `False` isn't the same thing as `'False'`. The Boolean values `True` and `False` don't have quote marks around them.)

**`main()`** is where the rest of your code will go. In this function, you should ask the user for their username, student ID, and a password to check, and you should print out `GOOD` if the password was good or `BAD` if it was bad.

Useful Code Snippets
====================

**These code snippets are _hints_. They solve problems that are _really similar to, but not quite the same as_ the problems you'll be solving in this assignment. You will need to think really hard about these snippets and make changes to them or rewrite them entirely from scratch, don't just copy-paste them into your program and expect them to work.**

Looping over each letter in a string
------------------------------------

You will definitely be looping over each letter of the password and doing something based on the letters you see.

Here's how to loop over each letter of a string and do something with each letter:
<pre><code class="py">
word = "Pizza"

# Loop over each letter of the string....
for letter in word:

	# ...and do something with that letter.
	print(letter)

</code></pre>

Seeing If One String Is In Another String
-----------------------------------------

You can check to see if one string is in another string by using Python's `in` operator, like this:

<pre><code class="py">
# `in` works for single letters like 'z' and 'f'...
print('z' in 'Pizza')
print('f' in 'Pizza')

# ...and also for longer strings like 'llo' and 'potatoes'.
print('llo' in 'Hello')
print('potatoes' in 'Hello')
</code></pre>

Notice that you get a result of `True` or `False`, so you could use this code as a condition in an `if` statement if you wanted to.

How might you use this technique to see if e.g. a letter is an uppercase letter?

Counting Things
---------------

In order to check that a password meets the PPS criteria, you'll want to loop over each character of the password and write some code that **keeps track of whether the password has any lowercase letters, uppercase letters, symbols, or numbers.** For instance, here's a bit of code that checks to see how many `'z'`s there are in a particular string:


<pre><code class="py">
word = "Pizza"
number_of_zs = 0

for letter in word:
    if letter == 'z':
	    number_of_zs = number_of_zs + 1

print(number_of_zs)
</code></pre>

Remember, though, that we don't care about *how many* uppercase letters are in a password; we just care about whether or not there *are any*.


Disallowing Student Info In Passwords
-------------------------------------

If my username is `jrheard` and my student ID is `12345`, then per the rules mentioned at the top of this page, these are bad passwords:

* `CarlsjRHeard!`
* `Password12345`

Here's one slightly tricky thing about this part of the project: my username is `"jrheard"`, and the password `"CarlsjRHeard!"` is invalid, but Python strings are **case sensitive**:

<pre><code class="py">
print("jrheard" == "jRHeard")
</code></pre>

Your password checker should be able to tell if a password contains your username, even if the password's capitalization is all funky like that. One way to handle this problem is to call a string's `.lower()` or `.upper()` method, like this:

<pre><code class="py">
print("jRHeard".lower())
print("jRHeard".upper())
</code></pre>

You will **definitely** be using this technique in your program. **Take your time and think about how `.lower()` or `.upper()` might be useful for dealing with the fact that string comparison in Python is case sensitive.**

Debugging Tip
-------------

As you're working on your program, you might find it useful to add some extra `print()` calls that print out what programmers call "debug information" to help you understand what your program's actually doing. For instance:

<asciinema-player src="{{ site.baseurl }}/password_checker_debug_cast.json?v=2" rows="18" cols="90" autoplay="true" loop="true"></asciinema-player>

It's OK if you leave those `print()` calls in there, you don't need to remove them before submitting your project. Just be sure that the last line of your checker's output says the word `GOOD` or the word `BAD`, with nothing else on that line, like you see in the example above.

That should be everything you need to get started. Good luck!

Submitting your project
=======================

Submit a file called `password_checker_<YOUR_NAME>.py`. For instance, I'd submit a file called `password_checker_jr_heard.py`.

On the first line of that file, write a comment with your name on it, like this:

```
# JR Heard
```

I've written some pretty crazy tests for this project that will make sure that your checker is implemented correctly, so **double check the requirements at the top of this page** before you submit your program, because if your program has any bugs, I _will_ find them! :)

Try coming up with some passwords that you know should be marked `GOOD` and some passwords that you know should be marked `BAD` and putting them into your program to make sure that it marks them correctly.

(Is `'A!a'` a good password? Why or why not?)

If you'd like to learn more about how I wrote these tests, [here's a talk I gave about this topic at the Portland Python meetup](https://www.youtube.com/watch?v=AqWFaDJYhIA). It's the best talk I've ever given, I'm really proud of it, consider watching it sometime!

Remember to follow this class's [style guide](https://docs.google.com/document/d/1UbyhIkxOdhpf-MGna_5dwh0yHXe02HTZ69CfEuYv76Y/edit).

The part about descriptive variable names is really important! For instance:

* `n` is a bad variable name, `username` is a good one.
* `ns` is a bad variable name, `number_of_symbols` is a good one.


[starter-code]: {{site.baseurl}}/python/password_checker_starter_code.py

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
