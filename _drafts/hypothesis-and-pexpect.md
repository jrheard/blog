---
layout: post
title:  "Using Hypothesis and Pexpect to Test High School Programming Assignments"
---

<style>
.cm-s-friendship-bracelet {
	font-size: 16px;
}
</style>

I've been coming up with some [fun][passwords] [projects][caesar] for a [beginner Python high school class][wcb]. Most of these projects are simple command-line programs that prompt the user for some input, perform some calculation, and print some output. For instance, here's the password checker project:

<asciinema-player src="{{ site.baseurl }}/password_checker_cast.json?v=1" rows="12" cols="90" autoplay="true"></asciinema-player>

This program should prompt the user for their username, student ID, and password, and it should print out the string GOOD or BAD to indicate whether or not the password is "valid" (see the [assignment writeup][passwords] for more details).

Testing
=======

When a student finishes their password checker, we need to examine it to see whether or not the student programmed it correctly. We have around thirty students, and the checker program needs to satisfy a variety of constraints, and students often don't get them all right the first time, so each student will usually submit several versions of the checker.

Testing submitted password checkers a jillion times by hand ("does the latest version of Jane's checker correctly reject `abcd`? How about `$!@#5555`?") sounded pretty awful, so I decided to write a program to do this for us.

These students hadn't learned about functions yet, so their programs didn't have an `is_password_good(password)` function that I could import and unit-test. Instead, I needed to write code that would run the student's program, send it several lines of input, and read its output.

