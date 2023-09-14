#!/usr/bin/python3

import argparse
import csv
import requests
import os

parser = argparse.ArgumentParser(prog='SentenceWordMatcher', description='given a list of comma separated words and a list of comma separated english-target sentence pairs, finds first sentence pair containing each word and outputs to a csv file')
parser.add_argument('input', help='name of sentence file to input from')
parser.add_argument('input2', help='name of word file to input from')
parser.add_argument('output', help='name of txt file to output to')
parser.add_argument('-v', '--verbose', action='store_true')
args = parser.parse_args()

input_file = args.input
input_file2 = args.input2
output = args.output

counter = 0

if __name__ == '__main__':
	with open(input_file, 'r') as file:
		with open(input_file2, 'r') as file2:
			with open(output, 'w') as f:
				writer = csv.writer(f)
				writer.writerow(['Headword', 'English Sentence', 'Target Sentence'])
				csv_reader2 = csv.reader(file2)
				csv_reader = csv.reader(file)
				wordlist = []
				sentencelist = []

				for word in csv_reader2:
					wordlist.append(word)

				for sentence in csv_reader:
					sentencelist.append(sentence)

				for word in wordlist:
					found_flag = False
					for sentence in sentencelist:
						if word[0] in sentence[1]:
							found_flag = True
							print("-------------------------")
							print(word[0])
							print(sentence[1])
							print("-------------------------")
							writer.writerow([word[0], sentence[0], sentence[1]])
							break
					if found_flag == False:
						print(f"no sentence found containing {word[0]}")
					else:
						counter = counter + 1
				print(f"Sentence-Word Pairs Found: {counter}")  
				f.close()
			file2.close()
		file.close()