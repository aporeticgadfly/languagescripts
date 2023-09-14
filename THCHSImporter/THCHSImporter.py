#!/usr/bin/python3
import os
import csv
import argparse

parser = argparse.ArgumentParser(prog='THCHSImporter.py', description='import THCHS corpus and outputs as anki readable csv file')
parser.add_argument('output', help='name of txt file to output to')
parser.add_argument('input_file', help="name of folder where THCHS folder is downloaded")
args = parser.parse_args()

output = args.output
input_file = args.input_file

root_folder = input_file
expanded_root_folder = os.path.expanduser(root_folder)

with open(output, 'w', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["Audio", "Text"])

    # Traverse through the directory tree
    for root, dirs, files in os.walk(expanded_root_folder):
        for file in files:
            if file.endswith(".mp3"):
                corresponding_tr_file = file.replace(".mp3", ".trn")
                if corresponding_tr_file in files:
                    audio_path = file
                    with open(os.path.join(root, corresponding_tr_file), "r", encoding="utf-8") as tr_file:
                        text_content = tr_file.read().strip()
                        csv_writer.writerow([audio_path, text_content])
