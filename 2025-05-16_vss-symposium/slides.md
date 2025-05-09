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
- Compare models. <!-- .element: class="fragment margin-top" data-fragment-index="2" -->
- Improve models models. <!-- .element: class="fragment margin-top" data-fragment-index="3" -->

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

## How to pick scientifically useful images?

<div data-animate data-load="assets/image_space-2.svg">
<!-- {"setup": [
{"element": "#g2", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]},
{"element": "#g1", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]}
]} -->
</div>

#note: now this isn't a new point to those of you in this room: the question of how to pick informative, how to pick scientifically useful, stimuli is one with a long history in psychophysics

---

## One possible answer: model metamers

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
{"element": "#g15", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "8"} ]}
]} -->
</div>

#note: one possible answer, which plenoptic provides, is model metamers.
- computational models map
- images from image space into their model response space. because many computational models discard some information, they have a null space
- that is, there are many images that give rise to the same model output
- these images are model metamers, a set of images that are physically distinct, but perceptually identical to the model in question. these images can be used to better understand your computational model by investigating what information it considers unimportant: any difference between images on this line are invisible to the model. but how to find these images?
- if you know the derivative of the model with respect to your image, then you know how to update an image to get the model output you want
- that is, you know how to start from some other image
- which gets mapped to some other location in model response space
- and update it so that we push it onto this manifold, so that its model output is the same as our original image
- that is, we've found a model metamer

---

#note: now that was very abstract, let's talk about a specific example using a retina-inspired model: has a center-surround filter (difference of Gaussians, bandpass, unoriented), with local divisive normalization and rectification. 
- if you apply this model to an image like Einstein
- you end up with an output that looks like this: the model is sensitive to contrast, highlighting the edges (which have a middling frequency, in that bandpass range) and ignoring local luminance, both because of that normalization and because it's low frequency
- we can start with some other image, like this patch of white noise, and similarly run it through the model, to get a very different output
- the goal of metamer synthesis is to update the pixels in this input so that these outputs match

---

#note:
- watch video doing just that
- now we end up with matched output, and we can see that the input has those features that the model is sensitive to, those edges, but it's *lacking* the ones it's insensitive to. and in fact, in the high frequencies and (less noticeably) the low ones, this metamer has just inherited content from the initial image.
- this emphasizes what the model cares about and what it discards.
- now this was a relatively simple model, those of you who are used to thinking about models like this didn't need metamers to understand everything I just walked you through

---

#note: but the general principles apply to any model. let's talk through a texture model. Ruth mentioned this in her talk, but it's a model built on top of Gabor-like filters / a V1-like representation, taking auto and cross correlations, trying to capture visual texture
- so if we give it a texturey image it transforms it into a big vector of numbers. there's not a great way to visualize this representation, unlike the last one, so I'm just going to show it as this big lollipop plot
- we can play the same game, taking another image, here a patch of white noise (checkerboard?). again, we have a very different output, but we know how to update the pixels of one to get the other

---

#note: 
- watch the video
- to emphasize what Ruth talked about in her talk, the process of modifying the model and synthesizing model metamers to see the effect adding or removing or changing different computations had, this was how this model was developed.
- now you may have noticed the big asterisk on this work: you need to know the gradient of the model with respect to the input in order to do this.
- originally, this was very labor-intensive, requiring a lot of calculus by hand.

---

<div data-animate data-load="assets/pytorch.svg">
<!-- {"setup": [
{"element": "#g4", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]},
{"element": "#g19", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]},
{"element": "#g2", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "2"} ]}
]} -->
</div>

#note:
- however in the past several decades, something called automatic differentiation, or autodiff, has really come into its own. with autodiff, we no longer have to compute these gradients manually, and can instead rely on software to do it for us.
- for plenoptic, we make use of pytorch, an open-source python package that came out of the deep learning community, originally developed at Meta and now part of the Linux Foundation.
- with pytorch, if we have a model that accepts and returns a torch tensor, and does the transofmration between the two in a torch-differentiable way (i.e., using functions from the pytorch library), pytorch can automatically compute the gradients we need.
- the upshot is: 

---

#note:
- I'm going to show you one simple example, so you know what this looks like. this is real code, if you install plenoptic you can run it now. I'm going to step through it bit by bit, so you see what's happening
- first, as should be familiar to all of you familiar with python, you import your library
- you then need to get your image into a torch tensor. there are many ways to do that: plenoptic has some built-in images we use for tests and examples, we have a helper function from loading images from disk, or if you're familiar with pytorch, you can get it in the normal way
- then we need to initialize your model. here, we're using the retina-like model I showed earlier, called luminance gain control. we have some built-in models you can use, or you can grab a model from any of the many pytorch model zoos that exist, or you can write your own. as long as it's in pytorch, it will work
- now, we need to detach the model parameter gradients -- most people are fitting pytorch models and so they want to update model parameters. for plenoptic, models are *fixed*, and so we remove those gradients, which saves computation
- now we initialize the metamer object. this only requires the target image and the model, though there are additional arguments you can specify here, for example, changing the loss function
- and finally, we call synthesize. the only option required here is the number of iterations to run the synthesis for, though again there are more options you could choose if you don't like our defaults.
- if you wanted to change the initial image, the optimization parameters, or the optimization algorithm, you can do that as well
- but this is all you *need*, five lines of code.

