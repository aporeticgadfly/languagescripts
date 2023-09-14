#!/usr/bin/python3
import requests
import time
import csv
import re
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser(prog='WiktVerbParser', description='scrapes wiktionary verb categories and outputs a list of all verbs in said category to a local txt file')
parser.add_argument('-b', '--base-URL', required=True, help='the base URL of the wiktionary verb category page')
parser.add_argument('-p', '--num-pages', required=True, type=int, help='the number of times to follow next button aka total verb entries divided by number displayed at once by wiktionary')
parser.add_argument('filename', help='name of txt file to output to')
parser.add_argument('-v', '--verbose', action='store_true')
args = parser.parse_args()

pagenum = args.num_pages
URL = args.base_URL
filename = args.filename
baseURL = "https://en.wiktionary.org"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

elements = [elements.text for elements in soup.select('#mw-pages li a')]

with open(filename, 'w') as f:
	for item in elements:
		print(item)
		f.write(item)
		f.write(',')

	for x in range(0, pagenum):
		nextbtn = soup.find("a", string="next page")
		btnhref = nextbtn.get('href')
		nextpage = requests.get(baseURL + btnhref)
		soup = BeautifulSoup(nextpage.content, "html.parser")
		elements = [elements.text for elements in soup.select('#mw-pages li a')]
		for item in elements:
			print(item)
			f.write(item)
			f.write(',')
	f.close()
