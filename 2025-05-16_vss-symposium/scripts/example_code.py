#!/usr/bin/env python3

import plenoptic as po
import matplotlib.pyplot as plt

def create_figure(met):
    fig, axes = plt.subplots(1, 4, figsize=(16, 4))
    po.imshow(met.image, ax=axes[0], title="Original image")
    axes[0].set_axis_off()
    fig, axes_idx = po.synth.metamer.plot_synthesis_status(met, fig=fig, axes_idx={"misc": 0},
                                                           iteration=0)
    fig.tight_layout(w_pad=.1, rect=(0, 0, 1, .9))
    return fig, axes_idx


def base():
    """
    >>> import plenoptic as po
    >>> # Load image into Pytorch tensor
    >>> img = po.data.einstein()
    >>> # Initialize model
    >>> model = po.simul.CenterSurround(kernel_size=(31, 31),
    ...                                 cache_filt=True)
    >>> # Detach gradients from model -- model parameters are fixed.
    >>> po.tools.remove_grad(model)
    >>> # Initialize metamer object
    >>> met = po.synth.Metamer(img, model)
    >>> # Synthesize model metamer
    >>> met.synthesize(max_iter=100, store_progress=5)
    >>> fig, axes_idx = create_figure(met) # ignore
    >>> fig.savefig("{filename}-{func}-init.svg") # ignore
    >>> po.synth.metamer.animate(met, framerate=5, fig=fig, axes_idx=axes_idx).save("{filename}-{func}.mp4", dpi=300) # ignore
    >>> fig.savefig("{filename}-{func}-final.svg") # ignore
    """
    "hi"


def gpu_one():
    """
    >>> import plenoptic as po
    >>> # Load image into Pytorch tensor
    >>> img = po.data.einstein().to("cuda")
    >>> # Initialize model
    >>> model = po.simul.CenterSurround(kernel_size=(31, 31),
    ...                                 cache_filt=True)
    >>> # Move model object to GPU
    >>> model = model.to("cuda")
    >>> # Detach gradients from model -- model parameters are fixed.
    >>> po.tools.remove_grad(model)
    >>> # Initialize metamer object
    >>> met = po.synth.Metamer(img, model)
    >>> # Synthesize model metamer
    >>> met.synthesize(max_iter=100, store_progress=5)
    >>> fig, axes_idx = create_figure(met) # ignore
    >>> fig.savefig("{filename}-{func}-init.svg") # ignore
    >>> po.synth.metamer.animate(met, framerate=5, fig=fig, axes_idx=axes_idx).save("{filename}-{func}.mp4", dpi=300) # ignore
    >>> fig.savefig("{filename}-{func}-final.svg") # ignore
    """
    "hi"


def gpu_two():
    """
    >>> import plenoptic as po
    >>> # Load image into Pytorch tensor
    >>> img = po.data.einstein()
    >>> # Initialize model
    >>> model = po.simul.CenterSurround(kernel_size=(31, 31),
    ...                                 cache_filt=True)
    >>> # Detach gradients from model -- model parameters are fixed.
    >>> po.tools.remove_grad(model)
    >>> # Initialize metamer object
    >>> met = po.synth.Metamer(img, model)
    >>> # Move Metamer object to GPU
    >>> met.to("cuda")
    >>> # Synthesize model metamer
    >>> met.synthesize(max_iter=100, store_progress=5)
    >>> fig, axes_idx = create_figure(met) # ignore
    >>> fig.savefig("{filename}-{func}-init.svg") # ignore
    >>> po.synth.metamer.animate(met, framerate=5, fig=fig, axes_idx=axes_idx).save("{filename}-{func}.mp4", dpi=300) # ignore
    >>> fig.savefig("{filename}-{func}-final.svg") # ignore
    """
    "hi"


def custom_image():
    """
    >>> import plenoptic as po
    >>> # Load image into Pytorch tensor
    >>> img = po.load_images("/home/billbrod/Desktop/reptile_skin.png")
    >>> # Initialize model
    >>> model = po.simul.CenterSurround(kernel_size=(31, 31),
    ...                                 cache_filt=True)
    >>> # Detach gradients from model -- model parameters are fixed.
    >>> po.tools.remove_grad(model)
    >>> # Initialize metamer object
    >>> met = po.synth.Metamer(img, model)
    >>> # Synthesize model metamer
    >>> met.synthesize(max_iter=100, store_progress=5)
    >>> fig, axes_idx = create_figure(met) # ignore
    >>> fig.savefig("{filename}-{func}-init.svg") # ignore
    >>> po.synth.metamer.animate(met, framerate=5, fig=fig, axes_idx=axes_idx).save("{filename}-{func}.mp4", dpi=300) # ignore
    >>> fig.savefig("{filename}-{func}-final.svg") # ignore
    """
    "hi"


def custom_image():
    """
    >>> import plenoptic as po
    >>> # Load image into Pytorch tensor
    >>> img = po.load_images("/home/billbrod/Desktop/reptile_skin.png")
    >>> # Initialize model
    >>> model = po.simul.CenterSurround(kernel_size=(31, 31),
    ...                                 cache_filt=True)
    >>> # Detach gradients from model -- model parameters are fixed.
    >>> po.tools.remove_grad(model)
    >>> # Initialize metamer object
    >>> met = po.synth.Metamer(img, model)
    >>> # Synthesize model metamer
    >>> met.synthesize(max_iter=100, store_progress=5)
    >>> fig, axes_idx = create_figure(met) # ignore
    >>> fig.savefig("{filename}-{func}-final.svg") # ignore
    >>> po.synth.metamer.animate(met, framerate=5, fig=fig, axes_idx=axes_idx).save("{filename}-{func}.mp4", dpi=300) # ignore
    """
    "hi"
