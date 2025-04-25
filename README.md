# plenoptic_presentations

Presentations about the
[plenoptic](https://github.com/plenoptic-org/plenoptic/) software
package. These presentations are all [reveal.js](https://revealjs.com/)
presentations built from markdown files found in their respective folders, with
the website built using github pages.

This repo also includes some code used to generate figures.

See [notes](./notes.md) for notes on how to improve presentations.

## Build locally

This repository uses `jekyll` to build `reveal.js` presentations from markdown
files and svg images. You will need to install `jekyll` locally (see below), and
`reveal.js` just needs to be present where expected. To do so, you can clone
this repository with `git clone --recurse-submodules
git@github.com:plenoptic-org/plenoptic_presentations.git`. If you've
already cloned this repository, run `git submodule init; git submodule update`
to check out the proper version.

For `jekyll`, [install Ruby](https://jekyllrb.com/docs/installation/), then run
`bundle install` from this directory to install `jekyll` and all necessary
components (if you get an error when doing this, run `gem install bundler`
first), then run `bundle exec jekyll serve` to build and serve the website
locally. In your browser, navigate to the address shown in the terminal
(probably `localhost:4000/`)

## Render code

This repo includes a script, `scripts/render_code.py`, which can be used to make
writing code in the markdown files easier. For all of this, see
`2025-05-16_vss-symposium/` for an example.

- It is run during every github pages build.
- To activate for a given presentation, include `render.md` in the `markdown`
  value of your yml frontmatter in `slides.html`, e.g., `markdown:
  slides-render.md` . 
- The script does three things in the following order:
  - Allows the insertion of code from other files. Any code block formatted like:
    ````
    ```python doctest:path/to/file.py:function
    ```
    ````

    will have its contents replaced with the docstring of the function named
    `function` in `path/to/file.py` (note that the code block has to be empty!).
    This is expected to be formatted like a standard python
    [doctest](https://docs.python.org/3/library/doctest.html), and the expected
    use is to run these scripts from the commandline (`python -m doctest
    path/to/file.py`), and using `render_code.py` to insert the source. You must
    manually insert any outputs. Any lines that have `ignore` in them will be
    excluded from the output.
  - Markdown code blocks will be converted to html, preserving any attributes.
    That is:
    ````
    ```python data-line-numbers
    import plenoptic
    ```
    ````
    Will get converted to:
    ```
    <pre><code class="language-python" data-line-numbers data-trim>
    import plenoptic
    </code></pre>
    ```
    Note that we always add `data-trim`.
  - Any code blocks that have a line before them formatted like `{: (.*)}` will
    be wrapped in a div containing the contents of the curly braces. This is
    apply additional classes or styling.
    
## Assets

The assets for these presentations (images, movies) are saved in [this OSF
project](https://osf.io/admxn/). The script `scripts/osf_files.py` is provided to ease
the upload and download of them as necessary. It requires python 3 with `click`
and `tqdm` installed (run `pip install click tqdm`).

### Package and upload

To package and upload, the [osfclient](https://github.com/osfclient/osfclient)
must also be installed. See that link for setup. The project name for the assets
is `admxn`.

Then, to package run `python scripts/osf_files.py package-assets
PRESENTATION_DIR/assets/` to create a tarball containing the contents of that
directory at the path `PRESENTATION_DIR/assets.tar.gz`. It's recommended you
examine the contents of this tarball (with `tar tvf
PRESENTATION_DIR/assets.tar.gz`) to make sure it contains what you expected.

To upload, run `python scripts/osf_files.py upload PRESENTATION_DIR/assets.tar.gz`.
Depending on how you configured the OSF client, it may ask for your password (or
give you permission denied if you do not have upload permissions for the
project). (This will *not* delete the tarball afterwards.)

### Download

Anyone can download the assets and it does not require the `osfclient` being set
up.

To do so, run `python scripts/osf_files.py download PRESENTATION_DIR`, which will
download the tarball, extract its contents, and then delete it. If you have a
local `assets/` directory with the same name as those you're downloading and a
more recent modification date, the script will ask if you'd like to extract the
contents (potentially overwriting local changes). If you choose not to, the
tarball will be left locally for you to examine.

You may also run `python scripts/osf_files.py download all`, which will download and
extract all tarballs.

## Licensing

The code found in this repo is licensed the [MIT License](./LICENSE-CODE) while
all text and images found in the presentations, as well as the presentations
themselves are licensed under [CC-BY-SA 4.0](./LICENSE-TEXT) (see
[here](https://creativecommons.org/licenses/by-sa/4.0/) for human-readable
summary, but in essence, you are free to copy and reuse any components,
including the whole presentations, as long as you credit the original authors
and share your material under the same (or a compatible) license).
