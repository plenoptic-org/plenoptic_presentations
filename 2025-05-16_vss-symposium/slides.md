![](assets/plenoptic_logo_wide.svg) <!-- .element: style="width:75%" -->

## A python library for synthesizing model-optimized visual stimuli
## Billy Broderick 
### <!-- .element: style="margin-bottom:5%" --> slides: https://vss.plenoptic.org 

#note: today I'm going to talk about plenoptic, a python library for synthesizing the model-optimized visual stimuli we're talking about it in this session. but first, I'm going to step back a bit

---

## Big picture goal

- Better understand computational visual models. <!-- .element: class="fragment" data-fragment-index="1" -->
- Compare models. <!-- .element: class="fragment" data-fragment-index="2" -->
- Improve models. <!-- .element: class="fragment" data-fragment-index="3" -->

<!-- .element: style="font-size:1.5em" -->

#note: big picture goal of plenotpic, of using model-optimized stimulus is to better understand computational visual models, the information they consider important and unimportant. these methods can also help you compare among competing models and improve your existing models.

with plenoptic, we seek to do all this with model-optimized stimuli

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

## How to pick scientifically useful images?

<div data-animate data-load="assets/image_space-2.svg">
<!-- {"setup": [
{"element": "#path2-3", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]},
{"element": "#text13-5", "modifier": "attr", "parameters": [ {"class": "fragment appear-disappear", "data-fragment-index": "0"} ]},
{"element": "#g13", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]},
{"element": "#g1", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "2"} ]},
{"element": "#g2", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "3"} ]}
]} -->
</div>

#note: the reason this is useful is to address the general difficult question of how to pick scientifically useful images.
- if this is image space, the space of all possible images, every point here is an image, and every image you can show is a point here.
- when you design an experiment, you have limited time and need to decide what stimuli to use -- this is not a new idea in psychophysics, but you can only do so much
- and many of the stimuli you could pick are not useful -- they're redundant with each other, not telling you anything new
- we want to find the ones that are helpful, that will tell you something about your model

---

## Image space is big!

<div data-animate data-load="assets/image_space.svg">
<!-- {"setup": [
{"element": "#text11", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]},
{"element": "#text3", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]},
{"element": "#rect13", "modifier": "attr", "parameters": [ {"class": "fragment disappear", "data-fragment-index": "2"} ]},
{"element": "#rect13-6", "modifier": "attr", "parameters": [ {"class": "fragment disappear", "data-fragment-index": "3"} ]},
{"element": "#rect13-6-7", "modifier": "attr", "parameters": [ {"class": "fragment disappear", "data-fragment-index": "4"} ]},
{"element": "#image15239", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "6"} ]},
{"element": "#text14", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "7"} ]}
]} -->
</div>

#note: and this is difficult because image space is big
- as the Hitchhiker's Guide to the Galaxy put it: **read quote**
- to be more concrete and a little heavy-handed, if you're looking at 8 bit images, you have 256 values per pixel
- and that means you already hav 10 to the 40 4x4 images
- 10 to 240 10 by 10
- and by 256 by 256, you have a truly absurd number
- for comparison, in the entirety of the observable universe
- there are "only" 10^80 protons, so this space really is vast

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
{"element": "#g15", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "8"} ]}
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

---

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

---

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

---
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

## Texture model metamer

<div class="overlap-parent">
<div data-animate data-load="assets/texture-metamers.svg">
<!-- {"setup": [
{"element": "#image1", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]},
{"element": "#g6", "modifier": "attr", "parameters": [ {"class": "fragment appear-disappear", "data-fragment-index": "1"} ]},
{"element": "#image1-6", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "2"} ]},
{"element": "#g8", "modifier": "attr", "parameters": [ {"class": "fragment disappear", "data-fragment-index": "2"} ]},
{"element": "#text39936", "modifier": "attr", "parameters": [ {"class": "fragment disappear", "data-fragment-index": "2"} ]},
{"element": "#image1-8", "modifier": "attr", "parameters": [ {"display": "none"} ]},
{"element": "#g4", "modifier": "attr", "parameters": [ {"display": "none"} ]},
{"element": "#g5", "modifier": "attr", "parameters": [ {"display": "none"} ]}
]} -->
</div>
</div>

