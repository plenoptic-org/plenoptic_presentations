#!/usr/bin/env python3

import plenoptic as po
import torch
import os
import pathlib
OUTPUT_DIR = pathlib.Path(os.environ["OUTPUT_DIR"])

def test():
    """
    >>> img = po.data.einstein()
    >>> img.shape
    torch.Size([1, 1, 256, 256])
    >>> fig = po.imshow(img)
    >>> fig.savefig(OUTPUT_DIR / "test.png") #ignore
    """
    'hi'


def test2():
    """
    >>> img = po.data.einstein()
    >>> img2 = po.data.curie()
    >>> anim = po.animshow(torch.stack([img, img2], dim=2))
    >>> anim.save(OUTPUT_DIR / "test.mp4") #ignore
    """
    'hi'
