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

![](assets/plenoptic_logo_wide.svg) <!-- .element: style="height:50%" -->

## A python library for synthesizing model-optimized visual stimuli
## Billy Broderick <!-- .element: style="height:50%" -->

#note: today I'm going to talk about plenoptic, a python library for synthesizing the model-optimized visual stimuli we're talking about it in this session. but first, I'm going to step back a bit

---

<div data-animate data-load="assets/metamer-intro.svg">
<!-- {"setup": [
{"element": "#g104", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]},
{"element": "#g103", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]},
{"element": "#g101", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "2"} ]},
{"element": "#g100", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "3"} ]},
{"element": "#g81", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "4"} ]},
{"element": "#g105", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "5"} ]},
{"element": "#g98", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "6"} ]},
{"element": "#g7", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "7"} ]},
{"element": "#text65-8-8", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "8"} ]}
]} -->
</div>


#note:
- when you look at a picture of this room and compare it to looking around at the actual room
- you generally judge the colors in those two as identical
- this is not because the actual physical light, the energy at each wavelength, which our brains interpret as color, are identical
- because they're very much not
- instead, it's because to get to our brains, the light has to first go through our eyes and, in particular, our cones. most humans are trichromatic, which means they only have three cone classes, each differentially sensitive to visible light. in order to get identical color perception, you don't need the input to the system, the light, to be identical, you need
- the output, the cone responses to be identical. 
- if the responses of the three cone classes are identical to two given stimuli, you'll perceive their colors as identical, because you've thrown away all information that could be used to distinguish them
- they are what we call *percpetual metamers*, a set of images that are physically different but perceptually identical.

---
## Color matching experiments

<!-- to generate (movie, plus initial and final frames as pngs+svgs) color_matching.match_some_colors(n_steps=10, save_path="color-match.mp4")
-->
<img data-src="assets/color-match-init.png"></img>

#note: Understanding of this property of human vision dates to the 19th century, with Thomas Young and Hermann von Helmholtz's analysis of color matching experiments. In these experiments, participants were presented with a single color, here on the left, whose appearance they needed to match by playing around with the intensity of three different primaries.

---
## Color matching experiments

<!-- to generate (movie, plus initial and final frames as pngs+svgs) color_matching.match_some_colors(n_steps=10, save_path="color-match.mp4")
-->
<video data-src="assets/color-match.mp4"></video>

#note: participants increased or decreased the relative intensity as needed to end up with two identical colors

---
## Color matching experiments

<div data-animate data-load="assets/metamer-model.svg">
<!-- {"setup": [
{"element": "#g275", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]},
{"element": "#g11", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]},
{"element": "#g1", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "2"} ]},
{"element": "#g8", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "3"} ]},
{"element": "#g274", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "4"} ]}
]} -->
</div>

#note: 
- after running these color matching experiments many times 
- Helmholtz was able to derive these curves, giving the response of putative "photoreceptors" found in the human eye which responded to light of different colors, from red to violet.
- these curves give you a linear model of human trichromacy, which
- allows you to predict the responses of these photoreceptors to any stimulus.

your model is also making another really strong prediction -- all other information *not* captured by the model is discarded. thus, if the outputs of this model match, then they should be identical.

testing that prediction is a really good way of validating our understanding of trichromacy, as embodied in this model.

- because this model is linear, we know how to solve for a new stimulus that gives the same output pretty easily
- that is, we now know how to generate model metamers: images that are physically distinct but identical *to a model*.

in this case, such images allow us to validate and refine the model in question -- by comparing these images against the target of the model (in this case, human color matching), we can see where the predictions don't match reality and update the model as needed

as I said, we knew how to find these images in this case because the model's linear and thus, straightforward. but if we'd like to use this procedure with more complex, non-linear models, we need another way to find these images

---

