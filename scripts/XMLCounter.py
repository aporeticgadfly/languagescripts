#!/usr/bin/python3

import xml.etree.ElementTree as ET
import argparse

parser = argparse.ArgumentParser(
    prog="XMLCounter",
    description="counts number of occurrences of given element in given file",
)
parser.add_argument("input", help="name of xml file to count from")
parser.add_argument("-t", "--tag", help="tag to search in input file")
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()

input_file = args.input
tag = args.tag

# Parse the XML file
tree = ET.parse(input_file)
root = tree.getroot()

# Count the elements with the specified tag
count = len(root.findall(f".//{tag}"))

print(f"Number of <{tag}> elements: {count}")
