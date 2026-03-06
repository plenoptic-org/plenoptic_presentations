#!/usr/bin/env python3

import argparse
import time
import plenoptic as po
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import torch
plt.rcParams["text.usetex"] = True


def synth_texture(max_iter=100, store_progress=True,
                  device=None,
                  **synth_kwargs):
    if device is None:
        device = DEVICE
    img = po.data.reptile_skin().to(device).to(torch.float64)
    ps = po.simul.PortillaSimoncelli(img.shape[-2:])
    ps.to(device)
    im_init = torch.rand_like(img) * .2 + img.mean()
    loss = po.tools.optim.portilla_simoncelli_loss_factory(ps, img)
    met = po.synth.Metamer(img, ps, loss_function=loss)
    opt_kwargs = {
        "max_iter": 10,
        "max_eval": 10,
        "history_size": 100,
        "line_search_fn": "strong_wolfe",
        "lr": 1,
    }
    met.setup(optimizer=torch.optim.LBFGS, optimizer_kwargs=opt_kwargs)
    start = time.time()
    met.synthesize(max_iter=max_iter, store_progress=store_progress)
    stop = time.time()
    return met, stop - start


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
    n_frames = len(met.saved_metamer)
    # lot of frames towards the end, so speed through them
    saved_metamer = torch.cat([met.saved_metamer[:n_frames//6],
                               met.saved_metamer[n_frames//6::8]])
    fig = init_figure(saved_metamer[0], met.model, ymax + ymax/5)
    if save_path is not None:
        fig.savefig(save_path.replace(".mp4", "-init.svg"))

    def update_frame(i):
        artists = []
        artists.extend(
            po.tools.display.update_plot(fig.axes[0], data=saved_metamer[i],
                                         batch_idx=0)
        )
        artists.extend(
            po.tools.display.update_plot(fig.axes[2],
                                         data=met.model(saved_metamer[i]),
                                         batch_idx=0)
        )
        return artists

    anim = animation.FuncAnimation(fig, update_frame, frames=len(saved_metamer),
                                   blit=True, interval=1000/framerate)
    if save_path is not None:
        anim.save(save_path)
        fig.savefig(save_path.replace(".mp4", "-metamer.svg"))
    return len(saved_metamer)


parser = argparse.ArgumentParser(
    description=("Synth and time texture metamers")
)
parser.add_argument("save_path",
                    help=(".mp4 path to save animated video at (metamer)"))
parser.add_argument("device", help="one of {cpu, gpu, None}. If None, use gpu if available.",
                    default=None)
args = vars(parser.parse_args())
if args["device"] == "None":
    args["device"] = None
met, duration = synth_texture(device=args["device"])
# in case we want to change how we plot/animate after the fact
met.save(args["save_path"].replace(".mp4", ".pt"))
met.to("cpu")
n_frames = animate(met, save_path=args["save_path"])
txt_path = args["save_path"].replace('.mp4', '-time.txt')
with open(txt_path, 'w') as f:
    f.write(f"{n_frames}\n{duration // 60} minutes, {duration % 60} seconds")
