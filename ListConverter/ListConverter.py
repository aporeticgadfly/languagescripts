import argparse

parser = argparse.ArgumentParser(prog='ListConverter.py', description='takes in list and converts it to a csv appropriate for Mnemosyne import')
parser.add_argument('output', help='name of csv file to output to')
parser.add_argument('input', help="path of input txt")
parser.add_argument('-t', '--title', help="title of list")
args = parser.parse_args()

output = args.output
input = args.input
title = args.title

items = ''

with open(input, 'r', newline='') as file:
    with open(output, 'w', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.write_row("Title", "Items")
        contents = file.read().split(",")
        for content in contents:
        	items += content
        	items += "#@!"
        items = items[:-3]
        csv_writer.write_row([title, items])
       