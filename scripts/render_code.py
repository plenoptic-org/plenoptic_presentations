#!/usr/bin/env python3

import ast
import re
import sys
import pathlib
from collections import OrderedDict


ALL_DOCSTRINGS = OrderedDict()

def parse_docstring(docstring, respect_ignore=True):
    docstring = docstring.splitlines()
    if respect_ignore:
        docstring = [d.strip() for d in docstring if "ignore" not in d]
    else:
        docstring = [d.strip() for d in docstring]
    docstring = [d for d in docstring if "..." not in d]
    docstring = [d.split("#doctest")[0] for d in docstring]
    return "\n".join(docstring).strip()


def get_file_docstrings(tree_body, respect_ignore=True):
    docstrings = OrderedDict()
    for node in tree_body:
        try:
            doc = ast.get_docstring(node)
        except TypeError:
            doc = None
        if doc is not None:
            docstrings[node.name] = parse_docstring(doc, respect_ignore)
    return docstrings

def get_docstring(file, function):
    if file not in ALL_DOCSTRINGS:
        with open(file) as f:
            tree = ast.parse(f.read())
        ALL_DOCSTRINGS[file] = get_file_docstrings(tree.body)
    return ALL_DOCSTRINGS[file][function]


paths = []
for p in sys.argv[1:]:
    p = pathlib.Path(p)
    if p.is_dir():
        raise ValueError("must be passed individual markdown files!")
    elif p.suffix == ".md":
        p = [p]
    else:
        p = []
    paths.extend(p)


for p in paths:
    with open(p) as f:
        contents = f.read()
    # skip those files whose slides.html do not have "render.md" in markdown field
    with open(p.parent / "slides.html") as f:
        slides_html = f.read()
    if not re.findall("markdown:.*render.md", slides_html):
        continue
    # insert the python code where needed
    matches = set(re.findall(r"```python.*? doctest:(.*?\.py):(\w*)", contents))
    for match_f, match_func in matches:
        doc = get_docstring(p.parent / match_f, match_func)
        contents = re.sub(rf"```(python.*? )doctest:{match_f}:{match_func}( |$)(.*)\n```",
                          rf"```\1\3\n{doc}\n```", contents, flags=re.MULTILINE)
    # convert md code blocks to html, preserving attributes
    contents = re.sub(r'```python +([a-z "=,0-9-]*?)(data-id=.[a-z0-9-]+.)([a-z "=,0-9-]*)$\n(.*?)```',
                      r'<pre \2><code class="language-python" data-trim \1 \3>\n\4</code></pre>',
                      contents,
                      flags=re.MULTILINE | re.DOTALL)
    # wrap these code blocks in a div with extra html, if specified.
    contents = re.sub(r"{: (.*?)}\n(<pre>.*?</pre>)", r"<div \1>\n\2</div>",
                      contents,
                      flags=re.MULTILINE | re.DOTALL)
    with open(str(p).replace(".md", "-render.md"), "w") as f:
        f.write(contents)


# update regex for doctest:file:func
# language should go in as class="language-{}"
# everything else should be added as attribute in code
