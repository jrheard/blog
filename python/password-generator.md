---
layout: page
title:  "Madison CS 3-4: Password Generator"
python_snippets: true
---

For this project, you'll write a program that prints a randomly generated password like "Fj3io19aA" to the screen and then exits. Every time you run the program, it'll print out a different password, like this:

<asciinema-player src="{{ site.baseurl }}/password_generator_cast.json" rows="8" cols="80" autoplay="true" loop="true"></asciinema-player>

Start by downloading this program's **[starter code][starter-code]** and opening it in IDLE. Note that the starter code has a `generate_password()` function - put your code in that function, and don't change the function's name.

You already know that you can print something to the screen by writing code like `print("Hello there!")`, but we'll need to do some thinking if we want to figure out how to actually generate a password from scratch. I'll give you a few useful bits of code that might come in handy.

Here's how to use the `choice()` function from the [random](https://docs.python.org/2/library/random.html) library to choose a random lower-case letter:

<pre><code class="py">
import random

lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
random_letter = random.choice(lowercase_letters)

print(random_letter)
</code></pre>

Interactive Snippets
--------------------

The code snippet above is interactive, which means:

1. You can re-run it by clicking on it and then pressing `Ctrl+Enter` (hold down the Control key, then press the Enter key). Try doing that now. Notice that it prints out a different letter almost every time you run it!
1. You can change that snippet's Python code yourself, or even write your own code in there. Try changing it so that it says `lowercase_letters = 'ABCDE'` and see what happens. (NOTE: calling the variable `lowercase_letters` doesn't automatically force it to hold only lowercase letters!) Press `Ctrl+Enter` a few more times while you're at it.

When we give you assignments in this class, they'll often have interactive code snippets like these because you can learn a lot by playing around with the example code yourself instead of just reading it. **You should mess around with every single one of these code snippets yourself**; it makes the whole experience less scary, and it's really fun!

Back to the assignment!
-----------------------

OK, so now we know how to use the code above to pick a random lowercase letter. You can also use the same approach in order to pick a random uppercase letter, or number, or symbol. Do you know how you would modify the code snippet above to do this? Go ahead and try it out!

Now then: another useful thing to remember is that you can add strings together (we call this "concatenating" them) by using the `+` sign:

<pre><code class="py">
a_lowercase_letter = "j"
an_uppercase_letter = "N"
a_number = "6"

print(a_lowercase_letter + an_uppercase_letter + a_number)
</code></pre>

Remember that you can check the length of a string by calling the `len()` function:
<pre><code class="py">
print(len("jfioaewofweijaewiof8a9wef"))
</code></pre>

Finally, here's how to use the `sample()` function from the `random` library to shuffle a string:

<pre><code class="py">
import random

my_name = 'JR Heard'
shuffled_name = ''.join(random.sample(my_name, len(my_name)))

print(shuffled_name)
</code></pre>

Try changing the value of that snippet's `my_name` variable to be **your** name so you're sure that this code works on your name too, and don't forget to use `Ctrl+Enter` to re-execute the snippet a bunch of times until you're convinced it's different each time.

There's some weird stuff going on in that snippet - what's that `''.join()` call all about, for instance? - but I'm not going to explain it just yet, we'll cover it in a later assignment. For now, you can just copy-paste that line of code into your program if you'd like to use it. In later projects, you won't be allowed to copy-paste code you don't understand, so be sure to cherish this moment while it lasts.

Now you have everything you'll need in order to write a password generator!

Your generator should generate passwords that meet the PPS standard: they should be **at least 8 characters long, and they should include at least 3 of these 4 categories: number, uppercase letter, lowercase letter, symbol.** (A "symbol" is one of these: `!@#$%^&*()-_=+,.`)

Before submitting your project, make sure to double-check that your program does all of the things I said in the line above, because if your program has any bugs, [I'll find them!](https://www.youtube.com/watch?v=AqWFaDJYhIA) :)


Submitting your project
=======================

Submit a file called `password_generator_<YOUR_NAME>.py`. For instance, I'd submit a file called `password_generator_jr_heard.py`.

On the first line of that file, write a comment with your name on it, like this:

```
# JR Heard
```

Remember to follow this class's [style guide](https://docs.google.com/document/d/1UbyhIkxOdhpf-MGna_5dwh0yHXe02HTZ69CfEuYv76Y/edit).

Notes
=====

* [Don't share your password with other people.](http://bash.org/?244321)
* [In reality, the passwords generated in this project aren't all that secure!](https://xkcd.com/936/)


[starter-code]: {{site.baseurl}}/python/password_generator_starter_code.py


<script src="{{ site.baseurl }}/assets/js/asciinema-player.js?v={{ site.time }}"></script>
