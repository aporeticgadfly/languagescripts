#!/usr/bin/python3
import csv
import argparse

parser = argparse.ArgumentParser(
    prog="PinyinGrouper.py",
    description="takes in list of chinese words, groups them according to homonyms",
)
parser.add_argument("output", help="name of file to output to")
parser.add_argument("input", help="path of input csv")
parser.add_argument("-s", "--sound", required=True, help="sound field of csv file")
parser.add_argument("-m", "--meaning", required=True, help="meaning field of csv file")
args = parser.parse_args()

# Replace 'your_file.csv' with the actual path to your CSV file
input_file = args.input
output = args.output
soundcol = int(args.sound)
meaningcol = int(args.meaning)
soundmap = {}

# Open the CSV file in read mode
with open(input_file, "r", newline="") as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)

    # Loop through each row in the CSV file
    for row in csv_reader:
        # Print each cell value in the current row
        for sound in soundmap:
            if row[colval] == sound:
                soundmap[sound].append(row[meaningcol])
                foundflag = True
                break
        if foundflag == true:
            foundflag = False
        else:
            soundmap[row[soundcol]].append(row[meaningcol])

with open(output, "w", newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.write_row("Sound", "Meanings")

    for sound, meanings in soundmap.items:
        meanings_str = ", ".join(meanings)
        csv_writer.write_row(sound, meanings_str)
