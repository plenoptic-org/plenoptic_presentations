<img style="height:50%" data-src="assets/plenoptic_logo.svg"></img> 

## CSHL Vision 2024
## Billy Broderick <!-- .element: style="height:50%" -->

---

## Who am I?

- PhD: NYU Center for Neural Science, May 2022 <!-- .element: class="fragment" data-fragment-index="0" -->
  - Advisors: Eero Simoncelli and Jonathan Winawer
- Research focus: how vision changes across the visual field, using fMRI, psychophysics, and computational models <!-- .element: class="fragment" data-fragment-index="1" -->
- Fell down the open source / open science rabbit hole <!-- .element: class="fragment" data-fragment-index="2" -->
- Currently: Associate Research Scientist &ndash; Software in the NeuroRSE group at the Flatiron Institute Center for Computational Neuroscience <!-- .element: class="fragment" data-fragment-index="3" -->

---

## What is Flatiron?

<div data-animate data-load="assets/flatiron.svg" crossorigin="anonymous">
<!-- {"setup": [
{"element": "#g715", "modifier": "attr", "parameters": [ {"class": "fragment appear-disappear", "data-fragment-index": "0"} ]}
]} -->
</div>

#note: so apologies to those who know already, but I thought I'd take a moment to explain who we are. We are employees of the Flatiron Institute. If you've heard "Flatiron" before, you're probably thinking of this iconic building in Manhattan, the Flatiron Building

**click**. unfortunately, we're not in that building. we're about 2 blocks from there -- the neighborhood around this building is known as the Flatiron district, hence the name. I think every employee goes through a moment of disappointment when they realize they won't be working here. we have interns every summer, and a fair number of the interns this summer showed up at the Flatiron building and were very confused. especially because the building is currently empty I think, due to some weirdness over the ownership

---

## The Real Flatiron Institute

<img data-src="assets/flatiron-institute.png"></img>

#note: we are part of this Flatiron institute, which is part of the Simons Foundation. the Simons Foundation is a private foundation whose money comes from Jim Simons, a mathematician and hedge fund billionaire who recnetly passed away. it funds a variety of projects in the maths and sciences, especially computational research, and the Flatiron institute is the in-house research center.

---
## The Real Flatiron Institute

<img data-src="assets/flatiron-centers.png"></img>

#note: Flatiron has five centers, one each for computational astrophysics, biology, mathematics, neuroscience, and quantum physics, plus the scientific computing core, who supports the cluster and other computational infrastructure that the other centers use.

---
## The Real Flatiron Institute

<img data-src="assets/flatiron-ccn.png"></img>

#note: Mots of the speakers and TAs here are part of the Center for Computational Neuroscience, the newest center at Flatiron, which has four research groups doing differnet types of computational neuroscience work, with grad students from NYU, postdocs and research scientists, along with summer interns.

---
## The Real Flatiron Institute

<img data-src="assets/neurorse.png"></img>

#note: And most of the speakers you're going to hear from over the next two days are from the neuroRSE, or research software engineering, group within CCN. We're a group of full time research scientists whose only job is to build and maintain open source python packages for neuroscience research, including pynapple and nemos.

---
## CCN Software packages

<div class='column' style="float:left;width:50%">
<img data-src="assets/pynapple.svg">
<ul>
<li><a href="https://github.com/pynapple-org/pynapple/</li>">https://github.com/pynapple-org/pynapple/</li></a>
<li>light-weight python library for neurophysiological data analysis</li>
</ul>
<img data-src="assets/nemos.svg">
<ul>
<li><a href="https://github.com/flatironinstitute/nemos</li>">https://github.com/flatironinstitute/nemos</li></a>
<li>statistical modeling framework for neuroscience</li>
</ul>
</div>
<div class='column' style="float:right;width:50%">
<img data-src="assets/plenoptic_logo.svg">
<ul>
<li><a href="https://github.com/plenoptic-org/plenoptic/</li>">https://github.com/plenoptic-org/plenoptic/</li></a>
<li>model-based synthesis of perceptual stimuli</li>
</ul>
<img data-src="assets/fastplotlib.svg">
<ul>
<li><a href="https://github.com/fastplotlib/fastplotlib</li>">https://github.com/fastplotlib/fastplotlib</li></a>
<li>expressive plotting library that enables rapid prototyping for large scale explorative scientific visualization</li>
</ul>
</div>

