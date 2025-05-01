#!/usr/bin/env python3

import ast
import os
import sys
import doctest
import importlib
import argparse
import render_code

dt_parser = doctest.DocTestParser()
dt_runner = doctest.DocTestRunner()

def parse_functions_args(functions_str, function_names):
    functions_str = functions_str.split(",")
    functions_out = []
    for s in functions_str:
        s = s.split("-")
        if len(s) == 1:
            s = s[0]
            try:
                functions_out.append(function_names[int(s)])
            except ValueError:
                functions_out.append(s)
        else:
            if s[0] == "":
                n = range(int(s[1])+1)
            elif s[-1] == "":
                n = range(int(s[0]), len(function_names))
            else:
                n = range(int(s[0]), int(s[1])+1)
            functions_out.extend([function_names[i] for i in n])
    return functions_out


parser = argparse.ArgumentParser(
    description=("Run some doctests. Will replace all instances of `{filename}` with the name of."
                 " the file and `{func}` with the name of the function.")
)
parser.add_argument("file", help=".py file whose docstrings we'll run as doctests.")
parser.add_argument("functions", nargs="?",
                    help=("functions to run from within FILE. Should be either comma-separated"
                          " names of functions or ints which give index into file. Ints can be"
                          " formatted as `0,3-5` where `x-y` is parsed as range(x,y+1); if `x` is"
                          " missing, replaced with 0, if `y` is missing, replaced with end. "
                          "If unset, run all functions."))
args = vars(parser.parse_args())
module_name = args["file"].replace('.py', '').replace('/', '.')
sys.path.append(os.getcwd())
module = importlib.import_module(module_name)

with open(args["file"]) as f:
    tree = ast.parse(f.read())
docstrings = render_code.get_file_docstrings(tree.body, False)
functions = parse_functions_args(args["functions"], list(docstrings.keys()))
for func in functions:
    docstr = docstrings[func].format(filename=args["file"].replace(".py", ""), func=func)
    doctests = dt_parser.get_doctest(docstr, module.__dict__, func, None, None)
    dt_runner.run(doctests)