#note: but the general principles apply to any model. let's talk through a texture model. Ruth mentioned this in her talk, but it's a model built on top of Gabor-like filters / a V1-like representation, taking auto and cross correlations, trying to capture visual texture
- so if we give it a texturey image it transforms it into this big vector statistics.
- there's not a great way to visualize this representation, unlike the last one, so I'm just going to show it as this big lollipop plot
- we can play the same game, taking another image, here a patch of white noise. again, we have a very different output, but we know how to update the pixels of one to get the other

---

## Texture model metamer

<div class="overlap-parent">
  <div data-animate data-load="assets/texture-metamers.svg">
<!-- {"setup": [
{"element": "#g8", "modifier": "attr", "parameters": [ {"display": "none"} ]},
{"element": "#image1-8", "modifier": "attr", "parameters": [ {"display": "none"} ]},
{"element": "#text39936", "modifier": "attr", "parameters": [ {"display": "none"} ]},
{"element": "#g6", "modifier": "attr", "parameters": [ {"display": "none"} ]},
{"element": "#g4", "modifier": "attr", "parameters": [ {"display": "none"} ]},
{"element": "#g5", "modifier": "attr", "parameters": [ {"display": "none"} ]}
]} -->
  </div>
  <video style="width:84%;top:58%;left:56%" class="overlap-item" data-src="assets/textures_workstation_gpu.mp4"></video>
</div>

#note: 
- watch the video

---
## Texture model metamer

<div class="overlap-parent">
  <div data-animate data-load="assets/texture-metamers.svg">
<!-- {"setup": [
{"element": "#g8", "modifier": "attr", "parameters": [ {"display": "none"} ]},
{"element": "#g6", "modifier": "attr", "parameters": [ {"display": "none"} ]},
{"element": "#text39936", "modifier": "attr", "parameters": [ {"display": "none"} ]},
{"element": "#g5", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]}
]} -->
  </div>
</div>

#note: 
- and again, we've ended up in a situation where these plots on the right match
- and so these images on the left are model metamers
- to emphasize what Ruth talked about in her talk, the process of modifying the model and synthesizing model metamers to see the effect adding or removing or changing different computations had, this was how this model was developed.
- now you may have noticed the big asterisk on this work: you need to know the gradient of the model with respect to the input in order to do this.

---
## Texture model metamer

<div class="overlap-parent">
  <div data-animate data-load="assets/texture-metamers-gd.svg">
<!-- {"setup": [
{"element": "#g4", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]},
{"element": "#g1", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]},
{"element": "#path2", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "2"} ]},
{"element": "#g3", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "3"} ]},
{"element": "#image1-67", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "4"} ]}
]} -->
  </div>
</div>

#note: 
- to visualize how we do that, let's go back to our initial starting point
- we ran both images through the model and got the model responses to each fo them
- if we take the mean squared error between these two, we end up with our loss. the goal of metamer synthesis is to minimize this loss, make it as small as possible
- to do that, we back propagate the loss through the model
- which tells us the derivative of the model with respect to the stimulus, the image pixels, as I mentioned earlier in this talk
- and now we know how to update the this bottom image so as to change its output and we run gradient descent to make the two reprsentations match
- now back in the day, this whole process had to be done by hand, which was tedious. and, even worse, you needed to redo it whenever you changed the model

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
- the upshot is: plenoptic can compute the necessary gradients for any model, as long as it's written in pytorch

---

## Example code: synthesize metamer

<div data-load="assets/lgn-metamers.svg"></div>

#note:
- to show you what that looks like, I'm going to show you one simple bit of code
- the code I'm going to show you was used to generate this example from earlier

---

## Example code: synthesize metamer

