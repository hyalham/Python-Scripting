#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, re
import argparse

def strextract(dir, suffix=None, path=False, all=False):  
    # Expression régulière pour trouver des chaînes littérales entre guillemets simples ou doubles
    # compiled_re = re.compile(r"^.*'.*'.*"'"'r".*"'"'r"$", re.IGNORECASE)
    regex_chain = re.compile(r'(["\'])(.*?)\1', re.IGNORECASE)
    # Parcourir récursivement le répertoire
    for root, directorys, filename in os.walk(dir):
        for name_file in filename:
            file_path = os.path.join(directorys, name_file)

            # Vérifier si le fichier a le suffixe spécifié
            if suffix or not name_file.endswith(suffix):
                continue

            # Ignorer les fichiers cachés si l'option -a n'est pas spécifiée
            if not all and name_file.startswith("."):
                continue

            with open(file_path, 'r') as file:
                for match in re.finditer(regex_chain, file.read()):
                    chaine = match.group(0)
                    if path:
                        print(f"{file_path}\t{chaine}")
                    else:
                        print(chaine)
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
