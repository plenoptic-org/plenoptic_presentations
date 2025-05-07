#!/usr/bin/env python3

import plenoptic as po
import matplotlib.pyplot as plt
import torch
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
torch.set_default_device(DEVICE)

def create_met_figure(met, included_plots=None):
    if included_plots is None:
        included_plots = [
            "display_metamer",
            "plot_loss",
            "plot_representation_error",
        ]
    fig, axes = plt.subplots(2, 2, figsize=(8, 8))
    axes = axes.flat
    po.imshow(met.image, ax=axes[0], title="Original image")
    axes[0].set_axis_off()
    torch.set_default_device("cpu")
    vrange = (met.image.min().item(), met.image.max().item())
    fig, axes_idx = po.synth.metamer.plot_synthesis_status(met, fig=fig, axes_idx={"misc": 0},
                                                           iteration=0, vrange=vrange,
                                                           included_plots=included_plots)
    if "plot_representation_error" not in included_plots:
        axes[-1].set_visible(False)
    fig.tight_layout(rect=(0, 0, 1, .95), h_pad=2)
    return fig, axes_idx


def create_eig_figure(eig, alpha=5):
    fig, axes = plt.subplots(3, 2, figsize=(8, 12))
    axes[0, 1].set_visible(False)
    po.imshow(eig.image, ax=axes[0, 0], title="Original image")
    title = ["Max", "Min"]
    axes[0, 0].set_axis_off()
    for i in range(2):
        po.imshow(eig.eigendistortions[i:i+1], ax=axes[i+1, 1],
                  title=f"{title[i]} Eigendistortion")
        axes[i+1, 1].set_axis_off()
        po.imshow(eig.image + alpha*eig.eigendistortions[i:i+1], ax=axes[i+1, 0],
                  title=f"Image + {alpha} * {title[i]} Eigendistortion")
        axes[i+1, 0].set_axis_off()
    fig.tight_layout()
    return fig


def base():
    """
    >>> import plenoptic as po
    >>> # Load image into Pytorch tensor
    >>> img = po.data.einstein()
    >>> # Initialize model
    >>> model = po.simul.CenterSurround(kernel_size=(31, 31),
    ...                                 cache_filt=True,
    ...                                 pad_mode="circular")
    >>> # Detach gradients from model -- model parameters are fixed.
    >>> po.tools.remove_grad(model)
    >>> # Initialize metamer object
    >>> met = po.synth.Metamer(img, model)
    >>> # Synthesize model metamer
    >>> met.synthesize(max_iter=100, store_progress=5)
    >>> fig, axes_idx = create_met_figure(met) # ignore
    >>> fig.savefig("{filename}-{func}-init.svg") # ignore
    >>> po.synth.metamer.animate(met, framerate=5, fig=fig, axes_idx=axes_idx).save("{filename}-{func}.mp4", dpi=300) # ignore
    >>> fig.savefig("{filename}-{func}-final.svg") # ignore
    """
    "hi"


def eigendistortion():
    """
    >>> import plenoptic as po
    >>> # Load image into Pytorch tensor
    >>> img = po.data.einstein()
    >>> # Initialize model
    >>> model = po.simul.CenterSurround(kernel_size=(31, 31),
    ...                                 cache_filt=True,
    ...                                 pad_mode="circular")
    >>> # Detach gradients from model -- model parameters are fixed.
    >>> po.tools.remove_grad(model)
    >>> # Initialize metamer object
    >>> eig = po.synth.Eigendistortion(img, model)
    >>> # Synthesize eigendistortions
    >>> eig.synthesize(max_iter=1000);
    >>> fig = create_eig_figure(eig) # ignore
    >>> fig.savefig("{filename}-{func}-init.svg") # ignore
    """
    "hi"


