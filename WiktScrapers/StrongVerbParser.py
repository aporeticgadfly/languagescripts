#!/usr/bin/python3

from wiktionaryparser import WiktionaryParser
import csv
wiktparser = WiktionaryParser()
newlines = []
import argparse

parser = argparse.ArgumentParser(prog='StrongVerbParser', description='gets stammformen of strong verbs')
parser.add_argument('input', help='name of txt file to input from')
parser.add_argument('output', help='name of txt file to output to')
parser.add_argument('-l', '--language', help='language to query wiktionary in')
parser.add_argument('-i', '--input-method', help='0 for comma delimited, 1 for newline delimited')
parser.add_argument('-v', '--verbose', action='store_true')
args = parser.parse_args()

input_file = args.input
output = args.output
language = args.language
input_method = int(args.input_method)
words = []

if __name__ == '__main__':
    with open(input_file, 'r') as file:
        if input_method == 0:
            content = file.read()
            words = content.split(',')
        elif input_method == 1:
            words = file.read().splitlines()
        print(words)
        for line in words:
            try:
                word = wiktparser.fetch(line, language)[0]["definitions"][0]["text"][0]
                if word:
                    iterator = word[word.find('(')+1]
                    stammformen = ''
                    counter = 0
                    while iterator != ')':
                        try:
                            iterator = word[word.find('(') + 1 + counter]
                            stammformen = stammformen + iterator
                            counter += 1
                        except Exception as e:
                            break
                    newlines.append([line, stammformen])
                else:
                    print('culprit word: ' + line)
            except Exception as e:
                print('culprit word: ' + line)
                continue
        

        with open(output, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["Strong Verb", "Stammformen"])
            for lines in newlines:
                print(lines)
                writer.writerow([lines[0], lines[1]])
        f.close()

        file.close()
