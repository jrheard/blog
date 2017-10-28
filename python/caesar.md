---
layout: page
title:  "Madison CS 3-4: Caesar Cipher"
---

In this project, you'll write a program that takes a plaintext sentence like "The weather is nice today" and converts it to a ciphertext sentence like "Znk ckgznkx oy toik zujge".

The program can also convert ciphertext *back* to plaintext, when given the right key; and if not given the right key, the program can attempt to brute-force decode the ciphertext.

<div class="message warning">
<p>All of the words and pictures that follow have been directly copy-pasted from Al Swiegart's excellent book "Invent Your Own Computer Games With Python".</p>

<p>This is OK because Al has graciously made this book available under a <a href="https://creativecommons.org/licenses/by-nc-sa/3.0/us/">Creative Commons license</a>. Thanks, Al!</p>
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

The Caesar Cipher was one of the earliest ciphers ever invented. In this cipher, you encrypt a message by taking each letter in the message (in cryptography, these letters are called symbols because they can be letters, numbers, or any other sign) and replacing it with a “shifted” letter. If you shift the letter A by one space, you get the letter B. If you shift the letter A by two spaces, you get the letter C. Here's a picture of some letters shifted over by three spaces:

<img style="display: block; margin: 0 auto;" src="https://inventwithpython.com/chapter14_files/image002.jpg" />

To get each shifted letter, draw out a row of boxes with each letter of the alphabet. Then draw a second row of boxes under it, but start a certain number (this number is the key) of spaces over. After the letters at the end, wrap around back to the start of the boxes. Here is an example with the letters shifted by three spaces:

<img style="display: block; margin: 0 auto;" src="https://inventwithpython.com/chapter14_files/image003.png" />





