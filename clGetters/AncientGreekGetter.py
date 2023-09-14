#!/usr/bin/python3
from cltk.data.fetch import FetchCorpus
from collections import Counter
import os
from lxml import etree
from cltk import NLP
from cltk.alphabet.grc.beta_to_unicode import BetaCodeReplacer

beta_code_replace = BetaCodeReplacer()
cltk_nlp = NLP(language="grc")

import argparse

parser = argparse.ArgumentParser(prog='AncientGreekGetter', description='uses CLTK to output a list of words in ancient language corpora ordered by frequency')
parser.add_argument('-n', '--num-words', help='number of words to output')
parser.add_argument('output', help='name of txt file to output to')
parser.add_argument('freqoutput', help='name of txt file to output frequency dist to')
parser.add_argument('-c', '--corpus', help='name of directory of corpus')
parser.add_argument('-v', '--verbose', action='store_true')
args = parser.parse_args()

num_words = int(args.num_words)
output = args.output
freqoutput = args.freqoutput
corpus = args.corpus

root_folder = "~/cltk_data/grc/text/" + corpus
expanded_root_folder = os.path.expanduser(root_folder)


# List to store concatenated XML content
concatenated_xml = []
# Traverse through the directory tree
for root, dirs, files in os.walk(expanded_root_folder):
    for file in files:
        if file.endswith("gk.xml"):  # Consider only XML files
            file_path = os.path.join(root, file)
            parser = etree.XMLParser(resolve_entities=False)  # Disable entity resolution
            tree = etree.parse(file_path, parser)
            rootxml = tree.getroot()
            for p_tag in rootxml.iter("p"):
                if p_tag.text != None:
                    stripped_p_tag = p_tag.text.strip()
                    converted_p = beta_code_replace.replace_beta_code(stripped_p_tag)
                    if len(converted_p) != 0:
                        modified_text = converted_p.replace('|', '')
                        cltk_doc = cltk_nlp.analyze(text=modified_text)
                        print(modified_text)
                        print(cltk_doc)
                        concatenated_xml.extend(cltk_doc.lemmata)

# Combine all XML content into a single string

# Now you can process the final_xml content as needed
print(concatenated_xml)
word_frequency = Counter(concatenated_xml)
most_common_words = word_frequency.most_common(num_words)
print(most_common_words)
print(len(most_common_words))
print(len(concatenated_xml))

with open(output, "w") as file:
    for value in most_common_words:
        file.write(str(value[0]) + ",")
    
    file.seek(file.tell() - 1)
    
    file.write("\n")

with open(freqoutput, "w", encoding="utf-8") as f:
    for word, frequency in word_frequency.items():
        f.write(f"{word}: {frequency}\n")

print("written")
