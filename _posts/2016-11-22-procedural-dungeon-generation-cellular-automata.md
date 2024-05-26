---
layout: post
title:  "Procedural Dungeon Generation: Cellular Automata"
klipse: true
---

Last time we looked at generating random dungeons for [video games](https://github.com/jrheard/voke) using the [Drunkard's Walk]({% post_url 2016-10-31-procedural-dungeon-generation-drunkards-walk-in-clojurescript %}) algorithm. The Drunkard's Walk is fun to play with, and often generates cool levels, but it's also pretty unreliable. That's not good enough for my purposes: I want to reliably generate big, open, cave-like maps, with lots of space for fast-moving enemies to swarm and surround the player.

To that end, we'll be using a [cellular automaton](http://natureofcode.com/book/chapter-7-cellular-automata/) to generate levels that look like this:

<div id="cellular-example"></div>

<script src="{{ site.baseurl }}/assets/js/cellular-blog.js?v={{ site.time }}"></script>
<script>
voke.world.visualize.cellular_example()
</script>

We're still using a 2D grid to represent our level, but we'll be using some new vocabulary this time. Each spot on the grid is now a *cell*. Each cell is either *alive* or *dead*. (An alive cell is a cave wall, and a dead cell is empty space where the player can move around freely.)

The algorithm starts by generating a grid of these cells, each of which has a certain chance of being alive.

<pre class="hidden"><code class="cljs">

(def canvas-id (atom "canvas-1"))

(defn draw-grid
 [grid]
 (let [canvas (js/document.getElementById @canvas-id)
  ctx (.getContext canvas "2d")
  width (count (first grid))
  height (count grid)
  canvas-width (.-width canvas)
  canvas-height (.-height canvas)
  cell-width (/ canvas-width width)
  cell-height (/ canvas-height height)]

  (.clearRect ctx 0 0 canvas-width canvas-height)
  (set! (.-fillStyle ctx) "#CCC")

  (loop [x 0 y 0]

   (when (< y height)
	(when (= (-> grid
			  (get y)
			  (get x))
		   :dead)

	 (doto ctx
	  (.beginPath)
	  (.rect (* x cell-width) (* y cell-height) cell-width cell-height)
	  (.fill)))

	(recur (if (identical? (inc x) width) 0 (inc x))
	 (if (identical? (inc x) width) (inc y) y))))))

(defn highlight-neighbors
[grid x y]
(let [canvas (js/document.getElementById @canvas-id)
  ctx (.getContext canvas "2d")
  width (count (first grid))
  height (count grid)
  canvas-width (.-width canvas)
  canvas-height (.-height canvas)
  cell-width (/ canvas-width width)
  cell-height (/ canvas-height height)]

  (set! (.-fillStyle ctx) "#00ff00")
  (doto ctx
  (.save)
(aset "globalAlpha" 0.3)
(.beginPath)
(.rect (* cell-width (dec x)) (* cell-height (dec y)) (* 3 cell-width) cell-height)
(.fill)
(.beginPath)
(.rect (* cell-width (dec x)) (* cell-height y) cell-width cell-height)
(.fill)
(.beginPath)
(.rect (* cell-width (inc x)) (* cell-height y) cell-width cell-height)
(.fill)
(.beginPath)
(.rect (* cell-width (dec x)) (* cell-height (inc y)) (* 3 cell-width) cell-height)
(.fill)
(.restore))))

(defn draw-grid-highlighted
[grid x y]
(draw-grid grid)
(highlight-neighbors grid x y))

</code></pre>


<pre><code class="cljs" data-preamble='(reset! canvas-id "canvas-1")'>

(defn generate-row
[width alive-probability]
(vec
(take width
(repeatedly #(if (< (rand) alive-probability)
:alive
:dead)))))

