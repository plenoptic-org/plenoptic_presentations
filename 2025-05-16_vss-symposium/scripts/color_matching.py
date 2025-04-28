#!/usr/bin/env python3

from functools import partial
import numpy as np
from matplotlib import animation
import matplotlib.pyplot as plt


def initialize_color_matching_fig(to_match=(7, 175, 220), to_start=(128, 128, 128),
                                  save_path=None):
    fig, axes = plt.subplots(1, 2, figsize=(6, 3))
    fig.subplots_adjust(top=.75)
    to_match = np.asarray(to_match)
    to_start = np.asarray(to_start)
    if any(to_match > 1):
        to_match = to_match / 255
    if any(to_start > 1):
        to_start = to_start / 255
    colors = [to_match, to_start]
    circles = {}
    distance = .25
    # for ax in axes:
        # ax.add_patch(plt.Rectangle((-1.5, -1.5), 3, 3, color=(0, 0, 0)))
    circles["red"] = axes[1].add_patch(plt.Circle((-distance, distance),
                                                  1, color=(to_start[0], 0, 0)))
    circles["green"] = axes[1].add_patch(plt.Circle((distance, distance),
                                                    1, color=(0, to_start[1], 0)))
    circles["blue"] = axes[1].add_patch(plt.Circle((0, -np.sqrt(2)*distance),
                                                    1, color=(0, 0, to_start[2])))
    for ax, c in zip(axes, colors):
        circ = ax.add_patch(plt.Circle((0, 0), 1, color=c))
        ax.set(aspect="equal", xlim=(-1.5, 1.5), ylim=(-1.5, 1.5))
        ax.set_axis_off()
    def update_circle(val, slider):
        color = list(circ.get_facecolor())
        idx = {"red": 0, "green": 1, "blue": 2}[slider]
        color[idx] = val/255
        circ.set_color(color)
        default_color = [0, 0, 0]
        default_color[idx] = val/255
        circles[slider].set_color(default_color)
    sliders = {}
    for i, c in enumerate(["red", "green", "blue"]):
        ax = fig.add_axes([.5, .9 - i*.07, .4, .03])
        sliders[c] = plt.Slider(
            ax=ax,
            label=c.capitalize(),
            valmin=0,
            valmax=255,
            valinit=int(to_start[i]*255),
            orientation="horizontal",
            color=c,
            initcolor="none",
            valstep=np.arange(0, 256),
        )
        sliders[c].on_changed(partial(update_circle, slider=c))
    if save_path is not None:
        fig.savefig(save_path, dpi=300)
    return fig, sliders


def match_some_colors(to_match=(7, 175, 220), to_start=(128, 128, 128),
                      n_steps=10, save_path=None):
    save_path_png = save_path
    if save_path_png is not None:
        save_path_png = save_path.replace(".mp4", "-init.png")
    fig, sliders = initialize_color_matching_fig(to_match, to_start, save_path_png)
    progression = {c: np.linspace(to_start[i], to_match[i], n_steps).astype(int)
                   for i, c in enumerate(sliders)}
    def animate_video(t):
        if t < n_steps:
            sliders["red"].set_val(progression["red"][t])
        elif t < 2*n_steps:
            sliders["green"].set_val(progression["green"][t-n_steps])
        else:
            sliders["blue"].set_val(progression["blue"][t-2*n_steps])
    anim = animation.FuncAnimation(fig, frames=3*n_steps,
                                   func=animate_video)
    if save_path is not None:
        anim.save(save_path, dpi=300)
        fig.savefig(save_path.replace(".mp4", "-final.png"), dpi=300)
    return anim
