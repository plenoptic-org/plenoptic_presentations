# Introduction to plenoptic

## Winawer lab meeting
## Oct 2, 2023

---

![](assets/plen-1.0.1-intro-1.svg)

#note: so I'm going to talk about plenoptic, which is a python library that performs "model-based synthesis of perceptual stimuli" to help better understand those computational models. I'm going to briefly describe what that means. key word is "synthesis"

but before I go on, summarizing the contents of plenoptic is like summarizing the work of at least 5 grad students and 2 postdocs from Eero's lab. I'm focusing on the high level idea of what do these methods *do* and how can they be used, but it's a lot of material and this is my first attempt at doing this so ... thanks for being guinea pigs! and please interrupt me with questions if something isn't clear. I'm hoping on giving variants of this talk over and over to different vision scientists, so any feedback on how to improve it are much appreciated. and it's why I'm starting here.

---

![](assets/plen-1.0.1-intro-2.svg)

#note: we've represented synthesis with this little abstract logo. This represents the relationship between computational models, their inputs, outputs, and parameters.

---

![](assets/plen-synth-1.svg)

#note: To make that slightly less abstract, here is a diagram of a model in visual neuroscience. it accepts some stimuli s, often for us images, as inputs, and based on some parameters theta, returns some responses r. these responses can be anything of interst to the experimenter, such as predicted spike rates or image class, if this were doing image net

---

## Simulate responses
![](assets/plen-synth-2.svg)

#note: now the way that models are most commonly used, is that we feed them an input and some parameter values and we simulate the responses.

---
## Fit parameters
![](assets/plen-synth-3.svg)

#note: we often pretty regularly fix the responses for a set of stimuli and use backpropagation to fit the parameters

---
## Synthesize stimuli
![](assets/plen-synth-4.svg)

#note: but there's nothing special about the stimuli. we can similarly hold both the responses and parameters constant and use back propagation to generate novel stimuli. 

this is what we call synthesis -- updating the pixel values of an image based on a model with set parameter values and some intended output.

---
## Metamers
Physically distinct stimuli that are perceptually identical  <!-- .element: class="margin-top" -->

#note: one such method is metamer synthesis. in the study of perception, metamers are physically distinct stimuli that are perceptually identical.

the classic example of metamers come from color perception.

---
## Metamers
![](assets/metamer-room.jpg) <!-- .element: style="margin-top:5%;height:950px;width:auto" -->

#note: when you look at this picture of this room, compared to the room in real life, they look like they're the same color. however, the physical light that is entering your eye is *very* different, because this projector only has three color channels (RGB), and so it cannot hope to exactly match the energy at every wavelength in the visual light spectrum

however, it doesn't need to

---
## Metamers
![](assets/plen-metamer-cones.svg)

#note: because of how the human eye transforms physical light into perceptual color. humans only have three cone classes, called short, medium, and long based on which wavelengths they're most sensitive to.

That means you only need those three color channels to match human color perception -- and for colorblind people who have only two cone classes, you'd need only two color channels.

---
## Metamers
Physically distinct stimuli that are perceptually identical <!-- .element: class="margin-top" -->

#note: so that's metamers -- physically different stimuli, but perceptually identical

---
## Metamers
Physically distinct stimuli that are perceptually identical (to a computational model) <!-- .element: class="margin-top" -->

#note: for plenoptic, what we're focusing on is not an organism, but a computational model. so metamers have different pixel values but identical outputs

---
## Texture model metamers
![contents](assets/texture-model-1.svg)

#note: some examples of this from Eero's lab include the texture model, which he developed with Javier Portilla in the late 90s. The goal of this model was to develop a set of statistical properties that adequately capture what makes a visual texture a texture (not a vision science goal, more engineering). That model is built off the steerable pyramid, a multi-scale, multi-orientation filter bank, which we can think of as "V1 like receptive fields", as shown here. the model measures the cross-correlations and auto-correlations of the responses of these receptive fields, as well as some marginal pixel statistics.

---
## Texture model metamers
![contents](assets/texture-model-2.svg)

#note: The question that Eero and Javier faced was: we developed this model that we think captures an images "texturiness", how do we demonstrate that it does a good job? 

they first thought, let's try classification. let's see if our model can distinguish this basket from this grain of wood. and it did *phenomenally*, performance was at ceiling on the database of ~30 textures they had (this was in the late 90s). 

