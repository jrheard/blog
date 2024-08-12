---
layout: post
title:  "Pure Functions"
python_snippets: true
---

The hardest problem in software engineering (aside from choosing _which program to write_) is keeping your program simple enough for maintainers to confidently read, understand, and make changes to. This problem is called "**managing complexity**", and there are lots of famous quotes about it[^1]. Managing complexity is easy when a program is small, but it gets exponentially harder as years pass, the program gets bigger, the engineering organization gets bigger too, and the program's original authors leave.

Pure functions are **my favorite tool** for managing complexity. Let's talk about what they are and why they're so effective. Note: I'll be showing examples in Python, but you can write pure functions in **any** programming language.

## What is a pure function?

We call a function "pure" if it follows these two rules:
1. It always returns the same outputs when given the same inputs.
2. It performs no side effects.

Here are some examples of what I mean when I say "side effects":

* Mutating one of the function's arguments
* Mutating a global variable
* Reading/writing to a database
* Making an HTTP request
* Sending an email
* Sending a push notification
* Firing a missile

## Examples

This is a pure function:

<textarea class="hidden">
# Imagine that this `distance_between` library function is also pure.
from some_library import distance_between

def find_closest_scooter(
    scooters: list[Scooter], point: Point
) -> Scooter | None:
    """Returns the closest Scooter to `point`."""
    if not scooters:
        return None

    distances = [
        distance_between(scooter.location, point)
        for scooter in scooters
    ]

    closest_scooter, smallest_distance = min(
        zip(scooters, distances),
        key=lambda scooter, distance: distance
    )

    return closest_scooter
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

This function is impure:

<textarea class="hidden">
def find_closest_scooter(
    scooters: list[Scooter], point: Point
) -> Scooter | None:
    """Returns the closest Scooter to `point`."""
    if not scooters:
        return None

    for scooter in scooters:
        # XXX: Mutating an input is a side effect!
        scooter.distance = distance_between(scooter.location, point)

    closest_scooter = min(
        scooters,
        key=lambda scooter: scooter.distance
    )

    return closest_scooter
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

This one's **super** impure:

<textarea class="hidden">
def notify_closest_scooter(
    conn: DatabaseConnection, point: Point
) -> None:
    """Sends the user an email about the closest scooter to `point`."""

    # XXX: Reading from the database is a side effect!
    scooters = conn.get_some_scooters_near_point(point)

    if not scooters:
        return

    distances = [
        distance_between(scooter.location, point)
        for scooter in scooters
    ]

    closest_scooter, smallest_distance = min(
        zip(scooters, distances),
        key=lambda scooter, distance: distance
    )

    # XXX: Reading from a global variable violates rule 1!
    email = REQUEST["user_email"]

    # XXX: Sending an email is a side effect!
    send_closest_scooter_email_to_user(email, closest_scooter)
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

## Primary Benefit

We have to put away some our tools when we write pure functions: we can't read from the database, we can't check what time it is, we can't pull an API key from a global config object. What do we get in return?

The primary benefit of pure functions is that they are simple enough to fit into your head. In order to understand what a pure function does, you just need to look at these things:

* What are the function's inputs?
* What are the function's outputs?

By contrast, let's think about impure functions. Here are *some of* the things that you need to think about when you're reading an impure function:

* What are the function's inputs?
    * When the function has finished running, what state will the inputs be in?
    * Will some of the inputs have been mutated? Which ones?
    * Will the inputs be mutated _every_ time the function runs, or only _sometimes_?
* What are the function's outputs? Does it have any?
* What global variables does the function read from?
    * Have those global variables been initialized the way that we expect by the time that this function is called?
    * What happens if they haven't?
* What global variables does the function *write to*?
    * How does that affect the other parts of the program that read those variables?
* What if the database is unreachable?
* What if the API we're calling is down?
* What day of the week is it?
* What is the phase of the moon as seen from Mars?
    * _Which_ moon?

When working with pure functions, you can think about the function in isolation and don't have to worry about fitting the rest of the program into your head. I've heard this described as "local reasoning" (which pure functions enable you to do), as opposed to "global reasoning" (which impure functions *force* you to do).

## Secondary Benefits

As if that weren't enough, you also get these things for free:

* Pure functions are safe to **cache**, since the same inputs always give the same outputs.
* Pure functions are safe to **parallelize**, since they don't mutate anything.
* Pure functions are trivial to **test**, since you don't need to mock anything.

