---
layout: post
title:  "Book Report: Architecture Patterns with Python"
klipse: false
---

I recently read [Architecture Patterns with Python](https://www.cosmicpython.com/). The book's primary focus is on how to structure programs so that they stay simple and maintainable as they grow: that's my specific favorite programming topic, so of course I liked it. I'm probably not going to use the exact techniques that the authors recommend in this book, but they discussed some cool ideas that reminded me of things I've run into at past jobs, and the book's [available to read for free online](https://www.cosmicpython.com/book/preface.html), so what's not to like?

The book discusses domain-driven design and an event-driven architecture (potentially, but not necessarily, a microservices-based one). I didn't walk away from the book knowing much more about DDD than I did before, which is OK[^1]; and the authors were careful to not wholeheartedly recommend microservices, which I appreciated.

I want to talk a bit about some of my favorite ideas from the book. Before we get there, I want to knock out a few odds and ends:

## Side notes
* It was a relatively fast read - nice clear prose, nice short chapters.
* Each chapter had a short pros/cons table at the end with some really frank discussion of whether or not the technique discussed in that chapter could be worth applying in your own work. Many of the "cons" sections looked something like this, and I appreciated their candor:
  * "We’ve been at pains to point out that each pattern comes at a cost. Each layer of indirection has a price in terms of complexity and duplication in our code and will be confusing to programmers who’ve never seen these patterns before."
* It seems like the authors disagree with each other about a lot of the techniques they propose as they get farther into the book, which makes it hard to trust that they’re good ideas. If the authors of the book aren’t both sure, then why should I be sure?

OK, on to the good stuff.

## Value Objects

The book recommends using "value objects" to represent core primitive business concepts, and suggests using dataclasses to do it. Here's an example from [Chapter 1](https://www.cosmicpython.com/book/chapter_01_domain_model.html):

<textarea class="hidden">
@dataclass(frozen=True)
class OrderLine:
    orderid: OrderReference
    sku: ProductReference
    qty: Quantity
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

I **also** recommend this. I hope to soon write more about why frozen dataclasses are so useful. A big part of it is that they're small and (as long as you don't cram a bunch of methods in them) easy to understand. Just look at that `OrderLine` definition: there's nothing up its sleeve, it's just plain old data!

## Pure functions

Pure functions come up now and then, although I don't remember the book spending much time addressing the topic head-on. That's OK, because they did a great job of showing them in action.

For instance, in [Chapter 3](https://www.cosmicpython.com/book/chapter_03_abstractions.html) they're writing a program to sync files between two directories, and are trying to figure out how to make it easy to test. At first, the whole program is concerned with operating directly on the file system, and so in all their tests they have to spin up some temporary directories and write a bunch of files to them and call the program and examine what it did to the temporary directories.

But then they propose a different approach: "[w]e’re going to separate _what_ we want to do from _how_ to do it". They change the core of their program so that it takes two dicts as input, each representing the files in a directory:

<textarea class="hidden">
source_files = {'hash1': 'path1', 'hash2': 'path2'}
dest_files = {'hash1': 'path1', 'hash2': 'pathX'}
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

And to go along with that, their program now returns a list of operations that it wants to perform in order to sync the two directories:

<textarea class="hidden">
("COPY", "sourcepath", "destpath"),
("MOVE", "old", "new"),
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

In order to test the sync algorithm, the authors don't have to read from and write to the file system any more - they can just pass a couple of dicts into the program, examine the data that it returns as output, and check to see if the program _wants_ to do the right thing. The dicts and tuples that their tests use are trivial to construct, no side effects (or, God forbid, mocking/patching) necessary.

There's still some code at the edges that turns the filesystem into those dicts and turns those commands into side effects, but that's an unavoidable fact of life; the main thing that matters is that the bulk of the program is now side-effect-free. Lovely!

This is the same thing as ["functional core, imperative shell"](https://www.destroyallsoftware.com/screencasts/catalog/functional-core-imperative-shell)[^2], which is the idea that the bulk of your program should be pure functions with a thin layer at the edges for actually interacting with the real world. I'll write more about this in the future too, but long story short, I think that this is a very good idea.





[^1]: I have Scott Wlaschin's "Domain Modeling Made Functional" on my desk, and am hoping that that book'll be the one that finally makes DDD click for me. I love his talks on YouTube, I need to go back and watch them all. Brilliant guy.

[^2]: Oh my gosh, I just found out as I was writing this that Scott Wlaschin just [gave a talk on this exact topic](https://www.youtube.com/watch?v=P1vES9AgfC4)! Added it to my watchlist!


<!-- TODO turn this into something i can just include-->
<!-- TODO can i make, like, a directive out of this textarea/pre thing? -->

<script src="{{ site.baseurl }}/assets/js/codemirror.js?v={{ site.time }}"></script>
<script src="{{ site.baseurl }}/assets/js/codemirror_python.js?v={{ site.time }}"></script>
<script src="{{ site.baseurl }}/assets/js/codemirror_runmode.js?v={{ site.time }}"></script>
<script>
var textAreas = document.getElementsByTagName("textarea");
var pres = document.querySelectorAll("pre.cm-s-friendship-bracelet");

for (var i = 0; i < textAreas.length; i++) {
	CodeMirror.runMode(textAreas[i].value, "python", pres[i]);
}

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
