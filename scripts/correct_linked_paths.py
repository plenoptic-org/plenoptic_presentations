#!/usr/bin/env python3

import re
import sys
import pathlib


paths = []
for p in sys.argv[1:]:
    p = pathlib.Path(p)
    if p.is_dir():
        p = list(p.glob("**/assets/*.svg"))
    elif p.suffix == ".svg":
        p = [p]
    paths.extend(p)


for p in paths:
    with open(p) as f:
        svg = f.read()
    # find all xlink:href= lines that end with .svg don't have assets/ in them, then add
    # assets/ to them.
    svg = re.sub(r"(xlink:href=[\"'])(?!:assets/)([a-z-_]+\.(svg|jpg|jpeg|png)['\"])$",
                 r"\1assets/\2", svg, flags=re.M)
    with open(p, "w") as f:
        f.write(svg)
