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
parser.add_argument("input", help="the path of the generated XML page")
parser.add_argument("output", help="name of txt file to output to")
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()

verbose = args.verbose

def my_print(*args, **kwargs):
    if verbose:
        print(*args, **kwargs)

input_file = args.input
output = args.output

tree = ET.parse(input_file)
root = tree.getroot()
counter = 0
base_perseus_url = "https://www.perseus.tufts.edu/hopper/text?doc="
base_wiktionary_url = "https://en.wiktionary.org/wiki/"

def remove_attributes(tag):
    tag.attrs = {}

with open(output, "w") as f:
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

        short_def = frequency_element.find(".//lemma/shortDefinition").text
        weighted_frequency = frequency_element.find(".//weightedFrequency").text
        lexiconQueries = frequency_element.find(".//lexiconQueries")
        # get hrefs
        dict_links = ''
        for query in lexiconQueries:
            if query.get("name") == "LSJ":
                dict_links = base_perseus_url + query.get("ref")

        url = base_wiktionary_url + unicode_lemma
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        #check if verb, noun, or adj
        #if there is a span w id noun, must also get the gender 
        noun_gender = ''
        noun_el = soup.find(id="Noun")
        if noun_el:
            parent = noun_el.parent
            noun_gender = parent.find_next_sibling('p').get_text().strip()
            my_print('-' * 80)
            my_print(noun_gender)
            my_print('-' * 80)

        parts_divs = soup.find_all('div', class_='NavHead')
        principal_parts_arr = []
        for parts_div in parts_divs:
            #remove NavToggle
            principal_parts_arr.append(parts_div.get_text().strip())
        principal_parts = ", ".join(principal_parts_arr)
        principal_parts = principal_parts + noun_gender
        inflection_divs = soup.find_all('div', class_='NavContent')
        inflection_tables = []
        for inflection_div in inflection_divs:
            inflection_table = inflection_div.find('table')
            if inflection_table:
                for tag in inflection_table.recursiveChildGenerator():
                    remove_attributes(tag)
                tr_elements = inflection_table.find_all('tr')
                if len(tr_elements) > 0:
                    last_tr = tr_elements[-1]
                    last_tr.extract()
                cleaned_html = inflection_table.encode_contents().decode('utf-8')
                inflection_tables.append(inflection_table)

        my_print(
            f"Classical Word: {unicode_lemma}, Weighted Frequency: {weighted_frequency}, Definition: {short_def}, Dictionary Links: {dict_links}, Principal Parts: {principal_parts}"
        )
        writer.writerow(
            [unicode_lemma, weighted_frequency, short_def, dict_links, principal_parts, inflection_tables]
        )
        progress_bar.update(1)
    print(f"{counter} words written to output")
    progress_bar.close()
    f.close()
