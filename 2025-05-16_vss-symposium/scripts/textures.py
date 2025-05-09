#!/usr/bin/env python3

import plenoptic as po
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import torch
plt.rcParams["text.usetex"] = True


def synth_texture(max_iter=500, store_progress=True,
                  change_scale_criterion=None,
                  ctf_iters_to_check=3,
                  **synth_kwargs):
    img = po.data.reptile_skin()
    ps = po.simul.PortillaSimoncelli(img.shape[-2:])
    im_init = torch.rand_like(img) * .2 + img.mean()
    met = po.synth.MetamerCTF(img, ps, loss_function=po.tools.optim.l2_norm)
    met.setup(im_init)
    met.synthesize(max_iter=max_iter, store_progress=store_progress,
                   change_scale_criterion=change_scale_criterion,
                   ctf_iters_to_check=ctf_iters_to_check)
    return met


def init_figure(image, model, ylim=None):
    fig, axes = plt.subplots(1, 3, figsize=(15, 3.5),
                             gridspec_kw={"width_ratios": [1, .5, 2]})
    po.imshow(po.to_numpy(image), ax=axes[0], vrange=(0, 1), title=None)
    for ax in axes:
        ax.set_axis_off()
    po.tools.clean_stem_plot(po.to_numpy(model(image).squeeze()), axes[2], ylim=False)
    if ylim is None:
        ylim = axes[2].get_ylim()
        ylim = max(abs(np.asarray(ylim)))
    ylim = (-ylim, ylim)
    axes[2].set(ylim=ylim, yscale="symlog")
    rect = axes[1].add_patch(plt.Rectangle((-.5, -.5), 1, 1, facecolor="white",
                                           edgecolor="black", lw=10))
    rx, ry = rect.get_xy()
    cx = rx + rect.get_width() / 2
    cy = ry + rect.get_height() / 2
    axes[1].annotate("", xytext=(-.5, .5), xy=(1.5, .5), zorder=0,
                     arrowprops={"arrowstyle": "->", "linewidth": 4},
                     xycoords=axes[1].transAxes)
    axes[1].annotate(r"$M$", (cx - .05, cy - .05), fontsize=80, ha="center", va="center")
    axes[1].set(xlim=(-.5, .5), ylim=(-.5, .5), aspect="equal")
    fig.tight_layout()
    return fig


def animate(met, framerate=10, save_path=None):
    ymax = po.to_numpy(met.model(met.image).abs().max())
    if save_path is not None:
        fig = init_figure(met.image, met.model, ymax + ymax/5)
        fig.savefig(save_path.replace(".mp4", "-image.svg"))
    fig = init_figure(met.saved_metamer[0], met.model, ymax + ymax/5)
    if save_path is not None:
        fig.savefig(save_path.replace(".mp4", "-init.svg"))

    def update_frame(i):
        artists = []
        artists.extend(
            po.tools.display.update_plot(fig.axes[0], data=met.saved_metamer[i],
                                         batch_idx=0)
        )
        artists.extend(
            po.tools.display.update_plot(fig.axes[2],
                                         data=met.model(met.saved_metamer[i]),
                                         batch_idx=0)
        )
        return artists

    anim = animation.FuncAnimation(fig, update_frame, frames=len(met.saved_metamer),
                                   blit=True, interval=1000/framerate)
    if save_path is not None:
        anim.save(save_path)
        fig.savefig(save_path.replace(".mp4", "-metamer.svg"))
