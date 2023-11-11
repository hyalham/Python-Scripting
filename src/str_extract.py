#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, re
import argparse

def strextract(dir, suffix, path, all):  
    list_expressions =[]
    compiled_re = re.compile(r"^.*'.*'.*"'"'r".*"'"'r"$", re.IGNORECASE)
    for root, dirs, filename_list in os.walk(dir):
        for filename in filename_list:
            chemin_fichier = os.path.join(dirs, filename)
            if suffix and not filename.endswith(suffix):
                continue
            if not all and filename.startswith("."):
                continue
            with open(filename, 'r') as file:
                content = file.readlines()
                pattern = re.findall(compiled_re, content)
                list_expressions(pattern)
    print(list_expressions)


def main():
    # build an empty parser
    parser = argparse.ArgumentParser(description='Return path')

    # define arguments
    parser.add_argument("dir", type=str, help="Directory path")
    parser.add_argument("-s", "--suffix", type=str, help="Optional definition of a suffixe <.suf>")
    parser.add_argument("--path", action = 'store_true')
    parser.add_argument("-a", "--all", action = 'store_true')

    # instruct parser to parse command line arguments
    args = parser.parse_args()
    strextract(args.dir, args.suffix, args.path, args.all)

if __name__ == '__main__':
    main()
