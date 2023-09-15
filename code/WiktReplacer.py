#!/usr/bin/python3
# replaces words w input w wiktionary entries to provide a more detailed and accurate definition
# this one ONLY does a series of comma separated values, assuming no new lines!!!
# TODO: add HTML insertion between separate word definitions
from wiktionaryparser import WiktionaryParser

wiktParser = WiktionaryParser()
import argparse
import csv
import requests
import os

parser = argparse.ArgumentParser(
    prog="WiktReplacer",
    description="replaces words w input w wiktionary entries to provide a more detailed and accurate definition",
)
parser.add_argument("input", help="name of txt file to input from")
parser.add_argument("output", help="name of txt file to output to")
parser.add_argument("-l", "--language", help="language")
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()

input_file = args.input
output = args.output
language = args.language

titles = []
audio2 = []
audio = []
definitions = []
examples = []
temp_ex = []
temp_def = []
counter = 0

if __name__ == "__main__":
    with open(input_file, "r") as file:
        content = file.read()

        words = content.split(",")

    with open(output, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Definition"])

        for word in words:
            try:
                wordparsed = wiktParser.fetch(word, language)[0]
                if wordparsed and len(wordparsed["definitions"]) != 0:
                    for text in wordparsed["definitions"][0]["text"]:
                        temp_def.append(text)
                    temp_def_string = "; ".join(map(str, temp_def))
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print(word)
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    writer.writerow([word, temp_def_string])
                    counter = counter + 1
                    temp_def = []
                    temp_def_string = ""
                else:
                    print("------------------------------------------------------")
                    print(word)
                    print("else")
                    print("------------------------------------------------------")

            except Exception as e:
                print("------------------------------------------------------")
                print(e)
                print(word)
                print("------------------------------------------------------")
                continue

    f.close()
    print(f"{counter} words written to output")
