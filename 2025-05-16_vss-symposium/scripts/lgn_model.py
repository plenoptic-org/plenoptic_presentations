#!/usr/bin/env python3

import argparse
import time
import plenoptic as po
import matplotlib.pyplot as plt
from matplotlib import animation
import torch
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
plt.rcParams["text.usetex"] = True


def metamer(max_iter=3500, store_progress=10,
            stop_criterion=1e-11,
            im_init = None,
            lr=.007, device=None, **synth_kwargs):
    if device is None:
        device = DEVICE
    img = po.data.einstein().to(device)
    lg = po.simul.LuminanceGainControl((31, 31), pad_mode="circular",
                                       pretrained=True, cache_filt=True)
    po.tools.remove_grad(lg)
    lg = lg.to(device)
    lg.eval()
    met = po.synth.Metamer(img, lg)
    if im_init is None:
        im_init = torch.rand_like(img)
        im_init = (2 * im_init - .5).clip(0, 1)
    met.setup(im_init, optimizer_kwargs={"lr": lr, "amsgrad": True})
    start = time.time()
    met.synthesize(max_iter=max_iter, store_progress=store_progress,
                   stop_criterion=stop_criterion, **synth_kwargs)
    stop = time.time()
    return met, stop - start


def init_figure(image, model, rep_vrange="indep1"):
    fig, axes = plt.subplots(1, 3, figsize=(11, 3.5),
                             gridspec_kw={"width_ratios": [1, .5, 1]})
    po.imshow(po.to_numpy(image), ax=axes[0], vrange=(0, 1), title=None)
    for ax in axes:
        ax.set_axis_off()
    po.imshow(model(image), ax=axes[2], title=None, vrange=rep_vrange)
    rect = axes[1].add_patch(plt.Rectangle((-.5, -.5), 1, 1, facecolor="white",
                                           edgecolor="black", lw=10))
    rx, ry = rect.get_xy()
    cx = rx + rect.get_width() / 2
    cy = ry + rect.get_height() / 2
    axes[1].annotate("", xytext=(-.5, .5), xy=(1.5, .5), zorder=0,
                     xycoords=axes[1].transAxes,
                     arrowprops={"arrowstyle": "->", "linewidth": 4})
    axes[1].annotate(r"$M$", (cx - .05, cy - .05), fontsize=80, ha="center", va="center")
    axes[1].set(xlim=(-.5, .5), ylim=(-.5, .5), aspect="equal")
    fig.tight_layout()
    return fig


def animate(met, framerate=10, save_path=None):
    all_imgs = torch.cat([met.image, met.saved_metamer[0], met.metamer], 0)
    rep_vrange = (met.model(all_imgs).min().item(), met.model(all_imgs).max().item())
    if save_path is not None:
        fig = init_figure(met.image, met.model, rep_vrange)
        fig.savefig(save_path.replace(".mp4", "-image.svg"))
    fig = init_figure(met.saved_metamer[0], met.model, rep_vrange)
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


parser = argparse.ArgumentParser(
    description=("Synth and time LGN metamers, eigendistortions")
)
parser.add_argument("synth_method", help="one of {metamer, eigendistortion}")
parser.add_argument("save_path", help=".mp4 path to save animated video at")
parser.add_argument("device", help="one of {cpu, gpu, None}. If None, use gpu if available.",
                    default=None)
args = vars(parser.parse_args())
if args["device"] == "None":
    args["device"] = None
met, duration = metamer(device=args["device"])
met.to("cpu")
with open(args["save_path"].replace('.mp4', '-time.txt'), 'w') as f:
    f.write(f"{duration // 60} minutes, {duration % 60} seconds")
animate(met, save_path=args["save_path"])