#note: 

---

# CITE YOUR SOFTWARE!

---

<img data-src="assets/defense-blackhole.svg"></img>

#note: To take one particularly illustrative example: I'm sure many of you recognize this picture. It's an image of supermassive black hole M87, captured by the Event Horizon Telescope Collaboration in April 2019

---
---

<img data-src="assets/defense-blackhole-headlines.svg"></img>

#note: this hit the headlines of every major news outlet, with the image eventually reaching more than 4.5 billion people around the world

the work that went into this was done with a variety of packages from the open-source python scientific ecosystem, such as numpy and matplotlib, which was credited by some of the scientists involved as making the work possible, preventing them from having to reinvent everything from scratch

---
---

<img data-src="assets/defense-blackhole-headlines-impact.svg"></img>

#note: yet five days after this announcement, the US National Science Foundation denied a grant to support that ecosystem, saying the software didn't have "sufficient impact"

---
---

# CITE YOUR SOFTWARE!

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
<img style="margin-top:5%;height:950px;width:auto" data-src="assets/plen-metamer-podium.svg"></img> 

#note: when you look at this picture of this room, compared to the room in real life, they look like they're the same color. however, the physical light that is entering your eye is *very* different, because this projector only has three color channels (RGB), and so it cannot hope to exactly match the energy at every wavelength in the visual light spectrum

however, it doesn't need to

---
## Metamers
<img data-src="assets/plen-metamer-cones.svg"></img>

#note: because of how the human eye transforms physical light into perceptual color. humans only have three cone classes, called short, medium, and long based on which wavelengths they're most sensitive to.

That means you only need those three color channels to match human color perception -- and for colorblind people who have only two cone classes, you'd need only two color channels.

---
## Metamers
Physically distinct stimuli that are perceptually identical <i class="fragment" data-fragment-index="1">(to a computational model)</i>

#note: so that's metamers -- physically different stimuli, but perceptually identical

for plenoptic, what we're focusing on is not an organism, but a computational model. so metamers have different pixel values but identical outputs

---

## Textures
<div data-animate data-load="assets/textures.svg">
<!-- {"setup": [
{"element": "#image765", "modifier": "attr", "parameters": [ {"display": "none"} ]}
]} -->
</div>

#note: in Eero's lab, this type of work goes back to a project he started in the late 90s with Javier Portilla seeking to understand visual textures, which I think he discussed a little with you already?

visual textures are homogeneous, with repeated features, and so folks in image processing had viewed them as potentially tractable for a while. Eero and Javier set out to build a statistical model that could capture the texturiness of these and similar images.

---

## Texture model
<div data-animate data-load="assets/texture-model.svg">
<!-- {"setup": [
{"element": "#g1865", "modifier": "attr", "parameters": [ {"display": "none"} ]},
{"element": "#text40092", "modifier": "attr", "parameters": [ {"display": "none"} ]}
]} -->
</div>

#note: they put together this model, which took the outputs of V1 like receptive fields, which decomposed the images into different orientation and spatial frequency bands, then took their auto-correlations and cross-correlations across spatial frequency and orientation, to end up with about 700 numbers quantifying this texturiness.

they then ran into the question: how do we validate our model? how do we make sure it's doing a good job?

---
## Texture model
<div data-animate data-load="assets/textures.svg">
<!-- {"setup": [
{"element": "#image765", "modifier": "attr", "parameters": [{"class": "fragment appear-disappear", "data-fragment-index": "0"} ]}
]} -->
</div>

#note: at first, they took a classic approach. they went back to these texture images and said, let's just try and do classification. let's take patches from each of these images and use our model to say "these patches are a brick wall,", "these are a basket", etc.

*click*. they had about 100 high quality images from this Brodatz book, and they used their model to classify them -- and it did phenomenally well, performing almost perfectly. they were very excited about how well it performed. but then they realized they needed to have some point of comparison, some baseline to show how much better their model was, how important all these new correlations, which others hadn't considered, really were.

