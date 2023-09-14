#!/usr/bin/python3
import csv
import re
import argparse
import xml.etree.ElementTree as ET
import beta_code
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm

parser = argparse.ArgumentParser(
    prog="PerseusXMLParser",
    description="scrapes Perseus Digital Library generated XML and outputs a list of all words to a local txt file",
)
parser.add_argument("input", help="the URL of the generated page")
parser.add_argument("output", help="name of txt file to output to")
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()

input_file = args.input
output = args.output

tree = ET.parse(input_file)
root = tree.getroot()
counter = 0
baseURL = "https://en.wiktionary.org/wiki/"

with open(filename, "w") as f:
    writer = csv.writer(f)
    writer.writerow(
        [
            "Classical Word",
            "Weighted Frequency",
            "Definition",
            "Dictionary Link",
            "Principal Parts",
        ]
    )
    freq_elems = root.findall(".//frequency")
    total_words = len(freq_elems)
    progress_bar = tqdm(total=total_words, unit=" words")
    for frequency_element in freq_elems:
        principal_parts = ""
        lemma = frequency_element.find(".//lemma/headword").text
        unicode_lemma = beta_code.beta_code_to_greek(lemma)

        shortDef = frequency_element.find(".//lemma/shortDefinition").text
        weighted_frequency = frequency_element.find(".//weightedFrequency").text
        lexiconQueries = frequency_element.find(".//lexiconQueries")
        # get hrefs

        url = baseURL + unicode_lemma
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        principal_parts_arr = (
            parent_element.find_all("div div span strong").get_text().strip()
        )
        print(principal_parts_arr)
        if principal_parts_arr:
            principal_parts = ", ".join(principal_parts_arr)

        print(
            f"Classical Word: {clas_word}, Weighted Frequency: {weighted_freq}, Definition: {definition}, Dictionary Links: {dict_links}, Principal Parts: {principal_parts}"
        )
        writer.writerow(
            [clas_word, weighted_freq, definition, dict_links, principal_parts]
        )
        counter = counter + 1
        progress_bar.update(counter)
    print(f"{counter} words written to output")
    progress_bar.close()
    f.close()
