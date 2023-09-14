#!/usr/bin/python
import nltk
from nltk.tokenize import word_tokenize
import spacy
import sys
language = sys.argv[3]

if language == 'german':
    spacyloader = "de_core_news_sm"
elif language == 'french':
    spacyloader = "fr_core_news_sm"
elif language == 'spanish':
    spacyloader = "es_core_news_sm"

nlp = spacy.load(spacyloader)

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

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python preprocess_with_nltk.py <input_text> <output_text> <language>")
        sys.exit(1)
   
    input_text = sys.argv[1]
    with open(input_text, 'r', encoding='utf-8') as file:
        text = file.read()
        tokens = preprocess_text(text)
        lemmas = lemmatize_tokens(tokens)

    output_text = sys.argv[2]
    with open(output_text, 'w', encoding='utf-8') as file:
        token_list = [lemma for lemma in lemmas]
        print(token_list)
        file.write(",".join(token_list))

        file.flush()
    
    print("Output written to", output_text)
