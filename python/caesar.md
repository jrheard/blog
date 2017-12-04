---
layout: page
title:  "Madison CS 3-4: Caesar Cipher"
---

In this project, you'll write a program that takes a **plaintext** sentence like `THE WEATHER IS NICE TODAY` and converts it to a **ciphertext** sentence like `GUR JRNGURE VF AVPR GBQNL`. The program can also convert ciphertext *back* to plaintext, when given the right **key**.

Don't worry, you're about to learn what those words mean!

<div class="message update">
<p>All of the words and pictures between this yellow box and the next yellow box have been copy-pasted directly from Al Sweigart's excellent book "Invent Your Own Computer Games With Python". I've made a few very minor edits.</p>

<p>This is OK because Al has graciously made his book available under a <a href="https://creativecommons.org/licenses/by-nc-sa/3.0/us/">Creative Commons license</a>. Thanks, Al!</p>
</div>

Encryption
==========

The science of writing secret codes is called **cryptography**. For thousands of years cryptography has made secret messages that only the sender and recipient could read, even if someone captured the messenger and read the coded message. A secret code system is called a **cipher**. The cipher used by the program you're about to build is called the Caesar cipher.

In cryptography, we call the message that we want to be secret the **plaintext**. The plaintext could look like this:

`HELLO THERE! THE KEYS TO THE HOUSE ARE HIDDEN UNDER THE FLOWER POT.`

Converting the plaintext into the encoded message is called **encrypting** the plaintext. The plaintext is encrypted into the **ciphertext**. The ciphertext looks like random letters, and we cannot understand what the original plaintext was just by looking at the ciphertext. Here is the previous example encrypted into ciphertext:

`YVCCF KYVIV! KYV BVPJ KF KYV YFLJV RIV YZUUVE LEUVI KYV WCFNVI GFK.`

But if you know about the cipher used to encrypt the message, you can **decrypt** the ciphertext back to the plaintext. (Decryption is the opposite of encryption.)

Many ciphers also use keys. **Keys** are secret values that let you decrypt ciphertext that was encrypted using a specific cipher. Think of the cipher as being like a door lock. You can only unlock it with a particular key.

The Caesar Cipher
=================

The key for the Caesar Cipher will be a number from 1 to 26. Unless you know the key (that is, know the number used to encrypt the message), you won’t be able to decrypt the secret code.

The Caesar Cipher was one of the earliest ciphers ever invented. In this cipher, you encrypt a message by taking each letter in the message (in cryptography, these letters are called symbols because they can be letters, numbers, or any other sign) and replacing it with a “shifted” letter. If you shift the letter A by one space, you get the letter B. If you shift the letter A by two spaces, you get the letter C.

Here's a picture of some letters shifted over by three spaces:

{% img caesar_1.jpg %}

To get each shifted letter, draw out a row of boxes with each letter of the alphabet. Then draw a second row of boxes under it, but start a certain number (this number is the key) of spaces over. After the letters at the end, **wrap around** back to the start of the boxes.

Here's an example with the letters shifted by three spaces:

{% img caesar_2.png %}

**The number of spaces you shift is the key in the Caesar Cipher**. The example above shows the letter translations for the key 3.

If you encrypt the plaintext `“HOWDY”` with a key of 3, then:

* The “H” becomes “K”.
* The letter “O” becomes “R”.
* The letter “W” becomes “Z”.
* The letter “D” becomes “G”.
* The letter “Y” becomes “B”.

The ciphertext of `“HOWDY”` with key 3 becomes `“KRZGB”`.

We will keep any non-letter characters the same. To decrypt `“KRZGB”` with the key 3, we go from the bottom boxes back to the top:

* The letter “K” becomes “H”.
* The letter “R” becomes “O”.
* The letter “Z” becomes “W”.
* The letter “G” becomes “D”.
* The letter “B” becomes “Y”.

ASCII, and Using Numbers for Letters
====================================

How do we implement this shifting of the letters as code? We can do this by representing each letter as a number called an **ordinal**, and then adding or subtracting from this number to form a new ordinal (and a new letter). ASCII (pronounced “ask-ee” and stands for American Standard Code for Information Interchange) is a code that **connects each character to a number between 32 and 126**.

The capital letters “A” through “Z” have the ASCII numbers 65 through 90. The lowercase letters “a” through “z” have the ASCII numbers 97 through 122. The numeric digits “0” through “9” have the ASCII numbers 48 through 57.

So if you wanted to shift “A” by three spaces, you would do the following:

* Convert “A” to an ordinal (65).
* Add 3 to 65, to get 68.
* Convert the ordinal 68 back to a letter (“D”).

<div class="message update">
<p>That's the end of the copy-pasted section of Al's book. Everything after this box was written by JR like usual.</p>
</div>

Converting between letters and numbers
======================================

Python comes with the `ord()` function, which lets you convert a letter to its corresponding ordinal number:

<pre><code class="py">
print(ord('J'))
</code></pre>

To go from an ordinal number back to a letter, you can use the `chr()` function.

<pre><code class="py">
print(chr(74))
</code></pre>

Let's try shifting the letter `H` over by 3, like we did in the `"Howdy"` example above:

<pre><code class="py">
print(chr(ord('H') + 3))
</code></pre>

It turns into `K`, just like we expected! `ord()` and `chr()` are going to be your best friends while you're working on this project.

String Manipulation Tip
=======================

You'll probably want to use a `for` loop at some point in your program - here's how you can use a `for` loop to do _something_ to each letter of a string:

<pre><code class="py">
my_name = "JR Heard"
transformed_name = ""

for letter in my_name:
	transformed_name += letter.lower()

print(transformed_name)
</code></pre>

That chunk of code painstakingly lowercases my name, one letter at a time - you might end up doing something similar (but different!) when you're building up your program's `ciphertext` variable.

Non-Uppercase-Letter Characters
=====================

If your program is given some plaintext that includes numbers, or lowercase letters, or punctuation marks like `!` or `.` or `$` or _anything_ that's not a letter from `A` to `Z`, it should leave that character unmodified. For example, if given a plaintext string of `HOWDY! Hello.` and a key of `5`, your program should output the ciphertext `MTBID! Mello.`

Note that in that message, the `W` ends up "wrapping around" to become a `B` when it's encrypted.

Demo
====

Your program should allow the user to both encrypt messages **and** decrypt them. Your program should look **exactly** like this when it's run:

<asciinema-player src="{{ site.baseurl }}/caesar_cast_1.json" rows="19" cols="80" autoplay="true" loop="true"></asciinema-player>

In order to get Python to prompt the user for input on a new line like you see in the demo above, you can add the `\n` character to the end of the string you give the `input()` function. That sentence might have sounded scary, but I'm just talking about doing this:

```python
input('Do you wish to encrypt or decrypt a message?\n')
```

If you don't know what I'm talking about, you'll see what I mean when you sit down to write the program yourself. It won't be a big deal. `\n` is the "newline" character - when Python sees it when it's printing out a string, it'll stop the current line of text and start a new one.

Nitty Gritty
============

If the user inputs an invalid mode (i.e. something that's not "encrypt" or "decrypt"), it's fine if your program crashes.

If the user inputs an invalid key (i.e. something that's not a number between 1 and 26), it's fine if your program crashes.

Submitting your project
=======================

Submit a file called `caesar.py`.

On the first line of that file, write a comment with your name on it, like this:

```
# JR Heard
```

Remember to follow this class's [style guide](https://docs.google.com/document/d/1UbyhIkxOdhpf-MGna_5dwh0yHXe02HTZ69CfEuYv76Y/edit).

Extra Credit
==========

talk to tamara about how to frame this section, re: extra credit, grades

Here are some ideas for cool extra features you can add to your program for extra credit.

Lowercase Letters
-----------------

Make your program work with uppercase _and_ lowercase characters, like this:

<asciinema-player src="{{ site.baseurl }}/caesar_upper_and_lower_cast.json" rows="19" cols="80" autoplay="true" loop="true"></asciinema-player>

When I did this, I ended up switching away from `ord()` and `chr()`, and instead made a string like `transformable_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'` and had my code do stuff based on the position of each letter of the message in my `transformable_characters` string. Here's how you can find the first position of a letter in a string in Python:

<pre><code class="py">
# 'l' is in 'Hello', so this evaluates to number 2.
print('Hello'.find('l'))

# 'z' isn't in 'Hello', so this evalutes to -1, which is
# Python's way of saying: I looked for this but couldn't find it!
print('Hello'.find('z'))
</code></pre>

Brute Force
-----------

Add a "brute force" mode that lets you try to decrypt a message even if you don't know the right key for it:

<asciinema-player src="{{ site.baseurl }}/caesar_brute_cast.json" rows="30" cols="80" autoplay="true" loop="true"></asciinema-player>

This might be a little painful to do if you don't know how to write your own functions. We'll be learning how to do that in class soon, but we haven't covered it yet. If you'd like to read ahead in the meantime, [this article](https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/functions.html) seems like a good introduction to writing your own functions.

Smart Brute Force
-----------------

This is my favorite one: enhance your program's "brute force" mode so that it can _automatically detect_ the correct key:

<asciinema-player src="{{ site.baseurl }}/caesar_brute_smart_cast.json" rows="15" cols="80" autoplay="true" loop="true"></asciinema-player>

You can do this however you want. Be creative! My solution involved using [this text file](https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co), which is a list of all of the English words in the 1934 edition of Webster's Second International Dictionary. If you'd like to figure out how to open a text file in Python and get all the lines out of it, Google around until you find a solution - you can always ask me for help if you get stuck, but I think you'd be surprised how far you can get by just Googling stuff 🙂


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