---

#note:
- and that will get you something like this
- as we saw before, you have your target image here, and the metamer-to-be down here. both of which we are sending through the model to get the model response
- our goal is to change these pixels until these outputs match
- I'm showing you one additional plot here: the optimization loss. this is what's going on under the hood: pytorch is minimizing the mean-squared error between these two outputs, which gives us this single number, which will decrease over time and eventually stabilize
- if you've ever done research like this, or any other high-dimensional non-convex optimization problem, you know that you spend a lot of time looking at curves like this -- you need to make sure that the solution you found is actually a good one

---

#note:
- now, we run the optimization and see these pixels change, as the outputs get more similar, and our loss goes down.
- just as we saw in the earlier example, we end up with a model metamer.
- if you go to my slides on the web, you can press the down arrow from this slide to see how you would make some of those simple changes, for those who are interested

---

## Another synthesis method: eigendistortions

<div data-animate data-load="assets/image_space-eigendistortion.svg">
<!-- {"setup": [
{"element": "#path2-3", "modifier": "attr", "parameters": [ {"class": "fragment disappear", "data-fragment-index": "0"} ]},
{"element": "#path13-3", "modifier": "attr", "parameters": [ {"class": "fragment disappear", "data-fragment-index": "0"} ]},
{"element": "#g4", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]},
{"element": "#g9", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]},
{"element": "#g7", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "2"} ]},
{"element": "#g8", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "3"} ]}
]} -->
</div>

#note:
- plenoptic contains more than just metamers.
- I'm going to talk briefly through one more synthesis method that we include, eigendistortions.  metamers are about investigating what information the model considers unimportant in a global manner, so that you can end up with a very different image
- eigendistortions ask the question: what small changes can I make to this image that my model thinks are really noticeable or really *un*-noticeable. in this sense, it's "local" -- we're not changing many pixels
- 

---

#note:
- so what does this look like for our retina-like model?
- to remind you, that model is a center-surround filter with divisive normalization and rectification
- we know that this cares about contrast, not luminance, and it cares only about mid-range frequencies
- so if we start again from our Einstein image, what can we do to make more and less noticeable changes?
- the least noticeable change, like we saw with metamers, is going to involve adding a bunch of high frequencies across the image. for this model, we're learning something very similar with the minimum distortion and metamers
- the most noticeable is more interesting: we're going to take a high contrast mid-frequency grating, *and* we're going to locate it in the darkest part of the image
- in so doing, we're maximizing its contrast
- so again, this emphasizes that the model cares about contrast and mid-frequencies: it does not care about high frequencies

---

## Contents
<img data-src="assets/contents.svg"></img>

#note:
- in addition to metamer and eigendistortion, plenoptic currently includes another synthesis method, known as MAD competition. I'm not going to describe that one in detail, but its goal is to efficiently compare models by generating stimuli that result in very different outputs
- we also provide a variety of stuff we find useful for vision science: some models, image quality metrics, and canonical computations, components for building visual models, as well as a handful of tools. I'm not going to explain all of these in detail, but if you already recognize them, hopefully this encourages you to check them out, and you can find more detail on our documentation or by asking me.
- all of these are written in pytorch, and so are differentiable and GPU-compatible

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

#note: to conclude, I'd like to step back a bit
- as I talked about today, plenoptic aims to help researchers better understand their models by facilitating synthesis of model-optimized stimuli
- we are compatible with any pytorch model. in this talk, I only showed you examples using built-in models, but you can swap in any pytorch model, including those from existing model zoos, or of course, your own
- we also provide a selection fo useful additional tools for vision science
- and all of this GPU-accelerated and differentiable. if you have a GPU, things will be faster, but you don't need to -- they all work as well on CPUs, just slower
- finally, I want to make some points that I think are generally under-valued in scientific software: we aim to provide thorough documentation and detailed examples, so that you can understand how to use the software and see some practical examples. we're always looking to improve the documentation, and I'm going to do a big push this summer
- we're also well-tested, with about 90% coverage, easy-to-install on any OS using either pip or conda, modular (so you can use any of these components separately), and of course open source (under MIT).

---

<div data-animate data-load="assets/advertisement_slide.svg">
<!-- {"setup": [
{"element": "#g18", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]}
]} -->
</div>

#note:
- thank you everyone for your time
- like I said, we're on pip and conda, you can find our documentation here, as well as our github
- if you have any questions about the package, you can find me here to ask (also on the discord). after the conference, you can post on the github -- I will respond
- this package has been the work of many people over many years, so I'd like to thank all of my contributors.
- and finally, if this intrigued you, I will be running a satellite event on Monday afternoon, a three hour chunk where we'll install plenoptic on your laptop and do some hands-on examples. registration is required for that event and we have limited spots, so if you're interested, follow that link/QR code, which will take you to a page that has the link for the registration, as well as my slides for this talk
- thank you all
