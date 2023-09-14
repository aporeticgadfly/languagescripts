#!/usr/bin/python3
#replaces verbs with wikt entry
#replace open or cmdline arg
#use on pdf, maybe main

from wiktionaryparser import WiktionaryParser
parser = WiktionaryParser()
newlines = []
import argparse

parser = argparse.ArgumentParser(prog='WiktVerbParser', description='replaces verbs from a file with wiktionary entries for more accurate and detailed translation')
parser.add_argument('input', help='name of txt file to input from')
parser.add_argument('output', help='name of txt file to output to')
parser.add_argument('-l', '--language', help='language to query wiktionary in')
parser.add_argument('-v', '--verbose', action='store_true')
args = parser.parse_args()

input = args.input
output = args.output
language = args.language

if __name__ == '__main__':
    txtfile = open(input, "r")
    lines = txtfile.readLines()
    for line in lines:
        word = parser.fetch(line, language)[0]
        audio = word[pronunciations][audio]
        definitions = word[definitions][0][text]
        examples = word[definitions][0][examples]
        iterator = word[word.find(','+1)]
        stammformen = ''
        counter = 0
        while iterator != ')':
            iterator = word[word.find(','+1) + counter]
            stammformen.append(iterator)
            counter = counter + 1
        newlines.append([line, audio, definitions, examples, stammformen])

    with open(output, 'w') as f:
        for index, lines in enumerate(newlines):
            f.write("[sound: GermanVerbs" + index + ".wav]") #
            f.write(',')
            f.write(line[1])
            f.write(',')
            f.write(line[2])
            f.write(',')
            f.write(line[3])
            f.write(',')
            f.write(line[4])
            f.write("\n")
    f.close()

    for line, index in newlines, range(newlines):
        with open('GermanVerbs'+index+'.wav', 'rb+'):
            f.write(line[0])

    txtfile.close()