<!-- to generate (movie, plus relevant svgs):
met = textures.synth_texture(max_iter=200, store_progress=5)
textures.animate(met, 5, save_path="textures.mp4")
-->
<div data-animate data-load="assets/metamer-portilla.svg">
<!-- {"setup": [
{"element": "#image1-35", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]},
{"element": "#g15", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]},
{"element": "#g2", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "2"} ]},
{"element": "#image1-05", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "3"} ]},
{"element": "#image1-39", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "4"} ]},
{"element": "#image1-82", "modifier": "attr", "parameters": [ {"display": "none"} ]},
{"element": "#g16", "modifier": "attr", "parameters": [ {"display": "none"} ]},
{"element": "#g17", "modifier": "attr", "parameters": [ {"display": "none"} ]},
{"element": "#g18", "modifier": "attr", "parameters": [ {"display": "none"} ]},
{"element": "#g19", "modifier": "attr", "parameters": [ {"display": "none"} ]},
{"element": "#g21", "modifier": "attr", "parameters": [ {"display": "none"} ]},
{"element": "#g20", "modifier": "attr", "parameters": [ {"display": "none"} ]}
]} -->
</div>

#note: 
- plenoptic comes out of work in Eero Simoncelli's lab, and in Eero's lab, this goes back to work he did in the late 90s with Javier Portilla on a texture model.
- in order to validate their computational model of visual texture, they were inspired by work from Bela Julesz in the 1960s. 
- as Javier and Eero put it: if they had a good model of visual texture, then any two texture images whose model outputs matched should be perceptually equivalent.

now, stumbling across two natural images with the same model output would be fairly difficult -- especially in the 90s, before the advent of large image databases

- so instead, they realized that, if they computed the gradient of the model with respect to the input image, they would know how to change the pixels of an image in order to get the model output to look like what they wanted
- that is, they could start with a natural texture image, send it through their model to get some output
- then take another image, say some white noise, ...

---

<div class="overlap-parent">
  <div data-animate data-load="assets/metamer-portilla.svg">
    <!-- {"setup": [
    {"element": "#g16", "modifier": "attr", "parameters": [ {"display": "none"} ]},
    {"element": "#g17", "modifier": "attr", "parameters": [ {"display": "none"} ]},
    {"element": "#g18", "modifier": "attr", "parameters": [ {"display": "none"} ]},
    {"element": "#g19", "modifier": "attr", "parameters": [ {"display": "none"} ]},
    {"element": "#g21", "modifier": "attr", "parameters": [ {"display": "none"} ]},
    {"element": "#g20", "modifier": "attr", "parameters": [ {"display": "none"} ]}
    ]} -->
    </div>
  <video style="width:71%" class="overlap-center" data-src="assets/textures.mp4"></video>
</div>

#note: and update its pixel values until the model outputs matched

doing this a bunch of times on different textures would allow them to then validate and refine their model, understanding what statistics captured what texture properties in their images

---

<div data-animate data-load="assets/metamer-portilla.svg">
<!-- {"setup": [
{"element": "#image1-39", "modifier": "attr", "parameters": [ {"display": "none"} ]},
{"element": "#g16", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]},
{"element": "#g17", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "2"} ]},
{"element": "#g18", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "3"} ]},
{"element": "#g19", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "4"} ]},
{"element": "#g21", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "5"} ]},
{"element": "#g20", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "6"} ]}
]} -->
</div>

#note:
- however, in order to do this, they needed to calculate this derivative, and, despite their claim that "this is usually straightforward", it involved doing a lot of calculus by hand
- even worse, every time they changed the model they would need to recompute the gradients, which is fairly tedious

---

<div data-animate data-load="assets/pytorch.svg">
<!-- {"setup": [
{"element": "#g4", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]},
{"element": "#g19", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]}
]} -->
</div>

