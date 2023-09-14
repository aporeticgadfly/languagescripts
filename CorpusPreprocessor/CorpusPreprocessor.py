#!/usr/bin/python
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import spacy
import sys
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser(
    prog="PerseusParser",
    description="scrapes Perseus Digital Library generated wordlist and outputs a list of all words to a local txt file",
)
parser.add_argument("-l", "--language", required=True, help="the language to process")
parser.add_argument("input", required=True, help="name of corpus file")
parser.add_argument("output", required=True, help="name of corpus file")
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()

URL = args.url
input_text = args.input
output_text = args.output
filename = args.filename
language = args.language

final_tokens = []
final_sorted_tokens = []

if language == "german":
    spacyloader = "de_core_news_sm"
elif language == "french":
    spacyloader = "fr_core_news_sm"
elif language == "spanish":
    spacyloader = "es_core_news_sm"
nlp = spacy.load(spacyloader)


def count_words_in_corpus(corpus_file):
    with open(corpus_file, "r", encoding="utf-8") as file:
        text = file.read()
        words = word_tokenize(text)
        return len(words)


def preprocess_text(text):
    tokens = word_tokenize(text)
    lowercase_tokens = [token.lower() for token in tokens]
    cleaned_tokens = [token for token in lowercase_tokens if token.strip()]
    return cleaned_tokens


def lemmatize_tokens(tokens):
    processed_tokens = []

    for token in tokens:
        doc = nlp(token)
        lemmatized_token = doc[0].lemma_
        processed_tokens.append(lemmatized_token)
    return processed_tokens


def sort_by_frequency(lemmas):
    freq_dist = FreqDist(lemmas)
    sorted_tokens = sorted(freq_dist.items(), key=lambda x: x[1], reverse=True)
    return sorted_tokens


def process_large_corpus(input_text, chunk_size, total_words):
    with open(input_text, "r", encoding="utf-8") as file:
        remaining = ""
        words_processed = 0  # Initialize the count of processed words

        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break

            chunk = remaining + chunk
            lines = chunk.splitlines()
            if lines:
                remaining = lines[-1]
                lines = lines[:-1]

            for line in lines:
                cleaned_tokens = preprocess_text(line)
                words_processed += len(cleaned_tokens)
                progress_bar.update(len(cleaned_tokens))  # Update the progress bar
                lemmas = lemmatize_tokens(cleaned_tokens)
                final_tokens.extend(lemmas)

                del cleaned_tokens
                del lemmas

        print("final tokens")
        print(final_tokens)
        print("reached sorting")
        final_sorted_tokens = sort_by_frequency(final_tokens)
        print("final sorted tokens")
        print(final_sorted_tokens)
        file.close()
        return final_sorted_tokens


if __name__ == "__main__":
    chunk_size = 100000
    total_words = count_words_in_corpus(input_text)
    progress_bar = tqdm(total=total_words, unit=" words")
    final_sorted_tokens = process_large_corpus(input_text, chunk_size, total_words)
    progress_bar.close()

    with open(output_text, "w", encoding="utf-8") as file:
        token_list = [token for token, _ in final_sorted_tokens]
        print(token_list)
        file.write(",".join(token_list))

        file.flush()

    print("Output written to", output_text)
