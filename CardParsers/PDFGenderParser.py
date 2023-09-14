#!/usr/bin/python3
#gets plurality and gender of pdf nouns
#use on pdf

from wiktionaryparser import WiktionaryParser
wiktParser = WiktionaryParser()
import argparse
import csv
import requests
import os

parser = argparse.ArgumentParser(prog='PDFGenderParser', description='gets plurality and gender of noun from PDF')
parser.add_argument('input', help='name of txt file to input from')
parser.add_argument('output', help='name of txt file to output to')
parser.add_argument('-v', '--verbose', action='store_true')
args = parser.parse_args()

input_file = args.input
output = args.output

newlines = []
splitarr = []

if __name__ == '__main__':
    with open(input_file, 'r') as file:
        csv_reader = csv.reader(file)
        for line in csv_reader:
            if line[0][0].isupper():
                try:
                    wordparsed = wiktParser.fetch(line[0], 'german')[0]['definitions'][0]['text'][0]
                    if wordparsed:
                        gender = wordparsed[wordparsed.find('\xa0')+1]
                        iterator = wordparsed[wordparsed.find('plural')+7]
                        plurality = ''
                        counter = 0
                        while iterator.isalpha():
                            iterator = wordparsed[wordparsed.find('plural')+ 7 + counter]
                            plurality = plurality + iterator
                            counter = counter + 1
                        #begin at 6 plus index of found substring plural, continue until nonchar
                        plurality = plurality[:-1]
                        newlines.append([line[0], gender, plurality])
                    else:
                        print(line)
                        continue
                except IndexError as e:
                    newlines.append([line[0], gender, "no plural"])
                    print(line)
                    continue
        file.close()
    with open(output, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Noun', 'Gender', 'Plurality'])
        for line in newlines:
            writer.writerow([line[0], line[1], line[2]])
        f.close()