#note:
- fortunately, in the 25ish years since that paper, science has advanced. in particular, something called automatic differentiation, or autodiff, has really come into its own. with autodiff, we no longer have to compute these gradients manually, and can instead rely on software to do it for us.
- for plenoptic, we make use of pytorch, an open-source python package that came out of the deep learning community, originally developed at Meta and now part of the Linux Foundation.
- with pytorch, if we have a model that accepts and returns a torch tensor, and does the transofmration between the two in a torch-differentiable way (i.e., using functions from the pytorch library), pytorch can automatically compute the gradients we need.

---

<div style="display:flex;flex-direction:column">
<div class="logo-title" data-load="assets/plenoptic_logo_wide.svg"></div>

Goals: <!-- .element: style="margin-top:1%" --> 
- Facilitate synthesis of model-optimized stimuli.
</div>

---

<h2 class="fragment disappear" data-fragment-index=0>Unpacking plenoptic logo</h2>
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

<div style="display:flex;flex-direction:column">
<div class="logo-title" data-load="assets/plenoptic_logo_wide.svg"></div>

Goals: <!-- .element: style="margin-top:1%" --> 
- Facilitate synthesis of model-optimized stimuli.
- <!-- .element: class="fragment appear"  -->
Be compatible with any PyTorch model: e.g., [torchvision](https://docs.pytorch.org/vision/stable/models.html),[timm](https://huggingface.co/docs/timm/index), [brainscore](https://www.brain-score.org/vision/), custom models. 
- Provide selection of useful vision science metrics, models, canonical computations, tools. <!-- .element: class="fragment appear"  --> 
- Do all of the above in (optional) GPU-accelerated manner. <!-- .element: class="fragment appear"  --> 
- Provide thorough documentation and detailed examples. <!-- .element: class="fragment appear"  --> 
- Well-tested, easy-to-install, modular, and open source. <!-- .element: class="fragment appear"  --> 
</div>

---

<div style="display:flex;flex-direction:column">
<div class="logo-title" data-load="assets/plenoptic_logo_wide.svg"></div>


Contents: <!-- .element: style="margin-top:1%" --> 

- Synthesis methods:
  - Metamers: investigate information discarded by model (e.g., Portilla and Simoncelli, 2000), with coarse-to-fine support.
  - Eigendistortions: generate image perturbations considered most and least noticeable by the model (e.g., Berardino et al., 2017).
  - Maximal Differentiation (MAD) Competition: efficiently compare two models, highlighting differences in sensitivity (e.g., Wang and Simoncelli, 2008).
- Image quality metrics:
  - Normalized Laplacian Pyramid Distance (Laparra et al., 2017)
  - SSIM (Structural Similarity Index) and MS-SSIM (Multi-Scale SSIM) (Wang et al. 2004; Wang et al., 2003)
- Canonical computations:
  - Laplacian and Steerable pyramids (Burt and Adelson, 1983; Simoncelli and Freeman, 1995)
  - Local gain control (e.g., Heeger, 1991)
- Models:
  - Center-Surround, On-Off and other "front end" models (Berardino et al., 2017)
  - Portilla and Simoncelli texture model (Portilla and Simoncelli, 2000)
- Image processing tools:
  - Alias-resistant up- and down-sampling
  - Efficient computation of autocorrelation
  - Complex signal phase modulation
  - Conversion of complex signal from polar to rectangular coordinates and vice versa
  - Computation of kurtosis, skew, and variance on n-dimensional tensors.

<!-- .element: class="two-columns-text"--> 

</div>

---

<div class="code-vis-grid">
```python doctest:scripts/example_code.py:base data-line-numbers data-id="one"
```
<p><img style="width:100%" data-src="assets/example_code-base-init.svg" ></img></p>
<div class='fragment appear-disappear overlap-code-grid' data-fragment-index="0">
<video style="width:100%" data-src="assets/example_code-base.mp4" ></video></div>
</div>

---

<div class="code-vis-grid">
```python doctest:scripts/example_code.py:gpu_one data-line-numbers="3,8,9" data-id="one"
```
<p><img style="width:100%" data-src="assets/example_code-base-final.svg" ></img></p>
</div>

---

<div class="code-vis-grid">
```python doctest:scripts/example_code.py:gpu_two data-line-numbers="12,13" data-id="one"
```
<p><img style="width:100%" data-src="assets/example_code-base-final.svg" ></img></p>
</div>

---

<div class="code-vis-grid">
```python doctest:scripts/example_code.py:base data-line-numbers data-id="one"
```
<p><img style="width:100%" data-src="assets/example_code-base-final.svg" ></img></p>
</div>

---

<div class="code-vis-grid">
```python doctest:scripts/example_code.py:custom_image data-line-numbers="3" data-id="one"
```
<p><img style="width:100%" data-src="assets/example_code-custom_image-init.svg" ></img></p>
<div class='fragment appear-disappear overlap-code-grid' data-fragment-index="0">
<video style="width:100%" data-src="assets/example_code-custom_image.mp4" ></video></div>
</div>

---

<div class="code-vis-grid">
```python doctest:scripts/example_code.py:init_image data-line-numbers="3,11" data-id="one"
```
<p><img style="width:100%" data-src="assets/example_code-init_image-init.svg" ></img></p>
<div class='fragment appear-disappear overlap-code-grid' data-fragment-index="0">
<video style="width:100%" data-src="assets/example_code-init_image.mp4" ></video></div>
</div>

---

<div class="code-vis-grid">
```python doctest:scripts/example_code.py:optimizer_kwargs data-line-numbers="12,13" data-id="one"
```
<p><img style="width:100%" data-src="assets/example_code-optimizer_kwargs-init.svg" ></img></p>
</div>

---

<div class="code-vis-grid">
```python doctest:scripts/example_code.py:optimizer data-line-numbers="2,13,14" data-id="one"
```
<p><img style="width:100%" data-src="assets/example_code-optimizer-init.svg" ></img></p>
</div>

---

<div class="code-vis-grid">
```python doctest:scripts/example_code.py:base data-line-numbers data-id="one"
```
<p><img style="width:100%" data-src="assets/example_code-base-final.svg" ></img></p>
</div>

---

<div class="code-vis-grid">
```python doctest:scripts/example_code.py:eigendistortion data-line-numbers="11" data-id="one"
```
<p><img style="width:100%" data-src="assets/example_code-eigendistortion-final.svg" ></img></p>
</div>

---

<div class="code-vis-grid" style="top:15%;">
```python doctest:scripts/example_code.py:custom_model data-line-numbers="8-21,24" data-id="one"
```
<p><img style="width:100%" data-src="assets/example_code-custom_model-init.svg" ></img></p>
<div class='fragment appear-disappear overlap-code-grid' data-fragment-index="0">
<video style="width:100%" data-src="assets/example_code-custom_model.mp4" ></video></div>
</div>

---

<div class="code-vis-grid" style="grid-template-columns: 53% 50%;top:15%;">
```python doctest:scripts/example_code.py:torchvision data-line-numbers="8-22" data-id="one"
```
<p><img style="width:100%" data-src="assets/example_code-torchvision-init.svg" ></img></p>
<div class='fragment appear-disappear overlap-code-grid' data-fragment-index="0" style="left:53%;width:50%;">
<video style="width:100%" data-src="assets/example_code-torchvision.mp4" ></video></div>
</div>

---

<div class="code-vis-grid">
```python doctest:scripts/example_code.py:texture data-line-numbers data-id="one"
```
<p><img style="width:100%" data-src="assets/example_code-texture-init.svg" ></img></p>
<div class='fragment appear-disappear overlap-code-grid' data-fragment-index="0">
<video style="width:100%" data-src="assets/example_code-texture.mp4" ></video></div>
</div>

---

<div data-load="assets/advertisement_slide.svg"></div>
