import argparse
import csv
import opencc
from PIL import Image, ImageDraw, ImageFont

parser = argparse.ArgumentParser(prog='UnihanLookup.py', description='takes in list of traditional characters and outputs and writes corresponding simplified and japanese characters and their meanings')
parser.add_argument('output', help='name of txt file to output to')
parser.add_argument('input', help="path of input csv")
parser.add_argument('-u', '--unihan', help="path of unihan database")
args = parser.parse_args()

def get_unicode_codepoint():

def convert_to_glyph():
    width, height = 200, 100
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Load fonts for Hanzi and Kanji (ensure these fonts support the characters)
    font_hanzi = ImageFont.load_default()  # Replace with a Hanzi font path
    font_kanji = ImageFont.load_default()  # Replace with a Kanji font path

    # Set the language context to render as Hanzi (Chinese)
    draw.text((10, 10), chr(unicode_code_point), font=font_hanzi, fill="black")

    # Set the language context to render as Kanji (Japanese)
    draw.text((10, 50), chr(unicode_code_point), font=font_kanji, fill="black")

    # Save or display the rendered image
    image.save("character_rendering.png")

def get_meanings():
    #EDICT/CEDICT Or whatever

def main():

    with open(input_file, 'r') as csv_file:
        csv_writer = csv.writer(f)
        csv_writer.writerow(["Traditional Character", "Traditional Meanings", "Simplified Character", "Simplified Meanings", "Japanese Character", "Japanese Meanings"])
        # Create a CSV reader object
        csv_reader = csv.reader(csv_file)
    
        # Loop through each row in the CSV file
        for row in csv_reader:
            get_unicode_codepoint()
            convert_to_glyph()
            get_meanings()
            output()

if __name__ == "__main__":
    main()
