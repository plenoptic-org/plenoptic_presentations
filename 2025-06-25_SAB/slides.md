![](assets/plenoptic_logo_wide.svg) <!-- .element: style="width:75%" -->

## <!-- .element: style="margin-bottom:15%" --> Better understand computational visual models

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

#note: which we represent with our logo

when we think about models in visual neuroscience, they're often set up like this. it accepts some stimuli s, often for us images, as inputs, and based on some parameters theta, returns some responses r. these responses can be anything of interst to the experimenter, such as predicted spike rates, BOLD response, or image class

- now the way that models are most commonly used, is that we feed them an input and some parameter values and we simulate the responses.

- we often pretty regularly fix the responses for a set of stimuli and use backpropagation to fit the parameters

- but there's nothing special about the stimuli. we can similarly hold both the responses and parameters constant and use back propagation to generate novel stimuli. 

this is what we call synthesis -- updating the pixel values of an image based on a model with set parameter values and some intended output.

---

## One possible method: model metamers

<div data-animate data-load="assets/image_space-metamers.svg">
<!-- {"setup": [
{"element": "#g2", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]},
{"element": "#g16", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]},
{"element": "#g1", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "2"} ]},
{"element": "#g17", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "3"} ]},
{"element": "#g3", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "4"} ]},
{"element": "#path2-3", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "5"} ]},
{"element": "#g7", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "6"} ]},
{"element": "#path2-0", "modifier": "attr", "parameters": [ {"class": "fragment appear-disappear", "data-fragment-index": "6"} ]},
{"element": "#path2-0-2", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "7"} ]},
{"element": "#g6", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "7"} ]},
{"element": "#rect1-2-0", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "9"} ]},
{"element": "#g10", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "9"} ]}
]} -->
</div>

#note: one possible way to find useful images in that great vastness, which plenoptic provides, is model metamers. as before, this blob is image space, with every point here representing an image
- computational models, then, map
- images from image space into their model response space. because many computational models discard some information, they have a null space
- that is, there are many images that give rise to the same model output
- these images are model metamers, a set of images that are physically distinct, but perceptually identical to the model in question. these images can be used to better understand your computational model by investigating what information it considers unimportant: any difference between images on this line are invisible to the model. but how to find these images?
- if you know the derivative of the model with respect to your image, then you know how to update an image to get the model output you want
- that is, you know how to start from some other image
- which gets mapped to some other location in model response space
- and update it so that we push it onto this manifold, so that its model output is the same as our original image
- that is, we've found a model metamer

--

## LGN-inspired model metamer

<div class="overlap-parent">
<div data-animate data-load="assets/lgn-metamers.svg">
<!-- {"setup": [
{"element": "#g2", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]},
{"element": "#image1-5", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]},
{"element": "#image1", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "2"} ]},
{"element": "#image1-1", "modifier": "attr", "parameters": [ {"display": "none"} ]},
{"element": "#g4", "modifier": "attr", "parameters": [ {"display": "none"} ]},
{"element": "#g5", "modifier": "attr", "parameters": [ {"display": "none"} ]}
]} -->
</div>
</div>

#note: now that was very abstract, let's talk about a specific example using a LGN-inspired model: has a center-surround filter (difference of Gaussians, bandpass, unoriented), with local divisive normalization and rectification. 
- if you apply this model to an image like Einstein
- you end up with an output that looks like this: the model is sensitive to contrast, highlighting the edges (which have a middling frequency, in that bandpass range) and ignoring local luminance, both because of that normalization and because it's low frequency
- we can start with some other image, like this patch of white noise, and similarly run it through the model, to get a very different output
- the goal of metamer synthesis is to update the pixels in this input so that these outputs match

--

## LGN-inspired model metamer

<div class="overlap-parent">
  <div data-animate data-load="assets/lgn-metamers.svg">
<!-- {"setup": [
{"element": "#image1-1", "modifier": "attr", "parameters": [ {"display": "none"} ]},
{"element": "#g4", "modifier": "attr", "parameters": [ {"display": "none"} ]},
{"element": "#g5", "modifier": "attr", "parameters": [ {"display": "none"} ]}
]} -->
  </div>
  <video style="width:74.5%;top:76%;left:60%" class="overlap-item" data-src="assets/workstation_gpu_noise_lr.mp4"></video>
</div>

#note:
- watch video doing just that

--

## LGN-inspired model metamer

<div class="overlap-parent">
  <div data-animate data-load="assets/lgn-metamers.svg">
<!-- {"setup": [
{"element": "#g5", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]}
]} -->
  </div>
</div>

#note:
- watch video doing just that
- now we end up with matched output on the right
- and that means that these images on the left are model metamers

and we can see that the input has those features that the model is sensitive to, those edges, but it's *lacking* the ones it's insensitive to. and in fact, in the high frequencies and (less noticeably) the low ones, this metamer has just inherited content from the initial image.

this emphasizes what the model cares about and what it discards.

now this was a relatively simple model, those of you who are used to thinking about models like this didn't need metamers to understand everything I just walked you through

---

<div style="display:flex;flex-direction:column">
<div class="logo-title" data-load="assets/plenoptic_logo_wide.svg"></div>
<img data-src="assets/contents.svg">
</div>

#note:
- so I talked you through briefly through metamer and eigendistortion, two of the synthesis methods included in plenoptic
- additionlly, plenoptic currently includes another synthesis method, known as MAD competition. I'm not going to describe that one in detail, but its goal is to efficiently compare pairs of models by generating stimuli that result in very different outputs
- we also provide a variety of stuff we find useful for vision science: some models, image quality metrics, and canonical computations, components for building visual models, as well as a handful of tools. I'm not going to explain all of these in detail, but if you already recognize them, hopefully this encourages you to check them out, and you can find more detail on our documentation or by asking me.
- all of these are written in pytorch, and so are differentiable and GPU-compatible

---

## Next steps

- Currently: under review at pyOpenSci
    - Improve documentation
- Add further synthesis examples: adversarial examples, style transfer, video and audio model metamers, metamer with penalization
- Add examples showing how to use plenoptic with more pre-trained models: torchvision, timm (huggingface), brainscore
- Reproduce examples from the literature: Wang and Simoncelli, 2008 (original MAD paper); Feather et al., 2023 (audio and image deep net metamers)
- Double-check compatibility with new Mac GPUs
- Finalize pooled texture model (e.g., Freeman and Simoncelli, 2011)