but then they said wait, let's compare it against a simple spectral model as well, just measuring the energy at several spatial frequencies and orientations. and it did just as well.

so clearly the test was too easy. they came up with another solution: let's take a texture image...

---
## Texture model metamers
![contents](assets/texture-model-3.svg)

#note: and a patch of white noise and let's adjust the pixels in the white noise image so that, eventually, it has the same texture statistics as the texture image. if our model is good, then the output of that process will look perceptually similar to the original image. That is, if we generate a metamer for our texture model, the human should believe it belongs to the same category.

let's watch

---
## Texture model metamers
<div class="column" style="float:left; width:65%">

![contents](assets/texture-model-2-half.svg) 

</div>

<div class="column" style="float:right; width:35%; margin-top: 6.5%">
<video data-autoplay src="assets/texture-model-synth.mp4"></video>
</div>

#note: so we can see that it gets very similar. Note they're not looking for *identical* here (and they didn't run any psychophysics), because their model cares more about texture category (fur, baskets, etc).

---
## Texture model metamers
![contents](assets/texture-model-4.svg)

#note: so this works for the basket...

---
## Texture model metamers
![contents](assets/texture-model-5.svg)

#note: ... it works for other textures, like this wood grain

---
## Texture model metamers
![image](assets/texture-model-5a.svg)

#note: while it did really well on those first two, there are some textures it has a bit more trouble on. here we can see it struggles to break these tiles up into discrete units. it has trouble capturing perfectly straight lines like this.

---
## Texture model metamers
![contents](assets/texture-model-6.svg)

#note: and it allows you to do other intersting things, like extrapolating a texture beyond its borders or mixing two textures together

---
## Texture model metamers
![contents](assets/texture-model-7.svg)

#note: but it's a texture model, so it doesn't work for arbtirary images. this portrait of Einstein isn't a texture, so the texture metamer (predictably) looks nothing like the original image. so this is one sort of thing that can be done with model metamers: validating whether this image-computable model adequately captures the appearance of textures.

---
## More model metamers!
![contents](assets/fovmet.png) <!-- .element: style="height:950px;width:auto" -->

#note: and as another example, these may look familiar to some of you. I built foveated models of the early visual system, which computed the local luminance or spectral energy in receptive-field like regions, which grew with eccentricity across the image. I then generated model metamers for different sizes of these images and showed them to humans in a psychophysics experiment (which, those who took part can attest, was super fun). I used these to find the parameter value for which the models and the humans agreed on which images were indistinguishable. that is, we used this metamer framework to find the size of the regions wherein humans would be insensitive to changes in either luminance or spectral energy

---
## Why do this?

- Improve understanding of computational models <!-- .element: class="fragment margin-top" data-fragment-index="1" -->
- Image space is vast! <!-- .element: class="fragment" data-fragment-index="2" -->
- Better understand single model or compare between competing models <!-- .element: class="fragment" data-fragment-index="3" -->

#note: For those of you who haven't heard of this approach, you might wonder, why do
this?

the goal is to improve our understanding of how our computational models make sense of their input. as adversarial examples and other similar techniques have shown, that's not trivial! just because a model does well on image net doesn't mean it won't behave unexpectedly on new / out-of-distribution data

image space is vast, so any possible dataset is a tiny sample of it, and the methods in plenoptic provide a different and targeted way of exploring this space.

they can be used for:
- improving understanding of a given model -- for example, fit a model to a visual neuron, then generate some stimuli with plenoptic and use it in a new experiment
- another way of comparing models: many models can do equivalently (or near equivalently) well on a given benchmark, and plenoptic's methods provide a complementary approach for comparing them.


---
## But wait there's more!

- Eigendistortion: most and least noticeable changes to an image. <!-- .element: class="margin-top" -->
- Maximally Differentiating (MAD) Competition: efficiently compare two visual models.
- Representation geodesic: in a movie, what does the model think the most likely next frame is?

#note: in addition to metamers, there are three other synthesis methods found in plenoptic, all based on research done in Eero's lab over the years. I'll describe each of them in a bit more detail, but they're all attempts to interrogate how visual models understand images and how we can compare them to biological perception in new ways.

---
## But wait there's more!

- Eigendistortion: most and least noticeable changes to an image. <!-- .element: class="margin-top" -->
- Maximally Differentiating (MAD) Competition: efficiently compare two visual models. <!-- .element: style="color: #bebebe" -->
- Representation geodesic: in a movie, what does the model think the most likely next frame is? <!-- .element: style="color: #bebebe" -->