def gpu_one():
    """
    >>> import plenoptic as po
    >>> # Load image into Pytorch tensor
    >>> img = po.data.einstein().to("cuda")
    >>> # Initialize model
    >>> model = po.simul.CenterSurround(kernel_size=(31, 31),
    ...                                 cache_filt=True,
    ...                                 pad_mode="circular")
    >>> # Move model object to GPU
    >>> model = model.to("cuda")
    >>> # Detach gradients from model -- model parameters are fixed.
    >>> po.tools.remove_grad(model)
    >>> # Initialize metamer object
    >>> met = po.synth.Metamer(img, model)
    >>> # Synthesize model metamer
    >>> met.synthesize(max_iter=100, store_progress=5)
    """
    "hi"


def gpu_two():
    """
    >>> import plenoptic as po
    >>> # Load image into Pytorch tensor
    >>> img = po.data.einstein()
    >>> # Initialize model
    >>> model = po.simul.CenterSurround(kernel_size=(31, 31),
    ...                                 cache_filt=True,
    ...                                 pad_mode="circular")
    >>> # Detach gradients from model -- model parameters are fixed.
    >>> po.tools.remove_grad(model)
    >>> # Initialize metamer object
    >>> met = po.synth.Metamer(img, model)
    >>> # Move Metamer object to GPU
    >>> met.to("cuda")
    >>> # Synthesize model metamer
    >>> met.synthesize(max_iter=100, store_progress=5)
    """
    "hi"


def custom_image():
    """
    >>> import plenoptic as po
    >>> # Load image into Pytorch tensor
    >>> img = po.load_images("/home/billbrod/Desktop/reptile_skin.png")
    >>> # Initialize model
    >>> model = po.simul.CenterSurround(kernel_size=(31, 31),
    ...                                 cache_filt=True,
    ...                                 pad_mode="circular")
    >>> # Detach gradients from model -- model parameters are fixed.
    >>> po.tools.remove_grad(model)
    >>> # Initialize metamer object
    >>> met = po.synth.Metamer(img, model)
    >>> # Synthesize model metamer
    >>> met.synthesize(max_iter=100, store_progress=5)
    >>> fig, axes_idx = create_met_figure(met) # ignore
    >>> fig.savefig("{filename}-{func}-init.svg") # ignore
    >>> po.synth.metamer.animate(met, framerate=5, fig=fig, axes_idx=axes_idx).save("{filename}-{func}.mp4", dpi=300) # ignore
    >>> fig.savefig("{filename}-{func}-final.svg") # ignore
    """
    "hi"


def init_image():
    """
    >>> import plenoptic as po
    >>> # Load image into Pytorch tensor
    >>> img = po.data.einstein()
    >>> # Initialize model
    >>> model = po.simul.CenterSurround(kernel_size=(31, 31),
    ...                                 cache_filt=True,
    ...                                 pad_mode="circular")
    >>> # Detach gradients from model -- model parameters are fixed.
    >>> po.tools.remove_grad(model)
    >>> # Initialize metamer object
    >>> met = po.synth.Metamer(img, model)
    >>> met.setup(initial_image=po.data.curie())
    >>> # Synthesize model metamer
    >>> met.synthesize(max_iter=100, store_progress=5)
    >>> fig, axes_idx = create_met_figure(met) # ignore
    >>> fig.savefig("{filename}-{func}-init.svg") # ignore
    >>> po.synth.metamer.animate(met, framerate=5, fig=fig, axes_idx=axes_idx).save("{filename}-{func}.mp4", dpi=300) # ignore
    >>> fig.savefig("{filename}-{func}-final.svg") # ignore
    """
    "hi"


def texture():
    """
    >>> import plenoptic as po
    >>> import torch # ignore
    >>> # for some reason, looks much better when done on cpu # ignore
    >>> torch.set_default_device("cpu") # ignore
    >>> # Load image into Pytorch tensor
    >>> img = po.load_images("/home/billbrod/Desktop/reptile_skin.png")
    >>> # Initialize model
    >>> model = po.simul.PortillaSimoncelli(img.shape[-2:])
    >>> # Initialize metamer object
    >>> met = po.synth.MetamerCTF(img, model,
    ...                           loss_function=po.tools.optim.l2_norm)
    >>> init_img = .2 * torch.rand_like(img) + img.mean()
    >>> met.setup(initial_image=init_img)
    >>> # Synthesize model metamer
    >>> met.synthesize(max_iter=500, store_progress=5,
    ...                ctf_iters_to_check=3,
    ...                change_scale_criterion=None)
    >>> included_plots = ["display_metamer", "plot_loss"] # ignore
    >>> fig, axes_idx = create_met_figure(met, included_plots) # ignore
    >>> fig.savefig("{filename}-{func}-init.svg") # ignore
    >>> po.synth.metamer.animate(met, framerate=5, included_plots=included_plots, #ignore
    ...                          fig=fig, axes_idx=axes_idx).save("{filename}-{func}.mp4", dpi=300) # ignore
    >>> fig.savefig("{filename}-{func}-final.svg") # ignore
    """
    "hi"


