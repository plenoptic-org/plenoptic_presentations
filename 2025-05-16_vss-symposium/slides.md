![](assets/plenoptic_logo_wide.svg) <!-- .element: style="height:50%" -->

## A python library for synthesizing model-optimized visual stimuli
## Billy Broderick <!-- .element: style="height:50%" -->

#note: today I'm going to talk about plenoptic, a python library for synthesizing the model-optimized visual stimuli we're talking about it in this session. but first, I'm going to step back a bit

---

<h2 class="fragment disappear" data-fragment-index=0>Unpacking plenoptic logo</h2>
<h2 class="fragment appear-disappear" data-fragment-index=0>Simulate responses</h2>
<h2 class="fragment appear-disappear" data-fragment-index=1>Fit parameters</h2>
<h2 class="fragment appear-disappear" data-fragment-index=2>Synthesize stimuli</h2>

<div data-animate data-load="assets/plen-synth-4.svg">
<!-- {"setup": [
{"element": "#g1", "modifier": "attr", "parameters": [ {"class": "fragment appear-disappear", "data-fragment-index": "0"} ]},
{"element": "#g2", "modifier": "attr", "parameters": [ {"class": "fragment appear-disappear", "data-fragment-index": "1"} ]},
{"element": "#g3", "modifier": "attr", "parameters": [ {"class": "fragment appear-disappear", "data-fragment-index": "2"} ]}
]} -->
</div>

#note: To make that slightly less abstract, here is a diagram of a model in visual neuroscience. it accepts some stimuli s, often for us images, as inputs, and based on some parameters theta, returns some responses r. these responses can be anything of interst to the experimenter, such as predicted spike rates or image class, if this were doing image net

- now the way that models are most commonly used, is that we feed them an input and some parameter values and we simulate the responses.

- we often pretty regularly fix the responses for a set of stimuli and use backpropagation to fit the parameters

- but there's nothing special about the stimuli. we can similarly hold both the responses and parameters constant and use back propagation to generate novel stimuli. 

this is what we call synthesis -- updating the pixel values of an image based on a model with set parameter values and some intended output.

---

## Why do this?

- Better understand computational visual models. <!-- .element: class="fragment margin-top" data-fragment-index="1" -->
- Build better models. <!-- .element: class="fragment margin-top" data-fragment-index="2" -->

---

## Image space is big!

<div data-animate data-load="assets/image_space.svg">
<!-- {"setup": [
{"element": "#path2-3", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]},
{"element": "#text13-5", "modifier": "attr", "parameters": [ {"class": "fragment appear-disappear", "data-fragment-index": "0"} ]},
{"element": "#g13", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]},
{"element": "#text11", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "2"} ]},
{"element": "#text3", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "3"} ]},
{"element": "#rect13", "modifier": "attr", "parameters": [ {"class": "fragment disappear", "data-fragment-index": "4"} ]},
{"element": "#rect13-6", "modifier": "attr", "parameters": [ {"class": "fragment disappear", "data-fragment-index": "5"} ]},
{"element": "#rect13-6-7", "modifier": "attr", "parameters": [ {"class": "fragment disappear", "data-fragment-index": "6"} ]},
{"element": "#rect13-6-7-5", "modifier": "attr", "parameters": [ {"class": "fragment disappear", "data-fragment-index": "7"} ]},
{"element": "#image15239", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "8"} ]},
{"element": "#text14", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "9"} ]}
]} -->
</div>

---
## ... but do we need to explore it all?

<div data-animate data-load="assets/image_space-2.svg">
<!-- {"setup": [
{"element": "#g3", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]},
{"element": "#g1", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]},
{"element": "#g7", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "2"} ]},
{"element": "#g5", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "3"} ]},
{"element": "#g6", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "4"} ]},
{"element": "#g4", "modifier": "attr", "parameters": [ {"display": "none"} ]},
{"element": "#g8", "modifier": "attr", "parameters": [ {"display": "none"} ]}
]} -->
</div>

---

## AlexNet Adversarial Examples 

<div data-animate data-load="assets/image_space-2.svg">
<!-- {"setup": [
{"element": "#g8", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]},
{"element": "#g10", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]}
]} -->
</div>
