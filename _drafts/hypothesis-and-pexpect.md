---
layout: post
title:  "Using Hypothesis and Pexpect to Test High School Programming Assignments"
---

<style>
pre .CodeMirror:nth-of-type(2) {
display: none;
}
</style>

Like I've [mentioned before]({{site.baseurl}}{% post_url 2017-11-30-watercolorbot %}), I'm spending the 2017-18 school year volunteering in a few tech classes at a local high school. My main focus is on a beginner Python course, where I've been coming up with [fun]({{site.baseurl}}/python/passwords) [projects]({{site.baseurl}}/python/caesar) for the students to work on.

Most of these early projects have been simple command-line programs that prompt the user for some input, perform some calculation, and print some output. For instance, here's the password checker program:

<asciinema-player src="{{ site.baseurl }}/password_checker_cast.json?v=1" rows="12" cols="90" autoplay="true"></asciinema-player>

The program should prompt the user for their username, student ID, and password, and it should print out the string GOOD or BAD to indicate whether the password is "valid" or not (see the [assignment writeup]({{site.baseurl}}/python/passwords) for more details).

When a student finishes their password checker, we need to examine it to see whether or not the student programmed it correctly. We have around thirty students, and the checker program needs to satisfy a variety of constraints, and students often don't get them all right the first time, so each student will usually submit several versions of the checker.

Testing submitted password checkers a jillion times by hand sounded pretty awful, so I decided to write an automated test suite to do this for us.

Pexpect
=======

These students hadn't learned about functions yet, so their programs didn't have an `is_password_good(password)` function that I could import and unit-test. Instead, I needed to write code that would run the student's program, send it several lines of input, and read its output.

My first instinct was to use the [subprocess library](https://docs.python.org/3/library/subprocess.html) to do this, but I had trouble getting that to work. I needed to send a line to the program, then wait and then send another line, and then wait and send a third line; but `subprocess.Popen` appears to only be able to send a single line of input to programs it spawns. I Googled around and found a bunch of StackOverflow questions about this exact issue, and they all said to use [Pexpect](https://github.com/pexpect/pexpect) instead.

Pexpect is a library that lets you spawn an interactive command-line program and control it as it runs; it lets you feed the program multiple lines of input and read lines of its output. Which is the specific thing I just said I needed to do!

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

I also wrote a couple of helper functions, `assert_good()` and `assert_bad()`.

Finally, I wrote some standard unit tests:

<pre><code class="py">
def test_literal_password(checker):
    assert_bad('password', checker)

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

Those checkmarks are so soothing.

A week later, I stumbled across Hypothesis and realized that my tests had a lot of room for improvement.

Hypothesis
==========



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
