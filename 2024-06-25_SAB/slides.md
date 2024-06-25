# plenoptic

## SAB Meeting
## June 25, 2024

---

<div data-animate data-load="assets/plen-1.0.1-intro-2.svg">
<!-- {"setup": [
{"element": "#rect4749", "modifier": "attr", "parameters": [ {"class": "fragment appear-disappear", "data-fragment-index": "0"} ]}
]} -->
</div>

#note: so I'm going to talk about plenoptic, which is a python library that performs "model-based synthesis of perceptual stimuli" to help better understand those computational models. I'm going to briefly describe what that means. key word is "synthesis"

we've represented synthesis with this little abstract logo. This represents the relationship between computational models, their inputs, outputs, and parameters.

---

<h2 class="fragment disappear" data-fragment-index=0>Visual model</h2>
<h2 class="fragment appear-disappear" data-fragment-index=0>Simulate responses</h2>
<h2 class="fragment appear-disappear" data-fragment-index=1>Fit parameters</h2>
<h2 class="fragment appear-disappear" data-fragment-index=2>Synthesize stimuli</h2>

<div data-animate data-load="assets/plen-synth-4.svg">
<!-- {"setup": [
{"element": "#rect6595-6", "modifier": "attr", "parameters": [ {"class": "fragment appear-disappear", "data-fragment-index": "0"} ]},
{"element": "#rect6595-7", "modifier": "attr", "parameters": [ {"class": "fragment appear-disappear", "data-fragment-index": "1"} ]},
{"element": "#rect6595", "modifier": "attr", "parameters": [ {"class": "fragment appear-disappear", "data-fragment-index": "2"} ]}
]} -->
</div>

#note: To make that slightly less abstract, here is a diagram of a model in visual neuroscience. it accepts some stimuli s, often for us images, as inputs, and based on some parameters theta, returns some responses r. these responses can be anything of interst to the experimenter, such as predicted spike rates or image class, if this were doing image net

- now the way that models are most commonly used, is that we feed them an input and some parameter values and we simulate the responses.

- we often pretty regularly fix the responses for a set of stimuli and use backpropagation to fit the parameters

- but there's nothing special about the stimuli. we can similarly hold both the responses and parameters constant and use back propagation to generate novel stimuli. 

this is what we call synthesis -- updating the pixel values of an image based on a model with set parameter values and some intended output.

---
## Metamers
Physically distinct stimuli that are perceptually identical

#note: one such method is metamer synthesis. in the study of perception, metamers are physically distinct stimuli that are perceptually identical.

the classic example of metamers come from color perception.

---
## Metamers
![](assets/plen-metamer-podium.svg) <!-- .element: style="margin-top:5%;height:950px;width:auto" -->

#note: when you look at this picture of this room, compared to the room in real life, they look like they're the same color. however, the physical light that is entering your eye is *very* different, because this projector only has three color channels (RGB), and so it cannot hope to exactly match the energy at every wavelength in the visual light spectrum

however, it doesn't need to

---
## Metamers
![](assets/plen-metamer-cones.svg)

#note: because of how the human eye transforms physical light into perceptual color. humans only have three cone classes, called short, medium, and long based on which wavelengths they're most sensitive to.

That means you only need those three color channels to match human color perception -- and for colorblind people who have only two cone classes, you'd need only two color channels.

---
## Metamers
Physically distinct stimuli that are perceptually identical

#note: so that's metamers -- physically different stimuli, but perceptually identical

---
## Metamers
Physically distinct stimuli that are perceptually identical (to a computational model) 

#note: for plenoptic, what we're focusing on is not an organism, but a computational model. so metamers have different pixel values but identical outputs

---

## Example metamers
<div data-animate data-load="assets/metamers.svg">
<!-- {"setup": [
{"element": "#g530", "modifier": "attr", "parameters": [ {"class": "fragment appear-disappear", "data-fragment-index": "0"} ]}
]} -->
</div>

#note: you are both familiar with some of this work from Eero, and plenoptic can be used to synthesize the classic Portilla-Simoncelli texture metamers (both the synthesis algorithm, now model-agnostic, and the model itself are included in the package),

but it's also what I used during my PhD to synthesize metamers for two foveated image statistic models, which, instead of matching image statistics across the entire visual field, like in the texture example, matched either luminance or spectral energy in receptive field-like pooling windows which grew with eccentricity. which we then used in a psychophysics experiment to see at which scale humans are insensitive to changes in these stats

---
## Why do this?

- Improve understanding of computational models <!-- .element: data-fragment-index="1" -->
- Image space is vast! <!-- .element: class="fragment" data-fragment-index="2" -->
- Better understand single model or compare between competing models <!-- .element: class="fragment" data-fragment-index="3" -->
- Take models seriously as objects of scientific inquiry <!-- .element: class="fragment" data-fragment-index="4" -->

#note: For those of you who haven't heard of this approach, you might wonder, why do
this?

the goal is to improve our understanding of how our computational models make sense of their input. as adversarial examples and other similar techniques have shown, that's not trivial! just because a model does well on image net doesn't mean it won't behave unexpectedly on new / out-of-distribution data

image space is vast, so any possible dataset is a tiny sample of it, and the methods in plenoptic provide a different and targeted way of exploring this space.

they can be used for:
- improving understanding of a given model -- for example, fit a model to prediction BOLD responses in V1, then generate some stimuli with plenoptic and use it in a new experiment
- another way of comparing models: many models can do equivalently (or near equivalently) well on a given dataset, and plenoptic's methods provide a complementary approach for comparing them.

and the real point here is that we should take our models seriously as objects of scientific inquiry. if we think that we have a good model for V1 responses, we should seriously test that model, to get a better sense for when its assumptions break down, the contexts in which it makes sense and the phenomena it can't explain.

---

## Metamer code example

<div class='margin-top column' style="float:left; width: 65%;">
<pre><code data-trim>
import plenoptic as po
basket = po.tools.load_images('data/basket.png')
model = po.simulate.PortillaSimoncelli((256, 256))
metamer = po.synthesize.Metamer(basket, model)
metamer.synthesize(max_iter=700, coarse_to_fine='together')
po.synthesize.metamer.animate(metamer, included_plots=['display_metamer', 'plot_loss'])
</code></pre>
</div>

<div class='margin-top column fragment appear-disappear' data-fragment-index="0" style="float:right; width:35%">
<video data-fragment-index="1" data-autoplay src="assets/texture-model-synth.mp4"></video>
</div>

---
## Contents
![image](assets/plen-contents-2.svg)

#note: plenoptic contains four synthesis methods, which have all been developed in Eero's lab over the years. I won't go though the rest of them in detail, but I'm happy to provide more detail or discuss them later if you're interested

each of these methods and models was developed by members of the lab over the years, but generally for a specific research question and with an implementation that others could not use, at least not easily. the goal of plenoptic was to implement these methods in a general, model-agnostic way, taking advantage of pytorch's automatic differentiation, so that we and other members of the scientific community could use them for novel models and questions

the package also contains several models and model components that we find useful and think others might. these are all implemented in pytorch, can be used easily with our synthesis methods, and are tested and maintained

---
## Developers
![people](assets/plen-people-details.svg)
