# plenoptic_presentations

Presentations about the
[plenoptic](https://github.com/LabForComputationalVision/plenoptic/) software
package. These presentations are all [reveal.js](https://revealjs.com/)
presentations built from markdown files found in their respective folders, with
the website built using github pages.

This repo also includes some code used to generate figures.

## Build locally

To build this locally, [install Ruby](https://jekyllrb.com/docs/installation/),
then run `bundle exec jekyll serve` to build and serve the website locally. In
your browser, navigate to the address shown in the terminal (probably
`localhost:4000/plenoptic_presentations/`)

## Assets

The assets for these presentations (images, movies) are saved in [this OSF
project](https://osf.io/admxn/). The script `osf_files.py` is provided to ease
the upload and download of them as necessary. It requires python 3 with `click`
and `tqdm` installed (run `pip install click tqdm`).

### Package and upload

To package and upload, the [osfclient](https://github.com/osfclient/osfclient)
must also be installed. See that link for setup. The project name for the assets
is `admxn`.

Then, to package run `python osf_files.py package-assets
PRESENTATION_DIR/assets/` to create a tarball containing the contents of that
directory at the path `PRESENTATION_DIR/assets.tar.gz`. It's recommended you
examine the contents of this tarball (with `tar tvf
PRESENTATION_DIR/assets.tar.gz`) to make sure it contains what you expected.

To upload, run `python osf_files.py upload PRESENTATION_DIR/assets.tar.gz`.
Depending on how you configured the OSF client, it may ask for your password (or
give you permission denied if you do not have upload permissions to the projct).
(This will *not* delete the tarball afterwards.)

### Download

Anyone can download the assets and it does not require the `osfclient` being set
up.

To do so, run `python osf_files.py download PRESENTATION_DIR`, which will
download the tarball, extract its contents, and then delete it.

You may also run `python osf_files.py download all`, which will download and
extract all tarballs.

## Licensing

The code found in this repo is licensed the [MIT License](./LICENSE-CODE) while
all text and images found in the presentations, as well as the presentations
themselves are licensed under [CC-BY-SA 4.0](./LICENSE-TEXT) (see
[here](https://creativecommons.org/licenses/by-sa/4.0/) for human-readable
summary, but in essence, you are free to copy and reuse any components,
including the whole presentations, as long as you credit the original authors
and share your material under the same (or a compatible) license).