#note: let's talk about eigendistortions first.

---
## How to noticeably change an image?
![contents](assets/eigendist-intro-1.svg)

#note: this starts with a seemingly simple question: if you have an image and a pixel budget, how can you most, or least, noticeably change that image. That is, if I have this picture of a parrot, and I can change the pixel values so that I end up with an image whose mean-squared error with the original is .01, what should I do?

---
## How to noticeably change an image?
![contents](assets/eigendist-intro-2.svg)

#note: should I spread that as noise everywhere across the image?

---
## How to noticeably change an image?
![contents](assets/eigendist-intro-3.svg)

#note: should I uniformly increase the value of all the pixels?

---
## How to noticeably change an image?
![contents](assets/eigendist-intro-4.svg)

#note: should I concentrate my changes in just a portion of the image? all three of these pixels have the same MSE with the original image, but we've spent that pixel budget in different ways. and so discriminating these images apart from the original has different difficulties: we're very good at detecting these contrast edges, but not so good at an overall shift in luminance. and the noise is fairly noticeable as well.

if we have a model, we can ask what changes *the model* thinks are easy or hard to detect, and use them in a human experiment.

---
## How to noticeably change an image?
![contents](assets/eigendist-intro-5.svg)

#note: this is important because we know from adversarial examples that just because a model seems to behave similar to human perception (here, classifying images into different categories), that does not mean that they'll agree what changes are obvious. This model thinks this noise pattern is enough to switch the image category from a dog to an ostrich, but humans find it indetectable.

---
## Eigendistortions
![contents](assets/eigendistortions-1.svg)

#note: you can do this for two possible models of the human visual system, one a simple 4-layer convolutional neural network, and one a physiologically-inspired on-off model with contrast and luminance normalization. you can see that the OnOff model thinks that, to make changes noticeable, you should make high contrast, localized changes, and do the opposite to make them invisible, spread them out and make them low contrast. the CNN, on the other hand, thinks that uniform noise is not noticeable, and does something somewhat similar to the On Of to make it noticeable, though less localized and less contrast.

---
## Eigendistortions
![contents](assets/eigendistortions.svg)

#note: you can run a psyhophysics experiment to see how human perception aligns, and use that to compare the models. they ran more models than this, but let's just focus on these two. on the y-axis is the threshold for detection: what value did they need to multiply the eigndistortion on the top by before humans noticed it. in the examples here, the most noticeable has been multiplied by 4, the bottom by 30. so the further apart these two dots are, the more the human agrees with the model.

---
## More synthesis!

- Eigendistortion: most and least noticeable changes to an image. <!-- .element: class="margin-top" style="color: #bebebe" -->
- Maximally Differentiating (MAD) Competition: efficiently compare two visual models.
- Representation geodesic: in a movie, what does the model think the most likely next frame is? <!-- .element: style="color: #bebebe" -->

#note: now let's talk about MAD Competition. So far, I've talked a bit about comparing models to each other, but it's always been a bit implicit. what if you have two models that perform really similar to each other. for example, you're fitting pRFs and trying to decide whether they can be linear or whether you should add a compressive nonlinearity, like a power-law, on the end. for many images, the predictions of those two models are going to be relatively similar, and you really want to exaggerate them, to find the stimuli where their predictions will *really* differ. you can think carefully about the two models, how they differ, and try to build the proper stimuli by hand, but that's hard, and will  get harder and harder as your models get more complex. 

or ... you could use MAD competition, who generates a set of stimuli that have *maximally different* predictions for the two models. let's step through how that works

---
## Simple MAD Competition
![img](assets/simple-mad.svg)

#note:
with a super simple example: we'll take a two-pixel image, each has value .5,
and add some noise, then run MAD Competition between the L1 and L2 norms. so the
L1 model thinks you can tell how different two points are by taking the absolute
value of the difference of x and y and summing them, while the L2 takes the
Euclidean norm of their difference, taking the difference between x and y,
squaring that, summing them, and taking the square root.

with this simple one first because we can actually plot it, with pixel 1 on the
x-axis and pixel 2 on the y, and we can also plot the level sets of our two
metrics.

- so we start with a reference point, in red
- we add some nosie to it, to get our initial point
- and the diamond and the circle give us the level sets of L1 and L2. that is,
  the L1 model thinks that all points which lie on the blue diamond are all *as
  different* from the red point as the black one. if you were to run this
  through psychophysics, L1 predicts the discrimination performance of every
  point on the diamond is the same