this probably sounds familiar to those of you who know more about machine learning: here's a benchmark dataset, let's test our model's performance and compare it to others in order to show that we're state of the art.

---
## Texture model
<div data-animate data-load="assets/texture-model.svg">
<!-- {"setup": [
{"element": "#g1865", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]},
{"element": "#text40092", "modifier": "attr", "parameters": [ {"class": "fragment appear-disappear", "data-fragment-index": "1"} ]}
]} -->
</div>

#note: so they went back to their model, *click* and they chopped off the second half. they just took the "V1-like" model, which decomposed the image into different bands based on the spatial frequency and orientation, and just averaged those numbers over the whole image *click* for a total of 16 numbers

so this was a significantly simpler model. but when they had it perform the same classification task as before... this simpler one did almost as well. they ended up with like 95% accuracy. so their new model was better, but not by much. this was confusing --- was their model *really* not much better than this super simple one. it's possible, surely, but maybe something else is going on.

---

<div data-animate data-load="assets/julesz.svg">
<!-- {"setup": [
{"element": "#g1831", "modifier": "attr", "parameters": [ {"class": "fragment appear-disappear", "data-fragment-index": "0"} ]}
]} -->
</div>

#note: so they turned to an idea from Bela Julesz, who had worked on textures since the 1960s. he was interested in second-order statistics, such as contrast. but the important bit was not how he understood textures, but how he sought to test his ideas. as he summarized it in a later paper: *click and read*

so Javier and Eero took this back to their model. what if they could come up with images that were matched in the statistics the model cared about, but everything else was random? if the statisitcs the model captured were the same as those that the human used to understand textures, then the new image should look like its the same texture as the original image. this is metamer synthesis

---
## Texture metamer synthesis

<div style="display:flex;align-items:center;justify-content:center;flex-direction:width">
<div style="flex:2 1 auto"><img data-src="assets/basket.jpg"></div>
<img class='fragment appear' data-fragment-index="0" style="flex:2 1 auto" data-src="assets/texture-two-models.svg">
<div class='fragment appear' data-fragment-index="1" style="flex:1 1 auto;width:50%">
<video data-autoplay data-src="assets/texture-pyr-synthesis.mp4"></video>
<video data-autoplay data-src="assets/texture-model-synthesis.mp4"></video>
</div>
</div>

#note: so that's what they did. they took texture images like this, sent them through the two models to get the "target statistics", the set of numbers that we need to match. they then took some white noise and ran gradient descent, updating the pixel values until those statistics matched. that looked like this.

so this image in the top row, according to the simple model, looks like the same texture as our original basket. same is true for the bottom row and the new and improved texture model. we can see that, as humans, we think the texture model has better captured this texturiness. put another way, the 16 numbers in the simpler model are sufficient to perform texture classification on that data set. they are not sufficient for synthesis.

Eero and Javier were pretty proud of this; they thought this was a nifty idea and that it showed their texture model was pretty good

---

## Metamer synthesis

<div data-animate data-load="assets/plen-synth-4.svg">
<!-- {"setup": [
{"element": "#rect6595-6", "modifier": "attr", "parameters": [ {"display": "none"} ] },
{"element": "#rect6595-7", "modifier": "attr", "parameters": [ {"display": "none"} ] },
{"element": "#rect6595", "modifier": "attr", "parameters": [ {"display": "none"} ] }
]} -->
</div>

#note: so to bring this back to our schematic here, Eero and Javier built a model and came up with a set of parameters, fed it a natural image of a texture, which gave them a statistic to match. they then used optimization to generate some novel images, starting from different patches of white noise, and the did this for many different textures. 

---

## Metamer usage

- Model validation <!-- .element: class="fragment" data-fragment-index="0" -->
- Model comparison <!-- .element: class="fragment" data-fragment-index="1" -->
- Model development <!-- .element: class="fragment" data-fragment-index="2" -->
- Parameter fitting <!-- .element: class="fragment" data-fragment-index="3" -->

