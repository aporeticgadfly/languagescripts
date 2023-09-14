#!/usr/bin/python3
import beta_code
import argparse

parser = argparse.ArgumentParser(
    prog="BetaToUnicode",
    description="converts input in beta code encoding to unicode ancient greek output",
)
parser.add_argument("input", help="name of txt file to input from")
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()

input_file = args.input

with open(filename, "r") as f:
    beta_code_text = f.read()
    unicode_greek_text = beta_code.beta_code_to_greek(beta_code_text)
    if unicode_greek_text:
        print(unicode_greek_text)
    else:
        print("error, ensure input is in beta code")
