![](assets/plenoptic_logo.svg) <!-- .element: style="height:50%" -->

## CSHL Vision 2024
## Billy Broderick <!-- .element: style="height:50%" -->

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
<div style="flex:2 1 auto"><img src="assets/basket.jpg"></div>
<img class='fragment appear' data-fragment-index="0" style="flex:2 1 auto" src="assets/texture-two-models.svg">
<div class='fragment appear' data-fragment-index="1" style="flex:1 1 auto;width:50%">
<video data-autoplay src="assets/texture-pyr-synthesis.mp4"></video>
<video data-autoplay src="assets/texture-model-synthesis.mp4"></video>
</div>
</div>

#note: so that's what they did. they took texture images like this, sent them through the two models to get the "target statistics", the set of numbers that we need to match. they then took some white noise and ran gradient descent, updating the pixel values until those statistics matched. that looked like this.

so this image in the top row, according to the simple model, looks like the same texture as our original basket. same is true for the bottom row and the new and improved texture model. we can see that, as humans, we think the texture model has better captured this texturiness. put another way, the 16 numbers in the simpler model are sufficient to perform texture on that data set. they are not sufficient for synthesis.

Eero and Javier were pretty proud of this; they thought this was a nifty idea and that it showed their texture model was pretty good

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

<div data-animate data-load="assets/image-space-test.svg">
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
{"element": "#g9931", "modifier": "attr", "parameters": [ {"display": "none"} ]}
]} -->
</div>

#note: to take some totally random pairs of images, if I were to show you the images on the left side of the plus sign, add a small amount of noise as shown in the middle and end up with the images on the right, you'd have pairs of images that differ in some surely neglibible amount, so surely we don't need to consider both images in these pairs

you, with your human visual system, see them as identical.

but if you were AlexNet

---
## AlexNet Adversarial examples

![](assets/adversarial_examples.svg)
#note: you'd see all these images on the right as ostriches.

these are adversarial examples, and this example is quite old, but the point is that there are dragons lurking in image space --- we can't explore it all and, as models get complicated, we can't assume that our intuitions about images, which have been developed over millenia of evolution, will be reflected by the models we build

---
![](assets/advertisement_slide.svg)

#note: so that's the point of plenoptic. the goal of plenoptic is to help guide you, to help find sets of images, like the model metamers we discussed earlier that are particularly informative for reasoning about how your computational model makes sense of images.

We are on pip, we're up on github, we have documentation, and this has been the work of many people, mostly but not exclusively in Eero's lab, over the past 4 or so years. we don't have a lot of time, so I think I'm going to jump in and work through the notebook?

---

## https://binder.flatironinstitute.org/~wbroderick/cshl2024

#note: everyone go ahead to that address. that will take you to a binder instance with a notebook we'll step through. normally, I like to do live coding, giving you an empty notebook and having you all follow along, but I think we don't have enough time for that, so we're going run through some cells and I'll explain the code as we go.