```python data-line-numbers="|1|2|3-6|7|8|9-10"
import plenoptic as po
img = po.data.einstein()
model = po.simul.LuminanceGainControl(
    kernel_size=(31, 31), pad_mode="circular",
    pretrained=True, cache_filt=True
)
po.tools.remove_grad(model)
met = po.synth.Metamer(img, model)
met.synthesize(max_iter=1300, 
               stop_criterion=1e-11)
```

<div class="overlap-item overlap-center" data-animate data-load="assets/code-overlay.svg">
<!-- {"setup": [
{"element": "#g6", "modifier": "attr", "parameters": [ {"class": "fragment appear-disappear", "data-fragment-index": "0"} ]},
{"element": "#g7", "modifier": "attr", "parameters": [ {"class": "fragment appear-disappear", "data-fragment-index": "1"} ]},
{"element": "#g9", "modifier": "attr", "parameters": [ {"class": "fragment appear-disappear", "data-fragment-index": "2"} ]},
{"element": "#g8", "modifier": "attr", "parameters": [ {"class": "fragment appear-disappear", "data-fragment-index": "3"} ]},
{"element": "#g10", "modifier": "attr", "parameters": [ {"class": "fragment appear-disappear", "data-fragment-index": "4"} ]},
{"element": "#g11", "modifier": "attr", "parameters": [ {"class": "fragment appear-disappear", "data-fragment-index": "5"} ]},
{"element": "#g19", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "6"} ]},
{"element": "#g20", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "7"} ]}
]} -->
</img>

#note:
- you don't need to understand this code in detail, for those of you who aren't python gurus, but I want you see that it's compact and that the way the process is broken up is reasonable.
- and again, this is the actual code I ran for this presentation -- if you install plenoptic and run this code, you'll get that metamer
- (I'm not showing you the code for creating the figures and animation -- as those of you who use matplotlib know, it can take some fiddling to make things look nice)
- first, as should be familiar to all of you familiar with python, you import your library
- you then need to load your image. there are many ways to do that: plenoptic has some built-in images we use for tests and examples, we have a helper function from loading images from disk.
- then we need to initialize your model. here, we're using the LGN-like model I showed earlier, called luminance gain control. we have some built-in models you can use, or you can grab a model from any of the many pytorch model zoos that exist, or you can write your own. as long as it's in pytorch, it will work
- now, we need to detach the gradients with respect to the model parameters -- most people are fitting pytorch models and so they want to update model parameters. for plenoptic, models are *fixed*, and so we remove those gradients, which saves computation. we only need to compute the gradients with respect to the image pixels
- now we initialize the metamer object. this only requires the target image and the model, though there are additional arguments you can specify here, for example, changing the loss function
- and finally, we call synthesize, which implements the gradient descent algorithm that I just talked you through. these arguments here specify how long to run the optimization for and the threshold we use for determining if it looks like the optimization has converged, i.e., the loss has stopped changing. neither of these arguments are necessary, we have defaults, but, depending on your model, you'll need to play around with them.
- if you wanted to change the initial image, the optimization parameters, or the optimization algorithm, you can do that as well
- but this is all you *need*, six lines of code.
- generally speaking, this last step, synthesize, is the most resource and time-intensive
- to give you a sense for how long this took, the synthesize step here took 7 seconds using the GPU on the workstation I have in my office, 3.5 minutes on that machine without using the GPU, and 7 min on this laptop
- the texture example I showed you earlier took 40sec using the GPU, about 1min without, or 3.5 min on this laptop

---

## Plenoptic also includes "eigendistortions"

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
- I'm going to talk briefly through one more synthesis method that we include, eigendistortions.  
- metamers are about investigating what information the model considers unimportant in a global manner, so that you can end up with a very different image
- eigendistortions ask the question: what small changes can I make to this image that my model thinks are really noticeable or really *un*-noticeable. in this sense, it's "local" -- we're not changing the pixels much

---

## LGN-inspired model eigendistortion

<div data-animate data-load="assets/lgn-eigen.svg">
<!-- {"setup": [
{"element": "#g34", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]},
{"element": "#g33", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]},
{"element": "#imagea1e65ec6fb", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "2"} ]},
{"element": "#image4fc786c3dc", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "2"} ]}
]} -->
</div>

