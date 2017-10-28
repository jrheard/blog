---
layout: page
title:  "Madison CS 3-4: Caesar Cipher"
---

In this project, you'll write a program that takes a plaintext sentence like "The weather is nice today" and converts it to a ciphertext sentence like "Znk ckgznkx oy toik zujge".

The program can also convert ciphertext *back* to plaintext, when given the right key. The program can also attempt to brute-force decode the ciphertext.

Don't worry, you're about to learn what all those words meant!

<div class="message">
<p>All of the words and pictures between this gray box and the next gray box have been copy-pasted directly from Al Swiegart's excellent book "Invent Your Own Computer Games With Python", except for a few very minor edits.</p>

<p>This is OK because Al has graciously made his book available under a <a href="https://creativecommons.org/licenses/by-nc-sa/3.0/us/">Creative Commons license</a>.</p>
</div>

Encryption
==========

The science of writing secret codes is called **cryptography**. For thousands of years cryptography has made secret messages that only the sender and recipient could read, even if someone captured the messenger and read the coded message. A secret code system is called a **cipher**. The cipher used by the program in this chapter is called the Caesar cipher.

In cryptography, we call the message that we want to be secret the **plaintext**. The plaintext could look like this:

`Hello there! The keys to the house are hidden under the flower pot.`

Converting the plaintext into the encoded message is called **encrypting** the plaintext. The plaintext is encrypted into the **ciphertext**. The ciphertext looks like random letters, and we cannot understand what the original plaintext was just by looking at the ciphertext. Here is the previous example encrypted into ciphertext:

`Yvccf kyviv! Kyv bvpj kf kyv yfljv riv yzuuve leuvi kyv wcfnvi gfk.`

But if you know about the cipher used to encrypt the message, you can **decrypt** the ciphertext back to the plaintext. (Decryption is the opposite of encryption.)

Many ciphers also use keys. **Keys** are secret values that let you decrypt ciphertext that was encrypted using a specific cipher. Think of the cipher as being like a door lock. You can only unlock it with a particular key.

The Caesar Cipher
=================

The key for the Caesar Cipher will be a number from 1 to 26. Unless you know the key (that is, know the number used to encrypt the message), you won’t be able to decrypt the secret code.

The Caesar Cipher was one of the earliest ciphers ever invented. In this cipher, you encrypt a message by taking each letter in the message (in cryptography, these letters are called symbols because they can be letters, numbers, or any other sign) and replacing it with a “shifted” letter. If you shift the letter A by one space, you get the letter B. If you shift the letter A by two spaces, you get the letter C.

Here's a picture of some letters shifted over by three spaces:

{% img caesar_1.jpg %}

To get each shifted letter, draw out a row of boxes with each letter of the alphabet. Then draw a second row of boxes under it, but start a certain number (this number is the key) of spaces over. After the letters at the end, wrap around back to the start of the boxes.

Here's an example with the letters shifted by three spaces:

{% img caesar_2.jpg %}

**The number of spaces you shift is the key in the Caesar Cipher**. The example above shows the letter translations for the key 3.

If you encrypt the plaintext `“Howdy”` with a key of 3, then:

* The “H” becomes “K”.
* The letter “o” becomes “r”.
* The letter “w” becomes “z”.
* The letter “d” becomes “g”.
* The letter “y” becomes “b”.

The ciphertext of `“Hello”` with key 3 becomes `“Krzgb”`.

We will keep any non-letter characters the same. To decrypt `“Krzgb”` with the key 3, we go from the bottom boxes back to the top:

* The letter “K” becomes “H”.
* The letter “r” becomes “o”.
* The letter “z” becomes “w”.
* The letter “g” becomes “d”.
* The letter “b” becomes “y”.

ASCII, and Using Numbers for Letters
====================================

How do we implement this shifting of the letters as code? We can do this by representing each letter as a number called an **ordinal**, and then adding or subtracting from this number to form a new ordinal (and a new letter). ASCII (pronounced “ask-ee” and stands for American Standard Code for Information Interchange) is a code that **connects each character to a number between 32 and 126**.

The capital letters “A” through “Z” have the ASCII numbers 65 through 90. The lowercase letters “a” through “z” have the ASCII numbers 97 through 122. The numeric digits “0” through “9” have the ASCII numbers 48 through 57.

So if you wanted to shift “A” by three spaces, you would do the following:

* Convert “A” to an ordinal (65).
* Add 3 to 65, to get 68.
* Convert the ordinal 68 back to a letter (“D”).

<div class="message">
<p>Copy-pasting complete. Thanks, Al!</p>
</div>

Converting between letters and numbers
======================================

Python comes with the `ord()` function, which lets you convert a letter to its corresponding ordinal number:

<pre><code class="py">
print(ord('j'))
</code></pre>

To go from an ordinal number back to a letter, you can use the `chr()` function.

<pre><code class="py">
print(chr(106))
</code></pre>

Let's try shifting the letter `H` over by 3, like we did in the `"Howdy"` example above:

<pre><code class="py">
h_ordinal = ord('H')
h_ordinal_shifted = h_ordinal + 3

print(chr(h_ordinal_shifted))
</code></pre>

It turns into `K`, just like we expected!






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
