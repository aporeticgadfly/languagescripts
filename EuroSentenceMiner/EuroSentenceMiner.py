#!/usr/bin/python
import argparse
import csv

parser = argparse.ArgumentParser(prog='EuroSentenceMiner', description='mines sentence pairs from europarl corpus')
parser.add_argument('input1', help='name of txt file to input from (english)')
parser.add_argument('input2', help='name of txt file to input from (other)')
parser.add_argument('output', help='name of txt file to output to')
parser.add_argument('-v', '--verbose', action='store_true')
args = parser.parse_args()

english_corpus_path = args.input1
other_corpus_path = args.input2
output = args.output

def extract_sentence_pairs(english_corpus, other_corpus):
    with open(english_corpus, 'r', encoding='utf-8') as english_file:
        english_sentences = english_file.readlines()

    with open(other_corpus, 'r', encoding='utf-8') as other_file:
        other_sentences = other_file.readlines()

    # Ensure both lists have the same length
    min_length = min(len(english_sentences), len(other_sentences))
    english_sentences = english_sentences[:min_length]
    other_sentences = other_sentences[:min_length]

    # Pair English and French sentences
    sentence_pairs = [(english.strip(), other.strip()) for english, other in zip(english_sentences, other_sentences)]

    return sentence_pairs

with open(output, 'w') as f:
	writer = csv.writer(f)
	writer.writerow(["English Sentence", "Target Sentence"])
	sentence_pairs = extract_sentence_pairs(english_corpus_path, other_corpus_path)
	for pair in sentence_pairs:
		print(pair[0])
		print(pair[1])
		print('----------------------------------------------------------------------------------------------------------')
		writer.writerow([pair[0], pair[1]])
