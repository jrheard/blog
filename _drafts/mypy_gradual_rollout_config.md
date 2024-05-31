---
layout: post
title:  "Configuring Mypy and VS Code for Gradual Adoption in a Preexisting Codebase"
klipse: false
---

I'm going to be introducing [mypy](https://mypy-lang.org/) at work soon. My plan is to start small with my immediate team and then grow adoption from there. I did this about five years ago at my last job and it went pretty well, and I've been putting some thought into what I'll do differently this time. I'll leave some notes on that at the end of this post.

Anyway: one great thing about mypy is that you can introduce it **gradually**. You don't have to annotate your **entire** codebase 100% perfectly before you can start to use mypy; instead, you can just point it at a few files or directories to start off, and then slowly let it start to see more and more files/directories over time.

That's exactly how I did it at my last job, but when I sat down to set mypy up again this time, I realized that I had completely forgotten how to configure it to behave the way I wanted. It took me a few hours of flailing around to figure out what I'd done last time, so that's why I'm writing this post. Hopefully this helps someone else.

## Here's How

I'll cut to the chase - put this in your `mypy.ini`:

```
[mypy]
strict = True
ignore_errors = True

[mypy-util.some_directory.*]
ignore_errors = False

[mypy-backend.models.validation.*]
ignore_errors = False
```

The top-level `ignore_errors = True` declaration tells mypy to not report **any** of the errors that it finds in **any** file. After that, you can build an allowlist of modules that mypy is allowed to complain about by declaring additional `[mypy-foo]` sections and setting `ignore_errors = False` within them.

The end result of this particular `mypy.ini` is that mypy will report any errors it finds in `util/some_directory/` and `backend/models/validation/`, and that's it. Add more `[mypy-foo]` sections over time as you get more files/directories passing under mypy.

It took me a while to get here - I was messing around with `exclude` and `files` for a while, but wasn't getting the results I wanted. The [docs for mypy.ini](https://mypy.readthedocs.io/en/stable/config_file.html) have gotten really long since the last time I looked at them. I must have scrolled by the section on `ignore_errors` like eight times!

## Bonus Section: Adoption/Rollout Plan

One great thing about this go-around is that everybody at work seems very excited about mypy. Last time I had to do a fair amount of convincing, and it was touch and go for a while; this time couldn't be more different. I think that the main reason for this difference is that Typescript has been around for an additional five years, and a lot of folks at work have already gone through the before/after process of using it instead of vanilla JavaScript. Why *wouldn't* you want that experience in your Python code too?

I had gone into this process expecting to have to spend a ton of time and energy convincing people that mypy is worth trying out, and once I discovered that I won't need to do that, I spent a while thinking about what I'll be spending that time and energy on instead. Here's my rough plan:

* Add mypy as a dev dependency, and configure it to only look at a directory I just added that has like two files in it. Pin the version so that I don't get super embarrassed when they eventually release a new stricter version and CI suddenly breaks for no obvious reason many months from now (this happened last time 😓).
* **Don't** add mypy to CI yet, even though mypy is only looking at one directory. I don't want to risk a situation where someone who doesn't know mypy exists edits a random file a month from now and suddenly their PR fails CI for reasons that they don't understand. People shouldn't be surprised by mypy, they should be excited about it.
* Set up the [VSCode mypy extension](https://github.com/microsoft/vscode-mypy) and document the config options I recommend using for our codebase. From this point onward, people who opt into using the extension will start reaping the benefits of mypy even though it's not running in CI.
* Write **really good internal docs** on what mypy is and why/how we're using it.
    * Include a getting-started guide, a brief FAQ where I discourage people from writing `#type: ignore` comments, and a [link to the cheatsheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html).
    * Point out that `reveal_type()` is useful.
    * Explain that mypy understands the use of an `if` statement to narrow the type of a variable.
    * Explain when it's appropriate to use an `assert`.
    * **Make it very clear that I am the go-to person for helping anyone with any mypy question**. I love it when people come to me with weird mypy problems, it's fun to fix them.
    * Write a guide on how to get a file/directory passing under mypy for the first time. Explain when and how to add new sections to `mypy.ini`.
* Give a ~20-minute presentation/demo to the folks on my immediate team. Record it and make it available to other folks who are particularly interested in mypy, but don't yet make a big deal out of it; this presentation is a practice run for the big one. Encourage my teammates to start using mypy in their day-to-day work.
* At least a couple of weeks later, once I've had a chance to think about how the last presentation went: give an engineering-org-wide lunch-and-learn presentation on mypy.
    * Explain what it is and why it's good; do a medium-length live demo; and spend the rest of the time talking about my vision for the adoption process.
    * Maybe briefly scroll through a few examples of live production crashes I've seen that would have been prevented by mypy (haven't decided about this one, don't want to make anyone feel bad).
    * Say at least five times that I am personally on the hook for making our mypy adoption experience a smooth one, and people can ask me about mypy any time. Try to communicate that mypy questions genuinely bring me great joy.
    * Maybe someone on my team will have had such a great experience with mypy that they'll want to speak up for a second and say how nice it is?
    * Q&A
* When the time is right: add mypy to CI! Encourage continued adoption!
* Keep an eye on our internal mypy docs - make sure that they stay up to date, and make sure that they contain obvious fixes for any gotchas / rough edges that we encounter.
* Keep an eye out for new mypy versions and update to them as appropriate. I subscribe to the mypy blog in feedly because I am a super cool dude 😎
* Live happily ever after!

That's the plan, we'll see how it goes! Can't wait!
