#!/usr/bin/env python3

import plenoptic as po


def synth_lgn(max_iter=3500, store_progress=5,
              stop_criterion=1e-11,
              lr=.007, **synth_kwargs):
    img = po.data.einstein()
    lg = po.simul.LuminanceGainControl((31, 31), pad_mode="circular",
                                       pretrained=True, cache_filt=True)
    po.tools.remove_grad(lg)
    lg.eval()
    met = po.synth.Metamer(img, lg)
    met.setup(optimizer_kwargs={"lr": lr, "amsgrad": True})
    met.synthesize(max_iter=max_iter, store_progress=store_progress,
                   stop_criterion=stop_criterion, **synth_kwargs)
    return met