- L2 thinks that about the circle.
- makes sense?

---
## Simple MAD Competition
![img](assets/simple-mad-1.svg)

#note:
- this then is one MAD image, where we've maximized L2 norm while keeping L1
  constant
- that is, L1 thinks the black and blue points are just as different from the
  red point, whereas L2 thinks the blue is *as different as possible*
- this puts it "along the axis", so that one pixel has the same value as our
  reference image, and the other is as extremal as possible
- the other corners of the diamond would also satisfy this, and the fact that we
  ended up here is because it's closer to our initial image and we used
  iterative optimization.

---
## Simple MAD Competition
![img](assets/simple-mad-2.svg)


#note:
- we can similarly max the L1 norm, which moves us along the L2 level set and
  moves us as far away from reference image as possible
- this puts it "on the diagonal", so that neither pixel has the same value as in
  the reference, but they individually have the same difference (about .07)
- again, other diagonals would also have worked, but this is the one we were
  closest to


---
## Simple MAD Competition
![img](assets/simple-mad-all.svg)

#note:
- now add the final two dots, corresponding to minimizing L1 and L2,
  respectively
- we see that they move along their respective level sets, ending up in the same
  two positions, along the axes and diagonal, but with lower overall value
- and note that they're swapped: max L1 puts you along the diagonal, minimizing
  it puts you along the axes, for analogous reasons -- you have to stay along L2
  level set and the place that does that and minimizes L1 is along the axis,
  where pixel 1 has no difference and pixel 2 has the minimum possible
  difference, given our L2 level set
- analogously for min L2.
- does that make sense? we've generated a set of points where the predictions of
  the two models disagree *as much as possible*
- this then allows us to efficiently compare the two models

---
## MAD Competition
![image](assets/mad-mse-ssim.svg)

#note: back in 2008, Eero did this work with a postdoc called Zhou Wang, comparing mean-squared error with SSIM, the strucural similarity metric, which was their proposed way of measuring how different two images are

this has the same layout as the last slide, with the reference image up here, which they added noise to, and then held either MSE or SSIM constant while changing the other as much or as little as possible. all of these look bad to me except this top one, so when holding MSE constant, you get two bad and one good image, while holding SSIM constant, you get three pretty bad images.

Eero, Zhou, and their collaborators won an Emmy for their work on SSIM, as an aside. because it was so useful to the television and movie industries, as a way of measuring the effects of compression (I think)

---
## More synthesis!

- Eigendistortion: most and least noticeable changes to an image. <!-- .element: class="margin-top" style="color: #bebebe" -->
- Maximally Differentiating (MAD) Competition: efficiently compare two visual models. <!-- .element: style="color: #bebebe" -->
- Representation geodesic: in a movie, what does the model think the most likely next frame is? 

#note: and the last one: geodesic. geodesic is about prediction. 

---
## Contents
![contents](assets/plen-contents-2.svg)

#note:

---
## Status and Roadmap
<div class="column margin-top" style="float:left; width:80%">

- All methods, models are implemented
  - Currently improving geodesics and refactoring texture model
- Working on improving tutorials and documentation, cleaning up code base
- Looking for feedback and users!
  - https://plenoptic.readthedocs.io/

</div>

<div class="column margin-top" style="float:right; width:20%">

![qr](assets/plen-docs-qr.svg)

</div>

#note: so currently, all methods and models that I just described are implemented, documented, and tested, though I'm working on some improvements to one of them, geodesics

I'm also generally looking to improve the tutorials and docs, especially to make sure it's understandable to folks who haven't been in Eero's lab for >5 years, and cleaning up the code base

I'm actively looking for feedback and users -- if you scan that qr code or go to that url, you'll find my docs.

At this point, I'm happy to work with anyone who wants to use plenoptic. I know most of you aren't comfortable in python, so I'm happy to meet regularly to help folks write their models in pytorch and to help with the project.

---
## Developers
![dev](assets/plen-people-details.svg)

#note: I want to point out that wasn't just me -- I'm the maintainer and core developer now, but this was the work of 7 folks in Eero's lab since 2019.

---
## Developers
![dev](assets/plen-people-details-and-you.svg)

#note: I'm not just interested in more users, but in new contributors as well.

We're about to finish merging our first substantial PR from someone outside the lab! Daniel Herrera from Johannes Burges's lab
