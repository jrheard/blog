---
layout: page
title:  "Madison CS 3-4: Password generator and checker"
---

In this project, you'll write two programs: a password **generator** and a password **checker**.

Password Generator
==================

The password generator is a little Python program that prints a string like "Fj3io19aA" to the screen and then exits. Every time you run the program, it'll print out a different string - so maybe the next time you run it, you'll see an output of "1LPoxA25Pq", you get the idea.

You already know that you can print something to the screen by writing code like `print("Hello there!")`, but we'll need to do some thinking if we want to figure out how to actually generate a password from scratch. I'll give you a few useful bits of code that might come in handy.

Here's how to write some code that chooses a random lower-case letter every time it's run:

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
1. You can change that snippet's Python code yourself, or even write your own code in there. Try changing it so that it says `lowercase_letters = 'ABCDE'` and see what happens. Press `Ctrl+Enter` a few more times while you're at it.

When we give you assignments in this class, they'll often have interactive code snippets like these because you can learn a lot by playing around with the example code yourself instead of just reading it. You should mess around with every one of these code snippets yourself; it makes the whole experience less intimidating, and it's really fun!

Back to the assignment!
-----------------------

OK, so we know how to pick a random lowercase letter using the [random module](https://docs.python.org/2/library/random.html). You can also use the same approach in order to pick a random uppercase letter, or number, or symbol.

Another useful thing to remember is that you can add strings together (we call this "concatenating" them) by using the `+` sign:

<pre><code class="py">
a_lowercase_letter = "j"
an_uppercase_letter = "N"
a_number = "6"

print(a_lowercase_letter + an_uppercase_letter + a_number)
</code></pre>

Finally, here's a useful bit of code that you can use to randomly shuffle a string:

<pre><code class="py">
import random

my_name = 'jrheard'
shuffled_name = ''.join(random.sample(my_name, len(my_name)))

print(shuffled_name)
</code></pre>

Try changing `my_name` to be **your** name so you're sure that this code works on your name too, and don't forget to use `Ctrl+Enter` to re-execute the snippet a bunch of times until you're convinced it's different each time.

There's some weird stuff going on in that snippet - what's that `''.join()` call all about, for instance? - but I'm not going to explain it just yet, we'll cover it in a later assignment. For now, you can just copy-paste that line of code into your program if you'd like to use it. In later projects, you won't be allowed to copy-paste code you don't understand, so be sure to cherish this moment while it lasts.

Now you have everything you'll need in order to write a password generator!

Your generator should generate passwords that meet the PPS standard: they should be **at least 8 characters long, and they should include at least 3 of these 4 categories: number, uppercase letter, lowercase letter, symbol.** (A "symbol" is one of these: `!@#$%^&*()-_=+,.`)


Password Strength Checker
=========================

The password strength checker is a program which asks the user for a password and prints out `"GOOD"` if it meets the PPS standard mentioned above, or prints out `"BAD"` if the password does not meet the PPS standard. Remember that you can use `input()` to ask the user for a password.

In order to check that it meets the PPS criteria, you'll want to loop over each character of the password and write some code that keeps track of how many lowercase letters, uppercase letters, etc are contained in the string. For instance, here's a bit of code that checks to see how many times the letter `"z"` is in the word `"Pizza"`:

<pre><code class="py">
word = "Pizza"
number_of_zs = 0

for letter in word:
    if letter == 'z':
	    number_of_zs = number_of_zs + 1

print(number_of_zs)
</code></pre>

Also, remember that you can check the length of a string by calling the `len()` function:
<pre><code class="py">
print(len("jfioaewofweijaewiof8a9wef"))
</code></pre>

One other thing: passwords should not contain your name or your student ID. So if my first name is `"JR"`, my last name is `"Heard"`, and my student ID is `12345`, then these are all bad passwords:

* CarlsjR1234.
* 5YaHeArD!
* Password12345

Your password checker should print out `"BAD"` if the user gives it a password containing **your** name or student ID. We'll be checking to make sure you did this right!

You can check to see if one string is in another string by using `.find()`, like this:

<pre><code class="py">
# "llo" is in "Hello", starting at index 2.
print("Hello".find("llo"))

# a_string.find(another_string) returns -1
# if another_string isn't in a_string.
print("Hello".find("potatoes"))
</code></pre>

Here's one slightly tricky thing about this part of the project: my last name is `"Heard"`, and the password `5YaHeArD!` is invalid, but:

<pre><code class="py">
print("Heard" == "HeArD")
</code></pre>

Your password checker should be able to tell if a password contains your name, even if the password's capitalization is all funky like that and doesn't exactly match how you capitalize your own name. Here's a relevant bit of code that you might find handy when you start thinking about how to handle this problem:

<pre><code class="py">
print("HeArD".lower())
</code></pre>

That should be everything you need to get started. Good luck!

Submitting your project
=======================

Submit two files: `password_generator.py` and `password_checker.py`.

Notes
=====

* [Don't share your password with other people.](http://bash.org/?244321)
* [In reality, the passwords generated in this project aren't all that secure!](https://xkcd.com/936/)


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
