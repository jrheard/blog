---
layout: post
title:  "Procedural Dungeon Generation: A Drunkard's Walk in ClojureScript"
cljs_klipse: true
---

<style>

#slider-ui .message p {
margin-bottom: 0;
}

#slider-canvas {
margin-bottom: 0.5rem;
}

#slider-ui input {
width: 100%;
}

</style>


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
		   :empty)

	 (doto ctx
	  (.beginPath)
	  (.rect (* x cell-width) (* y cell-height) cell-width cell-height)
	  (.fill)))

	(recur (if (identical? (dec x) width) 0 (inc x))
	 (if (identical? (dec x) width) (inc y) y))))))
</code></pre>

I'm working on a toy [game](http://github.com/jrheard/voke), and figured it'd be fun to learn how to write code that generates random levels for it. I'd like to show you a simple algorithm for level generation called the [Drunkard's Walk](http://www.roguebasin.com/index.php?title=Random_Walk_Cave_Generation). It generates levels that look like this:

<canvas id="canvas-4" width="400" height="400"></canvas>

<div class="button-wrapper">
<a class="button" id="generate-button">generate another</a>
</div>

As you can see, our level is a two-dimensional grid. Each cell on the grid is either empty or full. If it's empty, the player can wander around in there and find monsters and gold and items and stuff. If it's full, then it's a cave wall and the player smacks into it.

The Drunkard's Walk algorithm starts with a totally-filled-in level and then hollows it out one cell at a time, so let's start by defining a function that creates a filled-in level.

<pre><code class="cljs">
(defn full-grid
 [width height]
 (vec (repeat height
	   (vec (repeat width :full)))))

(full-grid 3 5)

</code></pre>

All of the code snippets in this article are interactive - go ahead and change that last line to <code>(full-grid 10 10)</code> and see what happens.

Our <code>full-grid</code> function is a good start, but its output doesn't really look like a cave. Let's fix that. I've provided a <code>draw-grid</code> function that takes a grid and draws it for you, like this:

<pre><code class="cljs" data-preamble='(reset! canvas-id "canvas-1")'>
(draw-grid (full-grid 10 10))
</code></pre>

<canvas id="canvas-1" width="200" height="200"></canvas>

That's not a very interesting cave. Let's try it again with a few empty cells carved out by hand, just so we're sure that this <code>draw-grid</code> function actually works.

<pre><code class="cljs" data-preamble='(reset! canvas-id "canvas-2")'>
(-> (full-grid 10 10)
 (assoc-in [1 2] :empty)
 (assoc-in [8 5] :empty)
 (assoc-in [5 9] :empty)
 draw-grid)

</code></pre>

<canvas id="canvas-2" width="200" height="200"></canvas>

Did I mention all the code in this article is interactive? Play around with it, go nuts. Hollow out some more cells. Make the whole level empty. Remove the <code>draw-grid</code> call to see what our actual 2D grid datastructure looks like when some of its cells have been hollowed out.

Okay, so the Drunkard's Walk algorithm looks like this:

1. Pick a random cell on the grid as a starting point.
1. If we've carved out enough empty spots, we're done.
1. Walk one step in a random cardinal direction - north, south, east, or west, no diagonals - and carve out that new spot.
1. Go back to step 2.

We're almost ready to implement it, but first let's define a little helper function that we'll use to make sure that we stay within the bounds of our grid and don't try to walk off into the gaping void beyond.

<pre><code class="cljs">

(defn bound-between
 [number lower upper]
 (cond
  (< number lower) lower
  (> number upper) upper
  :else number))

(bound-between 10 0 9)

</code></pre>

Okay, here we go!

<pre><code class="cljs" data-preamble='(reset! canvas-id "canvas-3")'>

(defn drunkards-walk
 [grid num-empty-cells]
 (let [height (count grid)
  width (count (first grid))]
  ; Guard against impossible demands.
  (when (<= num-empty-cells (* width height))

  (loop [grid grid
   ; Step 1: pick a random cell.
   x (rand-int width)
   y (rand-int height)
   empty-cells 0]

   ; Step 2: if we're done, return the grid.
   (if (= empty-cells num-empty-cells)
	grid

	(let [cell-was-full? (= (get-in grid [y x]) :full)
	 ; Step 3: walk one step in a random direction.
	 direction (rand-nth [:north :east :south :west])]

	 ; Step 4: back to step 2.
	 (recur (assoc-in grid [y x] :empty)
	  (case direction
	   :east (bound-between (inc x) 0 (dec width))
	   :west (bound-between (dec x) 0 (dec width))
	   x)
	  (case direction
	   :north (bound-between (dec y) 0 (dec height))
	   :south (bound-between (inc y) 0 (dec height))
	   y)
	  (if cell-was-full?
	   (inc empty-cells)
	   empty-cells))))))))

(-> (full-grid 40 40)
 (drunkards-walk 350)
 draw-grid)
</code></pre>

The fruits of our labor:

<canvas id="canvas-3" width="400" height="400"></canvas>

Focus the code snippet above and then press Control+Enter a few times to generate some more levels. Neat, huh? Go on, make it a 200x200 grid and carve out 5000 cells.

When looking at generated levels, I often find myself wondering: what exactly happened to make the level turn out this way? I've come up with a little tool that helps answer that question for this particular algorithm. Try dragging this slider around.

<div id="slider-ui"></div>
<script src="{{ site.baseurl }}/assets/js/drunkards-blog.js?v={{ site.time }}"></script>
<script src="{{ site.baseurl }}/assets/js/seedrandom.min.js?v={{ site.time }}"></script>
<script>
voke.world.visualize.drunkards_blog()
</script>

So, that's the Drunkard's Walk. I learned about it from [Kyzrati's excellent introductory blog post on procedural map generation](http://www.gridsagegames.com/blog/2014/06/procedural-map-generation/). It usually generates surprisingly cavelike levels, and they will always be connected — there will never be two separate subcaves that are separated from each other by a wall.

The bad news: you probably don't want to actually use this to generate levels for a video game. The main problem with it is that it's **unreliable** — it's so dang random that sometimes it'll generate super cool tunnely cavey levels, and sometimes it'll just generate a boring-looking blob. It's pretty fun to play with, though!

Don't worry, we'll look at a more useful algorithm next time 👍

<pre class="hidden"><code class="cljs">

(defn draw-top-canvas []
(reset! canvas-id "canvas-4")
(-> (full-grid 40 40) (drunkards-walk 400) draw-grid))

(draw-top-canvas)

(-> "generate-button"
 (js/document.getElementById)
 (.addEventListener "click"  (fn [e]
							 (draw-top-canvas))))
</code></pre>