#note: in this case, metamers served several purposes: 
- validation of the model: the texture model metamers look like textures from the same family to human observers
- model comparison: the texture model metamers look "better" than those of the simple V1-like model, even though that model could also perform texture classification very well
- more subtle, but validating that the components of the model were all necessary. the model had about 700 statistics, which fall into about 10 families: marginal pixel stats, cross-correlations across scales, across orientations, auto-correlations, etc. they removed each of these families from the model in turn and ran metamer synthesis again to see the effect. this allowed them to both get a sense for what each family was capturing in the image and also that all of them were necessary in order to result in good texture metamers. in this way, metamers contributed the development and improvement of the model.

while it didn't come up in this experiment, metamers can also be used to find the best parameter value. both in work from Jeremy Freeman around 2011 and myself during my PhD, we had models with a single parameter, generated model metamers for a range of parameter values, and then used those resulting images in a psychophysical experiment to determine for which parameter values were the model metamers also human metamers.

---

## It's not the 90s anymore!

<div data-animate data-load="assets/90s.svg">
<!-- {"setup": [
{"element": "#image2455", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]},
{"element": "#image2443", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]},
{"element": "#image765", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "2"} ]},
{"element": "#g3580", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "3"} ]}
]} -->
</div>

#note: but, you might say, it's not the 90s anymore! we're not listening to NSync, we're not worried about Y2K, and we know that datasets like this Brodatz one with about 100 images, are too small!

Surely the issue was that their dataset was too small and so the task was too easy.

now we have datasets like CIFAR-10, COCO, and ImageNet, which have thousands or millions of images. surely if they played the classification game on datasets with millions of images, they wouldn't have had this issue. with enough images, you wouldn't have this issue

you might think so, but...

---
## Image space is impossibly vast!

<div data-animate data-load="assets/image-space.svg">
<!-- {"setup": [
{"element": "#g19211", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]},
{"element": "#g19217", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]},
{"element": "#g19277", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "2"} ]},
{"element": "#g19524", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "3"} ]},
{"element": "#g19205", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "4"} ]}
]} -->
</div>

#note: image space is impossibly vast! and I'm going to be a bit pedantic about this. say we had a two by two binary image. each pixel can either be black or white, and we have four of them. how many images are there? it's a pretty small set, we can easily enumerate them, flipping pixels until we get to all 16.

so we have 16 possible 2x2 binary images. that is, we have 2^4 images because we have two possible pixel values and 4 pixels

you see where I'm going with this

---

## Image space is impossibly vast!

<div data-animate data-load="assets/image-space-2.svg">
<!-- {"setup": [
{"element": "#g10347", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]},
{"element": "#g20857", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]},
{"element": "#g20945", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "2"} ]},
{"element": "#g21236", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "3"} ]},
{"element": "#g13548", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "4"} ]},
{"element": "#image15239", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "5"} ]},
{"element": "#text25217", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "6"} ]}
]} -->
</div>

#note: we have 16 2x2, then 65k 4x4, then 10^19 8x8, then 10^77 16x16, and we could keep going, but we're already at about the number of protons int he universe, 10^80

and that's only with binary images, rather than the 256 possible values we get in typical 8 bit images. 

and you might say, well hold on, the vast majority of those images will look pretty much identical -- I certainly can't tell the difference between two images if the only difference is that the center pixel differs by a value of 1. so I don't need to look at *all* images

that's fair enough

---
## Some totally random image pairs

<div data-animate data-load="assets/adversarial_examples.svg">
<!-- {"setup": [
{"element": "#g9780", "modifier": "attr", "parameters": [ {"display": "none"} ]},
{"element": "#text9842", "modifier": "attr", "parameters": [ {"display": "none"} ]}
]} -->
</div>

#note: to take some totally random pairs of images, if I were to show you the images on the left side of the plus sign, add a small amount of noise as shown in the middle and end up with the images on the right, you'd have pairs of images that differ in some surely neglibible amount, so surely we don't need to consider both images in these pairs

you, with your human visual system, see them as identical.

but if you were AlexNet

---
## AlexNet Adversarial examples

<img data-src="assets/adversarial_examples.svg"></img>
#note: you'd see all these images on the right as ostriches.