(defn generate-grid
[width height alive-probability]
(vec
(take height
(repeatedly #(generate-row width alive-probability)))))

(draw-grid (generate-grid 50 50 0.5))

</code></pre>

<canvas id="canvas-1" width="200" height="200"></canvas>

As usual, all the code snippets in this article are interactive --- try changing that `0.5` to a `0.1` or a `0.99`. You can always focus a snippet and press Ctrl+Enter to rerun it, too![^1]

The basic idea with cellular automata is that we start with an initial grid like the one we've just generated, and then we pretend that its cells are bacteria in a petri dish. We simulate the passage of time, during which cells are born and die.[^2]

The algorithm looks like this:

1. If we've run the simulation `num-iterations` times, we're done.
1. For each cell on the grid,
    1. Calculate the number of its neighbors that are alive.
    1. If the cell is dead and has at least `birth-threshold` alive neighbors, it becomes alive.
	1. If the cell is alive and has at least `survival-threshold` alive neighbors, it stays alive.
	1. Otherwise, the cell is dead.
1. Go back to step 1.

Before we get carried away, let's consider an edge case we'll have to deal with: cells on the outskirts of the grid will have some neighbors that are out of bounds!

<pre><code class="cljs">
(defn spot-is-off-grid?
[grid x y]
(let [height (count grid)
width (count (first grid))]
(or (< x 0)
(>= x width)
(< y 0)
(>= y height))))

(spot-is-off-grid? (generate-grid 5 5 0.5) -1 0)
</code></pre>

For simplicity, we'll say that these nonexistent neighbors are considered to be alive. (As a bonus, this rule tends to give our levels nice solid walls around the edges.)

Now let's write a function that finds a given cell's neighbors. In addition to the `draw-grid` function from last time, I've supplied a `draw-grid-highlighted` function that lets you see what your cell's neighbors look like.

<pre><code class="cljs" data-preamble='(reset! canvas-id "canvas-2")'>
(defn neighbor-values
[grid x y]
(for [i (range (dec x) (+ x 2))
j (range (dec y) (+ y 2))
; We only care about our *neighbors*.
:when (not= [i j] [x y])]
(if (spot-is-off-grid? grid i j)
:alive
(get-in grid [j i]))))

; Let's try it out.
(let [grid (generate-grid 5 5 0.5)
[x y] [2 2]]
(draw-grid-highlighted grid x y)
(neighbor-values grid x y))
</code></pre>

<canvas id="canvas-2" width="200" height="200"></canvas>

Now that we're able to count how many of our neighbors are alive, let's figure out how to determine a cell's new value at each step of the simulation.

<pre><code class="cljs" data-preamble='(reset! canvas-id "canvas-3")'>

(defn new-value-at-position
[grid x y birth-threshold survival-threshold]
(let [cell-is-alive? (= (get-in grid [y x]) :alive)
alive-neighbors (count
(filter #(= % :alive)
(neighbor-values grid x y)))]
(cond
(and cell-is-alive?
(>= alive-neighbors survival-threshold)) :alive
(and (not cell-is-alive?)
(>= alive-neighbors birth-threshold)) :alive
:else :dead)))

; Let's try it out.
(let [grid (generate-grid 5 5 0.5)
[x y] [2 2]]
(draw-grid-highlighted grid x y)
(new-value-at-position grid x y 4 5))
</code></pre>

<canvas id="canvas-3" width="200" height="200"></canvas>

That's all the groundwork we need --- let's implement the algorithm!

<pre><code class="cljs" data-preamble='(reset! canvas-id "canvas-4")'>

(defn automata-iteration
[grid birth-threshold survival-threshold]
(let [height (count grid)
width (count (first grid))]
(loop [new-grid grid
x 0
y 0]

(if (= y height)
; Done!
new-grid

; Otherwise:
(let [new-value (new-value-at-position
grid
x
y
birth-threshold
survival-threshold)]
(recur (assoc-in new-grid [y x] new-value)
(if (= (inc x) width) 0 (inc x))
(if (= (inc x) width) (inc y) y)))))))

(defn automata
[width height initial-probability
birth-threshold survival-threshold iterations]
(nth
(iterate
#(automata-iteration
%
birth-threshold
survival-threshold)
(generate-grid width height initial-probability))
iterations))

(draw-grid
(automata 40 40 0.35 3 5 4))

</code></pre>

<canvas id="canvas-4" width="200" height="200"></canvas>

It... works?

Well, it sure looks like that code is doing *something* to our grid, but it's not easy to tell how we can use this to generate a cool cave like the one we saw at the beginning of this article. This problem is one of the most interesting things about procedural level generation --- whenever you're evaluating an algorithm, you've got to figure out what its inputs are, and try to develop some understanding of how you can manipulate those inputs to get the type of levels that you want.

I didn't pop out of the womb with a well-developed intuition for how birth and survival thresholds affect the shape of caves generated by a cellular automaton, and so I had some trouble figuring out how to proceed when I got to this point. Like last time, building a little tool helped a lot. Try cranking up the number of iterations!

<div id="cellular-tool"></div>

<style>
#cellular-tool .message p {
margin-bottom: 0;
}

#slider-canvas {
margin-bottom: 0.5rem;
}
</style>

After playing around with the different options available, I've settled on using an initial chance of `0.45`, a survival threshold of `4`, and a birth threshold of `5`. This set of parameters seems to reliably generate the specific kind of open cave areas that I'm interested in. Let's try our implementation again, using those values:

<pre><code class="cljs" data-preamble='(reset! canvas-id "canvas-5")'>
(draw-grid
(automata 40 40 0.45 5 4 4))
</code></pre>

<canvas id="canvas-5" width="200" height="200"></canvas>

Looks good! Kinda small, though.

The snippet above runs our code on a little `40x40` grid because this implementation of the algorithm is *really, really slow*, and it takes forever if you run it on e.g. a `100x100` grid. This speed issue is also the reason that these snippets use `4` as their default number of iterations --- in real life, I find that a value around `12` makes for smoother caves.

In a future article, we'll revisit this code and figure out how to make it much faster, and we'll learn a little bit about ClojureScript in the process.

## Wrapping up ##

I learned about today's algorithm from [Kyzrati's post on the topic](http://www.gridsagegames.com/blog/2014/06/mapgen-cellular-automata/). His implementation is a bit different from ours --- he starts by running these birth/survival/death rules on **random, individual cells** a bunch of times, rather than applying them to all cells on the grid at the same time. He then performs several smoothing passes, in which he applies cellular automata rules to the entire grid at once like we've been doing, in order to remove straggling single-cell pillars and cavelets.

I have an implementation that tries to mimic his, and I *think* I like the results it gives, but I've been playing with it for a couple of weeks and frankly I still have no idea what actual effect this run-on-individual-cells-many-times approach has. It does *something*, and it doesn't seem to make the levels worse, so I'm keeping it for now. Give it a shot yourself using [my visualization tool]({{site.baseurl}}/cellular-automata-tool.html).

## Future work ##

There's a lot left to do before these levels are super fun and playable:

* If we generate one of these caves, place the player at one end, and put his goal at the other end, he'll have to do a ton of backtracking along the way in his search for the exit, and that isn't very fun. [Kyzrati's solution](http://www.gridsagegames.com/blog/2014/06/mapgen-cellular-automata/) is to tweak the boundaries of the input grid so that the algorithm generates longer, narrower caves that require less backtracking.
* The algorithm often generates small "island" caves that are completely disconnected from the main cave; I need to write a post-processing step that [detects them](https://en.wikipedia.org/wiki/Flood_fill) and fills them in.

This seems like a good stopping point for now, though. We've written some code that generates neato caves! We'll make it better in future posts.

## Further Reading ##

* [Mapgen: Cellular Automata](http://www.gridsagegames.com/blog/2014/06/mapgen-cellular-automata/)
* [The Cellular Automaton Method for Cave Generation](https://jeremykun.com/2012/07/29/the-cellular-automaton-method-for-cave-generation/)
* [The Nature of Code: Cellular Automata](http://natureofcode.com/book/chapter-7-cellular-automata/)
* [Cellular Automata Method for Generating Random Cave-Like Levels](http://www.roguebasin.com/index.php?title=Cellular_Automata_Method_for_Generating_Random_Cave-Like_Levels)
* [Generate Random Cave Levels Using Cellular Automata](https://gamedevelopment.tutsplus.com/tutorials/generate-random-cave-levels-using-cellular-automata--gamedev-9664)

[^1]: Can we talk about how crazy this is? How many blogs have you ever seen with interactive code snippets like this? [KLIPSE](https://github.com/viebel/klipse/) rules. It's super-easy to use, *and* it can run python, ruby, javascript, plus [other languages too](http://blog.klipse.tech/klipse/2016/09/09/klipse-languages.html). Give it a shot in your blog!
[^2]: This algorithm will seem very familiar to you if you've ever seen [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

<script src="{{ site.baseurl }}/assets/js/seedrandom.min.js?v={{ site.time }}"></script>

<script>
voke.world.visualize.cellular_tool()
</script>