Let's zoom in on that last bullet point, because the difference is really unbelievable. Here's a test for the pure function I showed you earlier:

<textarea class="hidden">
import test_fixtures

def test_find_closest_scooter():
    scooters = [
        test_fixtures.SCOOTER_IN_MIDDLE_OF_OCEAN,
        test_fixtures.SCOOTER_IN_SOUTHEAST_PORTLAND,
        test_fixtures.SCOOTER_IN_TORONTO_CANADA
    ]

    point = test_fixtures.DOWNTOWN_PORTLAND

    assert_equal(
        find_closest_scooter(scooters, point),
        test_fixtures.SCOOTER_IN_SOUTHEAST_PORTLAND
    )
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

Here's a test for the one of the impure functions:

<textarea class="hidden">
from mock import patch

import test_fixtures
from scooters import notify

@patch.object(
    notify,
    "REQUEST",
    {"user_email": "jrheard@zombo.com"}
)
@patch.object(
    notify,
    "send_closest_scooter_email_to_user"
)
def test_notify_closest_scooter(send_email_mock, _request_mock):
    conn = test_fixtures.get_database_connection()

    scooters = [
        test_fixtures.SCOOTER_IN_MIDDLE_OF_OCEAN,
        test_fixtures.SCOOTER_IN_SOUTHEAST_PORTLAND,
        test_fixtures.SCOOTER_IN_TORONTO_CANADA
    ]

    point = test_fixtures.DOWNTOWN_PORTLAND

    with patch.object(
        conn,
        "get_some_scooters_near_point",
        return_value=scooters
    ):
        notify_closest_scooter(conn, point)

    send_email_mock.assert_called_once_with(
        "jrheard@zombo.com",
        test_fixtures.SCOOTER_IN_SOUTHEAST_PORTLAND
    )
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

Which of these two worlds would you rather live in?

## Smells To Watch Out For

* If a function takes no inputs, it's probably impure.
* If a function has no output, it's probably impure.
* If a function is async, it's probably impure.
* If you need to use mocks when testing a function, it's probably impure.

## How To Write Them

It's easiest to write pure functions when you're working with "[plain data](https://blog.jrheard.com/book-report-architecture-patterns-python#value-objects)", i.e. stuff that doesn't have an active connection to the database. You can still make a function pure even if it's operating on database models, though! As long as your function follows the two rules we talked about earlier (i.e. it exercises restraint and doesn't read from or write to the database), it's pure.

I'll bet that a lot of functions in your codebase are just one or two tweaks away from purity. As you get in the habit of looking for side effects, you'll get better at identifying them and yanking them out of the middle of your program.

In [my last post](https://blog.jrheard.com/book-report-architecture-patterns-python), I mentioned a chapter of the book "Architecture Patterns with Python" where the authors transformed the middle of a program into pure code. They did it by following these steps:

1. Load up the data that your pure code will need.
2. Pass that data to a pure function that returns a **decision** about the side effects that the program should perform.
3. Perform those side effects.

If you apply this technique repeatedly, you end up with a program that's primarily made up of pure code, with some impure code at the boundaries. This idea is called "functional core, imperative shell" - Scott Wlaschin has a [great talk](https://www.youtube.com/watch?v=P1vES9AgfC4) with more on this subject, check it out.

Programs written this way contain lots of little functions that can each be easily understood, modified, and tested. As you do your daily work, think about how you can nudge your program a little bit closer toward being shaped like this! 😎


## References
* [Hoist Your I/O](https://www.youtube.com/watch?v=PBQN62oUnN8)
* [Functional Core, Imperative Shell](https://www.youtube.com/watch?v=P1vES9AgfC4) (Scott Wlaschin version)
* [This refactoring exercise](https://www.youtube.com/watch?v=vK1DazRK_a0&t=2368s) from "Solving Problems the Clojure Way"
* [Functional Programming in C++](https://archive.is/zPtaC) (by John Carmack!!)



[^1]: Edsger Dijkstra: "The computing scientist's main challenge is not to get confused by the complexities of his own making." Steve McConnell: "Managing complexity is the most important technical topic in software development." Ben Moseley and Peter Marks: "Complexity is the single major difficulty in the successful development of large-scale software systems." Dr. Pamela Zave: "The purpose of software engineering is to control complexity, not to create it." Bruce Eckel: "Programming is about managing complexity: the complexity of the problem, laid upon the complexity of the machine. Because of this complexity, most of our programming projects fail."
