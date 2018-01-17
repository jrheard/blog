---
layout: post
title:  "Using Hypothesis and Pexpect to Test High School Programming Assignments"
---

<style>
pre .CodeMirror:nth-of-type(2) {
display: none;
}
</style>

I've been coming up with some [fun][passwords] [projects][caesar] for a [beginner Python high school class][wcb]. Most of these projects are simple command-line programs that prompt the user for some input, perform some calculation, and print some output. For instance, here's the password checker project:

<asciinema-player src="{{ site.baseurl }}/password_checker_cast.json?v=1" rows="12" cols="90" autoplay="true"></asciinema-player>

The program should prompt the user for their username, student ID, and password, and it should print out the string GOOD or BAD to indicate whether the password is "valid" or not (see the [assignment writeup][passwords] for more details).

Testing
=======

When a student finishes their password checker, we need to examine it to see whether or not the student programmed it correctly. We have around thirty students, and the checker program needs to satisfy a variety of constraints, and students often don't get them all right the first time, so each student will usually submit several versions of the checker.

Testing submitted password checkers a jillion times by hand ("does the latest version of Jane's checker correctly reject `abcd`? How about `$!@#5555`?") sounded pretty awful, so I decided to write an automated test suite to do this for us.

These students hadn't learned about functions yet, so their programs didn't have an `is_password_good(password)` function that I could import and unit-test. Instead, I needed to write code that would run the student's program, send it several lines of input, and read its output.

My first instinct was to use the [`subprocess` library](https://docs.python.org/3/library/subprocess.html) to do this, but I had trouble getting that to work. I needed to send a line to the program, then wait and then send another line, and then wait and send a third line; but the `subprocess` library's API isn't particularly well-suited for this use case. I Googled around and found a bunch of StackOverflow questions written by people in my exact situation, and the answers all said to use [Pexpect](https://github.com/pexpect/pexpect) instead.

Pexpect
=======

Pexpect is a library with a nice API that lets you start a program, feed it as many lines of input as you want, and read as many lines of output as you want.

Here's the code I used to drive students' password-checker programs.

<pre><code class="py">
def get_checker_output(password, checker):
	program = pexpect.popen_spawn.PopenSpawn('python ' + checker)
	program.sendline('jrheard')
	program.sendline('12345')
	program.sendline(password)

	lines = program.read().decode('utf-8').splitlines()
	return filter(bool, lines)[-1]
</code></pre>

It's interesting to note that `pexpect.popen_spawn.PopenSpawn` [uses the `subprocess` library](https://github.com/pexpect/pexpect/blob/master/pexpect/popen_spawn.py#L46) under the hood.

I also wrote a couple of helper functions, `assert_good()` and `assert_bad()`. Finally, I wrote some standard unit tests:

<pre><code class="py">
def test_too_short_rejected(checker):
    assert_bad('A!1', checker)

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
</code></pre>

I hand-wrote around twenty assertions like those and called it a day. It was very satisfying to run the resulting tests:

<asciinema-player src="{{ site.baseurl }}/hypothesis_pexpect_cast_1.json?v=1" rows="20" cols="90" autoplay="true" loop="true"></asciinema-player>

Those checkmarks are so soothing!

A week later, though, I stumbled across Hypothesis and realized that my tests had a lot of room for improvement.

Hypothesis
==========

[Hypothesis][hypothesis] is a "property-based testing" library for Python. Its homepage explains what that means:

> Hypothesis runs your tests against a much wider range of scenarios than a human tester could, finding edge cases in your code that you would otherwise have missed.

Here's an example to give you a better idea of what this actually means. Earlier, I showed you a test called `test_too_short_rejected()`, which asserts that the password `A!1` is marked BAD, because the password checker is supposed to reject passwords that are shorter than eight characters.

This is an "example-based test", which means that I wrote it by hand using an example password that I came up with off the top of my head. This test is actually pretty flimsy, because it only checks to see if `A!1` is rejected—but if the student's checker incorrectly allows a seven-character-long string like `A!12345`, my test won't catch that! I could add more examples, but that isn't very fun, and even if I added five more examples my test wouldn't be very exhaustive.

Here's how to use Hypothesis to enhance that test.

<pre><code class="py">
# This becomes a string like 'a..zA..Z0..9!..,'.
VALID_PASSWORD_CHARACTERS = string.ascii_letters + \
	string.digits + \
	'!@#$%^&*()-_=+.,'

@given(password=st.text(alphabet=VALID_PASSWORD_CHARACTERS,
						max_size=7))
def test_too_short_rejected(password, checker):
	assert_bad(password, checker)

</code></pre>

The `@given` decorator is what makes the magic happen. It tells Hypothesis: run this test a bunch of times with a random password (containing any of these characters, up to seven characters max) each time.

When you add Hypothesis to your tests, you'll usually find a ton of bugs in your code which your previous hand-written tests hadn't found. This is good! Fix those bugs and think happy thoughts about the authors of Hypothesis.

TALK MORE ABOUT WHAT PROPERTY BASED TESTING MEANS

PUT SOME MORE STUFF IN THE MIDDLE HERE, USE THIS CAST NEAR THE END OF THE POST

If your test passes and you'd like to convince yourself that Hypothesis isn't slacking off, you can use the [`HYPOTHESIS_VERBOSITY_LEVEL` environment variable][hypothesis-verbose] to see what Hypothesis is generating, like this:

<asciinema-player src="{{ site.baseurl }}/hypothesis_cast.json?v=1" rows="16" cols="90" autoplay="true" loop="true"></asciinema-player>








[wcb]: {{site.baseurl}}{% post_url 2017-11-30-watercolorbot %}
[passwords]: {{site.baseurl}}/python/passwords
[caesar]: {{site.baseurl}}/python/caesar
[hypothesis]: http://hypothesis.works/
[hypothesis-verbose]: http://hypothesis.readthedocs.io/en/latest/settings.html#seeing-intermediate-result




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
