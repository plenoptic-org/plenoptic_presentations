![](assets/plenoptic_logo.svg) <!-- .element: style="height:50%" -->

---
## Models in vision

<div data-animate data-load="assets/models.svg">
<!-- {"setup": [
{"element": "#g4005-8-1", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]},
{"element": "#g4005-8-3", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]},
{"element": "#g4005-8-7-43", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "2"} ]},
{"element": "#g5626", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "3"} ]},
{"element": "#g5535", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "3"} ]},
{"element": "#g4581", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "4"} ]},
{"element": "#g5685", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "4"} ]},
{"element": "#g7636", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "5"} ]},
{"element": "#g7589", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "6"} ]},
{"element": "#g5948", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "7"} ]}
]} -->
</div>

#note: the package I work on deals with models in vision science. these are models that accept some image as input and maps it to whatever you want to study. this could be neural firing rate, some decision your participants are making, or the brain response as measured by fMRI, among others. one common one, which I'll use for this example, is image category. so my model looks at this picture and learns to label it as "bus".

and we'd do this for a whole bunch of images, learning that this is a grouse, this is a dog, and so on.

the goal of plenoptic is to help you answer "how does my model do this?" what is it seeing in this image that makes it think "ah ha, this is a bus!" you might think, well that's obvious, it's clearly seeing that it's yellow, it has tires and headlights, and it's really long. but that's how *you* figured out it was bus, and your visual system has evolved for millenia in order to do labeling like that. you can't assume your model is solving the problem in the same way.

in fact, there was a paper from 2013 that took a model that did this kind of task and performed *exceedingly* well. as good as humans on a dataset with 16 million images. they then changed the pixel values very slightly in this strange way, to end up with these photos. these photos look unchanged to you, as they do to me and all other people. but their model was convinced that now, all these pictures showed ostriches

the point is, even if your model seems to be behaving like humans, you can't assume it's solving the problem in the same way. you need to explore, to show your model many different pictures in order to figure out how it's performing the task.

but, unfortunately you can't just show your model every image that exists

---

## There are so many images!

<div data-animate data-load="assets/image-space.svg">
<!-- {"setup": [
{"element": "#g19211", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "0"} ]},
{"element": "#g19217", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "1"} ]},
{"element": "#g19277", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "2"} ]},
{"element": "#g19524", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "3"} ]},
{"element": "#g19205", "modifier": "attr", "parameters": [ {"class": "fragment appear", "data-fragment-index": "4"} ]}
]} -->
</div>

#note: because there are so many images! say we had a really small image, just two by two, with two possible pixel value;. each pixel can either be black or white, and we have four of them. how many images are there? it's a pretty small set, we can easily enumerate them, flipping pixels until we get to all 16.

so we have 16 possible 2x2 binary images. that is, we have 2^4 images because we have two possible pixel values and 4 pixels

---

## There are so many images!

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

so you can't look at every possible image, and there are likely dragons out there among the images you haven't looked at yet.

---

![](assets/advertisement_slide.svg)

#note: so plenoptic helps guide you, to help find sets of images that are particularly informative for reasoning about how your computational model makes sense of images, like those image sets we showed you before

this project actually came out of the lab I got my PhD in. it contains a variety of methods that were developed in the lab over the years, but we had a pretty common problem: people had written the code for a paper, then graduated and moved on, and now we couldn't get their code to work. so a bunch of us sat down and said -- we can fix this! so we tried to rewrite the code into a coherent framework, didn't think it would be that hard. and four years later, here I still am, working on this