#note:
- so what does this look like for our LGN-like model?
- to remind you, that model is a center-surround filter with divisive normalization and rectification
- we know that this cares about contrast, not luminance, and it cares only about mid-range frequencies
- so if we start again from our Einstein image, what can we do to make more and less noticeable changes?
- the least noticeable change, like we saw with metamers, is going to involve adding a bunch of high frequencies across the image. for this model, we're learning something very similar with the minimum distortion and metamers
- the most noticeable is more interesting: we're going to take a mid-frequency grating, *and* we're going to concentrate it in a particular part of the image.
- this model predicts that if you take these distortions and add them back to the Einstein image, with the same amplitude, this distortion will be much more perceptually noticeable than this one.
- and that's what we see: much more noticeable is to take your distortion and concentrate it in the part of the image where the structure is very different to it; less noticeable is to take your distortion and make it diffuse, hiding it elsewhere
- what i just talked you through is the kind of informal psychophysics that Ruth talked about in her talk, helping to give you an intuition to better understand what your model cares about, and shows that it's capturing something about human vision
- you could also, as was done in the paper where  eigendistortions were developed, generate many distortions of this type for multiple models, and run a formal psychophysics experiment, determining how much you need to scale up these distortions to reach psychophysical thresholds
- in that case, you are using eigendistortions for model comparison as well

---

<div style="display:flex;flex-direction:column">
<div class="logo-title" data-load="assets/plenoptic_logo_wide.svg"></div>
<div data-animate data-load="assets/contents.svg">
<!-- {"setup": [
{"element": "#g4", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]},
{"element": "#g5", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]},
{"element": "#text1-3-6", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "2"} ]},
{"element": "#g1", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "3"} ]},
{"element": "#g2", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "4"} ]},
{"element": "#g6", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "5"} ]}
]} -->
</div>
</div>

#note:
- so I talked you through briefly through metamer and eigendistortion, two of the synthesis methods included in plenoptic
- additionlly, plenoptic currently includes another synthesis method, known as MAD competition. I'm not going to describe that one in detail, but its goal is to efficiently compare pairs of models by generating stimuli that result in very different outputs
- we also provide a variety of stuff we find useful for vision science: some models, image quality metrics, and canonical computations, components for building visual models, as well as a handful of tools. I'm not going to explain all of these in detail, but if you already recognize them, hopefully this encourages you to check them out, and you can find more detail on our documentation or by asking me.
- all of these are written in pytorch, and so are differentiable and GPU-compatible

---

<div style="display:flex;flex-direction:column">
<div class="logo-title" data-load="assets/plenoptic_logo_wide.svg"></div>

Goal: understand, compare, and improve computational models <!-- .element: style="margin-top:1%;font-size:1.3em" --> 
- <!-- .element: class="fragment appear"  --> 
Facilitate synthesis of **model-optimized stimuli**.
- <!-- .element: class="fragment appear"  -->
Be compatible with **any PyTorch model**: e.g., [torchvision](https://docs.pytorch.org/vision/stable/models.html), [timm](https://huggingface.co/docs/timm/index), [brainscore](https://www.brain-score.org/vision/), custom models. 
- <!-- .element: class="fragment appear"  --> 
Provide selection of useful vision science **metrics, models, tools**. 
- <!-- .element: class="fragment appear"  --> 
Do all of the above in (optional) **GPU-accelerated manner**. 
- <!-- .element: class="fragment appear"  --> 
Provide thorough **documentation** and detailed **examples**.
- <!-- .element: class="fragment appear"  -->
Well-tested, easy-to-install, modular, and open source. 

<!-- .element: style="font-size:1.3em" -->
</div>

#note: 
- as I talked about today, plenoptic aims to help researchers better understand, compare, and improve their models
- and we do this by facilitating synthesis of model-optimized stimuli
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