def optimizer():
    """
    >>> import plenoptic as po
    >>> import torch
    >>> # Load image into Pytorch tensor
    >>> img = po.data.einstein()
    >>> # Initialize model
    >>> model = po.simul.CenterSurround(kernel_size=(31, 31),
    ...                                 cache_filt=True,
    ...                                 pad_mode="circular")
    >>> # Detach gradients from model -- model parameters are fixed.
    >>> po.tools.remove_grad(model)
    >>> # Initialize metamer object
    >>> met = po.synth.Metamer(img, model)
    >>> met.setup(initial_image=po.data.curie(),
    ...           optimizer=torch.optim.SGD)
    >>> # Synthesize model metamer
    >>> met.synthesize(max_iter=100, store_progress=5)
    >>> fig, axes_idx = create_met_figure(met) # ignore
    >>> fig.savefig("{filename}-{func}-init.svg") # ignore
    >>> po.synth.metamer.animate(met, framerate=5, fig=fig, axes_idx=axes_idx).save("{filename}-{func}.mp4", dpi=300) # ignore
    >>> fig.savefig("{filename}-{func}-final.svg") # ignore
    """
    "hi"


def optimizer_kwargs():
    """
    >>> import plenoptic as po
    >>> # Load image into Pytorch tensor
    >>> img = po.data.einstein()
    >>> # Initialize model
    >>> model = po.simul.CenterSurround(kernel_size=(31, 31),
    ...                                 cache_filt=True,
    ...                                 pad_mode="circular")
    >>> # Detach gradients from model -- model parameters are fixed.
    >>> po.tools.remove_grad(model)
    >>> # Initialize metamer object
    >>> met = po.synth.Metamer(img, model)
    >>> met.setup(initial_image=po.data.curie(),
    ...           optimizer_kwargs=dict(lr=1e-3))
    >>> # Synthesize model metamer
    >>> met.synthesize(max_iter=100, store_progress=5)
    >>> fig, axes_idx = create_met_figure(met) # ignore
    >>> fig.savefig("{filename}-{func}-init.svg") # ignore
    >>> po.synth.metamer.animate(met, framerate=5, fig=fig, axes_idx=axes_idx).save("{filename}-{func}.mp4", dpi=300) # ignore
    >>> fig.savefig("{filename}-{func}-final.svg") # ignore
    """
    "hi"


def torchvision():
    """
    >>> import plenoptic as po
    >>> import torch
    >>> import torchvision
    >>> # Load image into Pytorch tensor
    >>> img = po.data.einstein(as_gray=False)
    >>> # Initialize model
    >>> weights = torchvision.models.ResNet50_Weights.IMAGENET1K_V1
    >>> model = torchvision.models.resnet50(weights=weights)
    >>> model = po.TorchVisionModel(model, "layer2", weights.transforms())
    >>> # Detach gradients from model -- model parameters are fixed.
    >>> po.tools.remove_grad(model)
    >>> model = model.eval()
    >>> # Initialize metamer object
    >>> met = po.synth.Metamer(img, model)
    >>> # Synthesize model metamer
    >>> met.synthesize(max_iter=400, store_progress=5)
    >>> met.to('cpu') # ignore
    >>> included_plots = ["display_metamer", "plot_loss"] # ignore
    >>> fig, axes_idx = create_met_figure(met, included_plots) # ignore
    >>> fig.savefig("{filename}-{func}-init.svg") # ignore
    >>> po.synth.metamer.animate(met, 5, included_plots=included_plots, #ignore
    ...                          fig=fig, axes_idx=axes_idx).save("{filename}-{func}.mp4", dpi=300) # ignore
    >>> fig.savefig("{filename}-{func}-final.svg") # ignore
    """
    "hi"


