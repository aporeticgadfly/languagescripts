#!/usr/bin/python3
import requests
import time
import csv
import re
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser(prog='WiktRussianParser', description='scrapes wiktionary wordlist and outputs a list of all words to a local txt file')
parser.add_argument('-b', '--base-URL', required=True, help='the base URL of the wiktionary verb category page')
parser.add_argument('-k', '--key', required=True, type=str, help='html elements to iterate over (passed to soup.select())')
parser.add_argument('filename', help='name of txt file to output to')
parser.add_argument('-v', '--verbose', action='store_true')
args = parser.parse_args()

key = args.key
URL = args.base_URL
filename = args.filename
baseURL = "https://en.wiktionary.org"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

elements = [elements.text for elements in soup.select(key)]

with open(filename, 'w') as f:
	for item in elements:
		print(item)
		f.write(item)
		f.write(',')
	f.seek(f.tell() - 1)
	
	f.close()