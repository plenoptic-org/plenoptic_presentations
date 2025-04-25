<!-- outline
15-20 minutes
* background
  * what are metamers 
    * trichromacy: picture of room, show wavlelengths to cone responses, like on conceptual intro page
  * this was originally done with color matching, then you got linear algebra, which gave you closed form solution
* but models that are more complex require optimization
  * plenoptic comes out of Eero's lab, where this kind of work dates tot he late 90s
  * and required a lot of computing gradients by hand
* now we have autodiff and more specifically, pytorch
  * schematic of image -> model -> response
  * add second, showing white noise, different response, and difference between the responses
  * as long as this is done in pytorch, can differentiate for us and run
  * update image and scatter? so they align
* plenoptic takes advantage of this: goals and contents
  * goals
    * facilitate model-optimized stimulus generation
    * compatible with any pytorch model: list examples
    * include helpful vision science models
    * documented, tested, easy-to-install, modular, open source
  * contents
    * synthesis methods with one-sentence description and citations
    * models and metrics, with glyphs
    * canonical computations
    * tools?
* example code
  * simplest example just loads in image, instantiates model, initializes synthesis, runs it, and visualizes
  * then swap out different portions: use GPU, swap target image, swap model (show ours, model zoo, custom), change init image / optimizer, synth method
* conclude: return to goals and content?
  * mention work is ongoing
* advertisement slide
-->


# Slide 1

```python data-line-numbers
>>> import plenoptic as po
>>> po.data.einstein()
```

---
# Slide 2

{: class="margin-top column" style="float:left; width:60%"}
```python  data-line-numbers doctest:scripts/test.py:test data-line-numbers
```

![](assets/test.png)

---
# Slide 2

```python doctest:scripts/test.py:test data-line-numbers data-line-numbers
```

![](assets/test.png)

---
# Slide 3

{: class="margin-top column" style="float:left; width:60%"}
```python data-line-numbers doctest:scripts/test.py:test2
```

<div class='margin-top column ' data-fragment-index="0" style="float:right; width:35%">
<video data-autoplay src="assets/test.mp4"></video>
</div>