My first instinct was to use [the `subprocess` library](https://docs.python.org/3/library/subprocess.html) to do this, but I had trouble getting that to work. I needed to send a line to the program, then wait and then send another line, and then wait and send a third line; but the `subprocess` library's API isn't particularly well-suited for situations where you want to send a program more than one line of input. I Googled around and found a bunch of StackOverflow questions written by people in my exact situation, and the answers all said to use `pexpect` instead.

Pexpect
=======

[Pexpect][pexpect] is a library that lets you start a program, feed it as many lines of input as you want, and read as many lines of output as you want.

Here's how to use pexpect to operate the password-checker program you saw earlier:

<textarea class="hidden">
def get_checker_output(password, checker):
	program = pexpect.popen_spawn.PopenSpawn('python ' + checker)
	program.sendline('jrheard')
	program.sendline('12345')
	program.sendline(password)

	lines = program.read().decode('utf-8').splitlines()
	# Return the last line of the program's output,
	# which should be a string like 'GOOD' or 'BAD'.
	return filter(bool, lines)[-1]
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

(It's interesting to note that `pexpect.popen_spawn.PopenSpawn` [uses the `subprocess` library](https://github.com/pexpect/pexpect/blob/master/pexpect/popen_spawn.py#L46) under the hood.)

Once I had that working, I wrote some standard unit tests.

<textarea class="hidden">
def test_contains_student_id(checker):
    assert_bad('jifoaw12345@!#*LKJFSklfaew', checker)

def test_two_categories(checker):
    assert_bad('JIFEOWjiofewajife', checker)
    assert_bad('13283248JIOFEWOI', checker)
    assert_bad('faewjio*(#$@$', checker)
    assert_bad('$#*(($#@83248', checker)
    assert_bad('jioaew123345', checker)

def test_exactly_eight_characters(checker):
    assert_good('abc123!P', checker)

# Remember this one for later!
def test_too_short_rejected(checker):
    assert_bad('A!1', checker)
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

I hand-wrote around twenty assertions like those and called it a day. It was very satisfying to run the resulting tests, and I felt great about all the time I was saving by not having to laboriously verify students' programs by hand.

A week later, though, I stumbled across Hypothesis and realized that my tests had a lot of room for improvement.

Hypothesis
==========

[Hypothesis][hypothesis] is a **[property-based testing](http://blog.jessitron.com/2013/04/property-based-testing-what-is-it.html)** library. Its homepage says:

> Hypothesis runs your tests against a much wider range of scenarios than a human tester could, finding edge cases in your code that you would otherwise have missed.

Earlier, I showed you a test called `test_too_short_rejected()`. That test asserts that the password `A!1` is marked "BAD", because the password checker is supposed to reject passwords that are shorter than eight characters.

<textarea class="hidden">
def test_too_short_rejected(checker):
    assert_bad('A!1', checker)
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

This is an **example-based test**, which means that I wrote it by hand using an example too-short password that I came up with off the top of my head.

This test is actually pretty flimsy, because it only checks to see if `A!1` is rejected—but if the student's checker program incorrectly allows a seven-character-long password like `A!12345`, my test won't catch that bug, because I didn't think to include that example in my test. I could add more examples to my test, but that isn't very fun; and even if I did think really hard and came up with five more examples, my test still wouldn't be very exhaustive, because students are very good at coming up with bugs that I wouldn't think to test for.

How To Use Hypothesis
---------------------

Let's use Hypothesis to improve this test. We'll start by adding the `@given` decorator:

<textarea class="hidden">
@given(password=TODO_DEFINE_ME)
def test_too_short_rejected(password, checker):
    assert_bad(password, checker)
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

When Hypothesis sees a test that's annotated with the `@given` decorator, it runs that test a bunch of times. This test's decorator says that it wants a random `password` argument, so Hypothesis will give the test a random password each time it's run.

We're halfway there—all we have to do now is tell Hypothesis how to generate too-short passwords.

A too-short password is a string with some characters in it. Those characters can be the lowercase letters a-z, the uppercase letters A-Z, the digits 0-9, and some specific symbols given in the assignment writeup. Since we only want to generate passwords that are "too short", a too-short password can have at most seven characters.

Here's how to say that to Hypothesis:

<textarea class="hidden">
VALID_PASSWORD_CHARACTERS = string.ascii_letters + string.digits + '!@#$%^&*()-_=+.,'

short_password_strat = st.text(alphabet=VALID_PASSWORD_CHARACTERS,
                             max_size=7)
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>


`st.text()` returns a **strategy**, which is an object that Hypothesis can use to generate random data. Hypothesis has a [ton of these][strategies] that you can use to generate all sorts of stuff.

When we give `short_password_strat` to the `@given` decorator, Hypothesis will generate random passwords like these whenever it runs our test:

<textarea class="hidden">
'yKbSH7)'
'aa'
',xcc69'
'#g^teH'
'pbFr'
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>


That's all there is to it - now that we know how to generate random too-short passwords, we can convert our example-based test to a property-based test.

<textarea class="hidden">
@given(password=short_password_strat)
def test_too_short_rejected(password, checker):
       assert_bad(password, checker)
</textarea>
<pre class="cm-s-friendship-bracelet"></pre>

We're done! That wasn't so hard.

Here's what our test looks like in action—in this recording, I've put Hypothesis into verbose mode using the [HYPOTHESIS_VERBOSITY_LEVEL][hypothesis-verbose] environment variable so that we can see the random passwords that it generates.

<asciinema-player src="{{ site.baseurl }}/hypothesis_cast.json?v=1" rows="16" cols="90" autoplay="true" loop="true"></asciinema-player>

What It Feels Like To Use Hypothesis
------------------------------------

It feels really good.

Before Hypothesis, this is how I felt about writing tests:

> Oh geez, I've gotta test this program. OK, what are a bunch of possible example inputs that might cause it to crash or behave incorrectly? Let's write a test for each of those and hope that's good enough.

It was never good enough, and it was never fun.

TODO tlak more about what it's like to use hypothesis


TODO talk about shrinking

TODO talk about failure database





[wcb]: {{site.baseurl}}{% post_url 2017-11-30-watercolorbot %}
[passwords]: {{site.baseurl}}/python/passwords
[caesar]: {{site.baseurl}}/python/caesar
[pexpect]: https://github.com/pexpect/pexpect
[hypothesis]: http://hypothesis.works/
[hypothesis-verbose]: http://hypothesis.readthedocs.io/en/latest/settings.html#seeing-intermediate-result
[strategies]: http://hypothesis.readthedocs.io/en/latest/data.htm





{% javascript asciinema-player %}
{% javascript codemirror %}
{% javascript codemirror_python %}
{% javascript codemirror_runmode %}


<script>
var textAreas = document.getElementsByTagName("textarea");
var pres = document.querySelectorAll("pre.cm-s-friendship-bracelet");

for (var i = 0; i < textAreas.length; i++) {
	CodeMirror.runMode(textAreas[i].value, "python", pres[i]);
}
</script>