these are adversarial examples, and this example is quite old, but the point is that there are dragons lurking in image space --- we can't explore it all and, as models get complicated, we can't assume that our intuitions about images, which have been developed over millenia of evolution, will be reflected by the models we build

---
<img data-src="assets/advertisement_slide.svg"></img>

#note: so that's the point of plenoptic. the goal of plenoptic is to help guide you, to help find sets of images, like the model metamers we discussed earlier that are particularly informative for reasoning about how your computational model makes sense of images.

We are on pip, we're up on github, we have documentation, and this has been the work of many people, mostly but not exclusively in Eero's lab, over the past 4 or so years. we don't have a lot of time, so I think I'm going to jump in and work through the notebook?

---

## The Plan

<div data-animate data-load="assets/plan.svg">
<!-- {"setup": [
{"element": "#g17680", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]},
{"element": "#g1", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]},
{"element": "#g17797", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "2"} ]}
]} -->

#note: I have a notebook I'm going to walk us all through, but first I'd like to foreshadow what we're going to do for the rest of the session. I'm going to walk us through using plenoptic with three different convolutional models of increasing complexity.

- The first is a simple Gaussian filter. Convolving a filter with an image blurs it, as I'm sure many of you know. This means that the model is throwing away high frequency information, which are responsible for the sharp lines in an image, while preserving the low frequencies. This isn't a model anyone uses in the visual system, but it's simple and will allow us to get our legs under us
- The second is a CenterSurround model, constructed from taking the difference of two Gaussians, one larger than the other. This is similar to how people model retinal ganglion cells and neurons in the lateral geniculate nucleus. This model has a bandpass selectivity, meaning that it cares mostly about middle frequencies, and less about both low and high frequencies.
- Finally, we'll introduce some nonlinearities with a LuminanceGainControl model. We'll take the CenterSurround filter, divide its response by local luminance (computed with a larger Gaussian) and then rectify that, throwing away any negative values. Gain control is a proposed "canonical computation" and shows up across the central nervous system, where it's proposed to help the brain maximimize sensitivity to relevant stimuli in changing contexts. here, it will make our model insensitive to luminance, and focus its sensitivity on contrast (the other linear models mixed contrast and luminance in their responses). This also has the flavor of a retinal ganglion cell or LGN neuron, but with this additional nonlinearity; whether it would be relevant for a given data set depends on the experiment: if you only ever showed stimuli whose overall luminance varied in a relatively small range, it would be unnecessary

We're going to use these models with metamer synthesis, which I've described already. with metamers, we pass a target image, here the cows, through the to get a target representation. we then start with another image, by default white noise, and update its pixels *click* until the representations match

Finally, we're also going to use these models with eigendistortions. this is a different method, for examining the most and least noticeable change in an image. we again start with a target image, and then we find the eigenvectors of the model's Fisher information matrix, which in our setup is basically the model's gradient with respect to the specific image. this allows us to say, given a certain pixel budget, how can I spend those pixels in the way that the model thinks is the most obvious, that changes the representation the most, and in the way that the model thinks is the least obvious, which changes the representation the least. (note this has a similar feel to metamers, but in practice does not the result in the same images). eigendistortion will give us two distortions, which we can then add to the reference image, in order to overlay them. all good?

---

## a very important link

https://labforcomputationalvision.github.io/plenoptic-cshl-vision-2024/

#note: everyone go ahead to that address. that will take you to the website that has the notebooks we'll use. I'm going to post this in the slack as well, so I can show you what this will look like.

I'd encourage you to keep this website up for reference. it has a glossary with some terms that might be unfamiliar -- I'll try to explain them, but you know how it is. it has two versions of the notebook we'll be going through, one with text and one without. today, we'll be working through the version without text, with me explaining as we go, but if you want to come back to this later, you can come back to this website -- the text is basically what I'm saying

today, we're going to use this binder link here, which will open up the notebook in an environment with a gpu. I got the emails you registered for the course with from Eline, so login with those. if that doesn't work or you want to use a different email address, send me a slack of the email address and I'll give you permission. once you've got into the binder and the notebook has rendered, put up your green sticky
