#!/usr/bin/python3
from wiktionaryparser import WiktionaryParser
wiktParser = WiktionaryParser()
import argparse
import csv
import requests
import os

parser = argparse.ArgumentParser(prog='PDFMainParser', description='replaces words w input w wiktionary entries to provide a more detailed and accurate definition')
parser.add_argument('input', help='name of txt file to input from')
parser.add_argument('output', help='name of txt file to output to')
parser.add_argument('-l', '--language', help='language')
parser.add_argument('-f', '--flag', help='pdf/0 or main/1 as input')
parser.add_argument('-v', '--verbose', action='store_true')
args = parser.parse_args()

input_file = args.input
output = args.output
language = args.language
flag = int(args.flag)

colval = 0

titles = []
definitions = []
examples = []
temp_ex = []
temp_def = []
    
if __name__ == '__main__':
    with open(input_file, 'r') as file:
    	with open(output, 'w') as f:
            csv_reader = csv.reader(file)
            writer = csv.writer(f)
            writer.writerow(['Word', 'Definitions'])
            if flag == 0:
                for row in csv_reader:
                    row = row[0].split("-")[0].strip()
                    try:
                        wordparsed = wiktParser.fetch(row, language)[0]
                        if wordparsed and len(wordparsed['definitions']) != 0:
                            for text in wordparsed['definitions'][0]['text']:
                                temp_def.append(text)
                            temp_def_string  = '; '.join(map(str, temp_def))
                            writer.writerow([row, temp_def_string])
                            temp_def = []
                            temp_def_string = ''
                        else:
                            print(row)
                    except Exception as e:
                        print(e)
                        print(row)
                        continue
            else:
                for row in csv_reader:
                    row = row[0].split('\t')[0]
                    checked_row = row.split(' ')
                    if len(checked_row) != 1:
                        row = checked_row[1]
                   
                    try:
                        wordparsed = wiktParser.fetch(row, language)[0]
                        if wordparsed and len(wordparsed['definitions']) != 0:
                            for text in wordparsed['definitions'][0]['text']:
                                temp_def.append(text)
                            temp_def_string = '; '.join(map(str, temp_def))
                            writer.writerow([row, temp_def_string])
                            temp_def = []
                            temp_def_string = ''
                        else:
                            print(row)
                            continue
                    except Exception as e:
                        print(e)
                        print(row)
                        continue
