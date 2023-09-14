#!/usr/bin/python3
from wiktionaryparser import WiktionaryParser
wiktParser = WiktionaryParser()
import argparse
import csv
import requests
import os

parser = argparse.ArgumentParser(prog='SentenceMiner', description='given a word, will mine its example sentences from wiktionary')
parser.add_argument('input', help='name of txt file to input from')
parser.add_argument('output', help='name of txt file to output to')
parser.add_argument('-l', '--language', help='language')
parser.add_argument('-v', '--verbose', action='store_true')
args = parser.parse_args()

input_file = args.input
output = args.output
language = args.language

colval = 2
    
if __name__ == '__main__':
    with open(input_file, 'r') as file:
    	with open(output, 'w') as f:
            content = file.read()
            words = content.split(',')
            writer = csv.writer(f)
            writer.writerow(["English Sentence", "Target Sentence"])
            for row in words:
                english_ex = []
                german_ex = []
                try:
                    wordparsed = wiktParser.fetch(row, language)[0]
                except Exception as e:
                    print(e)
                    print(row)
                    continue
                if wordparsed:
                    for definition in wordparsed['definitions']:
                        for example in definition['examples']: 
                            try:
                                split_ex = example.split('―')
                                if (len(split_ex) == 1) :
                                    split_ex = example.split('.')
                                english_ex.append(split_ex[0])
                                german_ex.append(split_ex[1])
                            except Exception as e:
                                print(e)
                                print(example)
                                continue
                    temp_eng_string  = '; '.join(map(str, english_ex))
                    temp_ger_string  = '; '.join(map(str, german_ex))
                    writer.writerow([temp_eng_string, temp_ger_string])
                else:
                    print("culprit word:", row)