---
layout: post
title:  "Book Report: Architecture Patterns with Python"
python_snippets: true
---

I recently read [Architecture Patterns with Python](https://www.cosmicpython.com/). The book's primary focus is on how to structure programs so that they stay simple and maintainable as they grow: that's my specific favorite programming topic, so of course I liked it. I'm probably not going to use the exact techniques that the authors recommend in this book, but they discussed some cool ideas that reminded me of things I've run into at past jobs, and the book's [available for free online](https://www.cosmicpython.com/book/preface.html), so what's not to like?

<img src="{{site.baseurl}}/assets/img/architecture_patterns_with_python.jpg" />

The book discusses domain-driven design and an event-driven architecture (potentially, but not necessarily, a microservices-based one). I'm going to talk a bit about some of my favorite ideas from the book, but I want to knock out a few odds and ends before we get there:

## Side Notes
* It was a relatively fast read - nice clear prose, nice short chapters.
* I didn't walk away from the book having become a total expert in DDD, but that's OK[^1].
* The authors were careful to not wholeheartedly recommend microservices, which I appreciated.
* Each chapter had a short pros/cons table at the end with some really frank discussion of whether or not the technique discussed in that chapter could be worth applying in your own work. Many of the "cons" sections looked something like this, and I appreciated their candor:
  * "We’ve been at pains to point out that each pattern comes at a cost. Each layer of indirection has a price in terms of complexity and duplication in our code and will be confusing to programmers who’ve never seen these patterns before."

OK, on to the good stuff.

## Value Objects

The book recommends using "value objects" to represent core primitive business concepts, and suggests using dataclasses to do it. Here's an example from [Chapter 1](https://www.cosmicpython.com/book/chapter_01_domain_model.html#_dataclasses_are_great_for_value_objects):

<textarea class="hidden">
@dataclass(frozen=True)
class OrderLine:
    order_id: OrderReference
    sku: ProductReference
    qty: Quantity
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

I **also** recommend doing this. The important thing here is that this class doesn't know anything about a database/ORM - it's just a simple dataclass that refers to some other simple dataclasses. It's really easy to write nice, easy-to-test pure functions that operate on data like this. In an ideal world, this is what **all** of your core primitives would look like.

This brings us to our next topic, which is extremely related:

## Dependency Inversion Principle

This term was new to me, and is my favorite idea from the whole book. It's easiest to explain by contrast to the previous example. Most of the codebases I've worked in have used models like this as their core primitives instead of going with the approach you saw above:

<textarea class="hidden">
class OrderLine(ORMBaseClass):
	order_id = orm.ForeignKey(Order)
	sku = orm.ForeignKey(Product)
	qty = orm.IntegerField()
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

In a system like this, the vast majority of your code operates directly on these database-focused models, which makes it a lot harder to reliably write pure functions. Instead, you tend to end up with code that's littered with lots of little reads+writes to the database. Code written this way is hard to unit test (because you have to patch out all of those database interactions), and it tends to grow in complexity over time as maintainers add more and more little reads and writes, because what's the harm in just one more?

The dependency inversion principle is the idea that instead of using database-focused models as the core primitives of your system, you should use simple pure-Python data structures like the frozen dataclass you saw earlier, and _your database models should be derived from those pure-Python models_. [To put it another way](https://www.cosmicpython.com/book/chapter_02_repository.html#_inverting_the_dependency_orm_depends_on_model):

> The ORM imports (or "depends on" or "knows about") the domain model, and not the other way around.

I'd love to work in a system like this someday :)

## Pure Functions

Pure functions[^2] come up now and then throughout the book, although I don't remember the authors spending much time addressing the topic head-on. That's OK, because the book does a great job of showing them in action.

For instance, [Chapter 3](https://www.cosmicpython.com/book/chapter_03_abstractions.html) focuses on a program for syncing files between two directories, and the authors trying to figure out how to make it easy to test. At first, the whole program is concerned with operating directly on the file system, and so in all their tests they have to spin up some temporary directories and write a bunch of files to them and call the program and examine what it did to the temporary directories. Ick!

Then they propose a different approach: "[w]e’re going to separate _what_ we want to do from _how_ to do it". They change the core of their program so that it takes two dicts as input, each representing the files in a directory:

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

In order to test the sync algorithm, the authors don't have to read from and write to the file system any more - they can just pass a couple of dicts into the program, examine the data that it returns as output, and check to see if the program _wants_ to do the right thing. The dicts and tuples that their tests use are trivial to construct, no side effects or mocking/patching necessary.

There's still some code at the edges of their program that a) examines the file system to create those input dicts and b) modifies the file system based off of the instructions in those output commands, but that's an unavoidable fact of life; the main thing that matters is that the bulk of the program is now side-effect-free. Lovely!

This approach is often called ["functional core, imperative shell"](https://www.destroyallsoftware.com/screencasts/catalog/functional-core-imperative-shell)[^3], which is the idea that the bulk of your program should be pure functions with a thin layer at the edges for actually interacting with the real world. I like this idea very much 🙂


## Conclusion

This book was pretty decent, I'd give it 3.5 stars. I'm not going to go write an event-driven microservice-based system with lots of DDD techniques, but it was fun to hear the authors talk about those topics, and I enjoyed their treatment of the ideas above!


[^1]: I have Scott Wlaschin's "Domain Modeling Made Functional" on my desk, and am hoping that that book'll be the one that finally makes DDD click for me. I love his talks on YouTube, I need to go back and watch them all. Brilliant guy.

[^2]: For more info about pure functions: I love the talk "[Hoist Your IO](https://www.youtube.com/watch?v=PBQN62oUnN8)", and [this refactoring exercise](https://youtu.be/vK1DazRK_a0?si=c4onwoql5J7RH1Ty&t=2368) is a great companion piece. [This post](https://tylerayoung.com/2022/03/16/write-more-pure-functions/) is pretty good, too!

[^3]: Oh my gosh, I just found out as I was writing this that Scott Wlaschin just [gave a talk on this exact topic](https://www.youtube.com/watch?v=P1vES9AgfC4)! Added it to my watchlist!