def torchvision_full():
    """
    >>> import plenoptic as po
    >>> import torch
    >>> from torchvision.models import feature_extraction as fe
    >>> import torchvision
    >>> # Load image into Pytorch tensor
    >>> img = po.data.einstein(as_gray=False)
    >>> # Initialize model
    >>> class TorchVisionModel(torch.nn.Module):
    ...     def __init__(self, model, return_node, transform):
    ...         super().__init__()
    ...         self.transform = transform
    ...         self.extractor = fe.create_feature_extractor(model,
    ...                                                      [return_node])
    ...         self.model = model
    ...         self.return_node = return_node
    ...     def forward(self, x):
    ...         if self.transform is not None:
    ...             x = self.transform(x)
    ...         return self.extractor(x)[self.return_node]
    >>> weights = torchvision.models.ResNet50_Weights.IMAGENET1K_V1
    >>> model = torchvision.models.resnet50(weights=weights)
    >>> model = TorchVisionModel(model, "layer2", weights.transforms())
    >>> # Detach gradients from model -- model parameters are fixed.
    >>> po.tools.remove_grad(model)
    >>> model = model.eval()
    >>> # Initialize metamer object
    >>> met = po.synth.Metamer(img, model)
    >>> # Synthesize model metamer
    >>> met.synthesize(max_iter=400, store_progress=5)
    >>> met.to('cpu') # ignore
    >>> included_plots = ["display_metamer", "plot_loss"] # ignore
    >>> fig, axes_idx = create_met_figure(met, included_plots) # ignore
    >>> fig.savefig("{filename}-{func}-init.svg") # ignore
    >>> po.synth.metamer.animate(met, 5, included_plots=included_plots, #ignore
    ...                          fig=fig, axes_idx=axes_idx).save("{filename}-{func}.mp4", dpi=300) # ignore
    >>> fig.savefig("{filename}-{func}-final.svg") # ignore
    """
    "hi"


def custom_model():
    """
    >>> import plenoptic as po
    >>> import torch
    >>> import torchvision
    >>> from plenoptic.simulate import circular_gaussian2d
    >>> # Load image into Pytorch tensor
    >>> img = po.data.einstein()
    >>> # Create a simple Gaussian convolutional model
    >>> class Gaussian(torch.nn.Module):
    ...     def __init__(self, kernel_size, std_dev=3):
    ...         super().__init__()
    ...         self.kernel_size = kernel_size
    ...         self.conv = torch.nn.Conv2d(1, 1,
    ...                                     kernel_size=kernel_size,
    ...                                     padding=(0, 0), bias=False)
    ...         gauss = circular_gaussian2d(kernel_size, std_dev)
    ...         self.conv.weight.data[0, 0] = gauss
    ...     def forward(self, x):
    ...         x = po.tools.conv.same_padding(x, self.kernel_size,
    ...                                        pad_mode='circular')
    ...         return self.conv(x)
    >>> model = Gaussian((31, 31))
    >>> # Detach gradients from model -- model parameters are fixed.
    >>> po.tools.remove_grad(model)
    >>> po.tools.validate.validate_model(model)
    >>> # Initialize metamer object
    >>> met = po.synth.Metamer(img, model)
    >>> # Synthesize model metamer
    >>> met.synthesize(max_iter=100, store_progress=5)
    >>> fig, axes_idx = create_met_figure(met) # ignore
    >>> fig.savefig("{filename}-{func}-init.svg") # ignore
    >>> po.synth.metamer.animate(met, 5, fig=fig, axes_idx=axes_idx).save("{filename}-{func}.mp4", dpi=300) # ignore
    >>> fig.savefig("{filename}-{func}-final.svg") # ignore
    """
    "hi"
