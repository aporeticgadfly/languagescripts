#!/usr/bin/python3
import requests
import time
import csv
import re
from bs4 import BeautifulSoup
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser(
    prog="PerseusParser",
    description="scrapes Perseus Digital Library generated wordlist and outputs a list of all words to a local txt file",
)
parser.add_argument("-u", "--url", required=True, help="the URL of the generated page")
parser.add_argument("filename", help="name of txt file to output to")
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()

URL = args.url
baseURL = "https://www.perseus.tufts.edu/hopper/"
filename = args.filename

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

parent_element = soup.find_all(id="vocab_list")[0]
rows = parent_element.find_all("tr")
rows = rows[9811 + 7370 :]

total_words = len(rows)
progress_bar = tqdm(total=total_words, unit=" words")

counter = 0

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
    for row in rows:
        columns = row.find_all("td")
        if len(columns) >= 9:
            clas_word = columns[1].find("a").get_text().strip()
            weighted_freq = columns[4].get_text().strip()
            definition = columns[7].get_text().strip()
            dict_els = columns[8].find_all("a")
            dict_links = []
            extracted_text = ""
            cleaned_text = ""
            for el in dict_els:
                href = el.get("href")
                dict_links.append(baseURL + href)

                if el.get_text(strip=True) == "Lewis & Short":
                    newurl = baseURL + href
                    page = requests.get(newurl)
                    soup = BeautifulSoup(page.content, "html.parser")
                    target_div = soup.find("div", class_="text")
                    if target_div:
                        for element in target_div.find_all():
                            element.extract()

                        extracted_text = target_div.get_text(strip=True)
                        cleaned_text = extracted_text.lstrip(",").strip()
            dict_links = ", ".join(dict_links)
            print(
                f"Classical Word: {clas_word}, Weighted Frequency: {weighted_freq}, Definition: {definition}, Dictionary Links: {dict_links}, Principal Parts: {cleaned_text}"
            )
            writer.writerow(
                [clas_word, weighted_freq, definition, dict_links, cleaned_text]
            )
            counter = counter + 1
            progress_bar.update(counter)
    f.seek(f.tell() - 1)
    progress_bar.close()
    print(f"{counter} words written to output")
    f.close()
