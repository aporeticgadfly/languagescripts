#!/usr/bin/python3
# goes through list of verbs and extracts all of the root verbs from it
# use on verbs
import argparse

parser = argparse.ArgumentParser(
    prog="RootExtractor", description="gets stammformen of strong verbs"
)
parser.add_argument("input", help="name of txt file to input from")
args = parser.parse_args()

input_file = args.input

prefixes = [
    "ab",
    "an",
    "auf",
    "aus",
    "be",
    "bei",
    "dar",
    "dran",
    "durch",
    "ein",
    "ent",
    "er",
    "fort",
    "frei",
    "ge",
    "her",
    "hin",
    "hinter",
    "hoch",
    "mit",
    "nach",
    "tief",
    "über",
    "um",
    "unter",
    "ver",
    "vor",
    "weg",
    "zer",
    "zu",
    "auseinander",
    "empor",
    "entgegen",
    "entlang",
    "entzwei",
    "fern",
    "fest",
    "für",
    "gegen",
    "gegenüber",
    "heim",
    "hinterher",
    "los",
    "neben",
    "nieder",
    "weiter",
    "zurecht",
    "zurück",
    "zusammen",
    "miss",
    "wider",
    "wieder",
    "fehl",
    "statt",
    "wahr",
    "zuvor",
    "zwangsein",
    "zupass",
    "zugute",
    "zufrieden",
    "wund",
    "wunder",
    "wiederauf",
    "warm",
    "vorweg",
    "vorbei",
    "vorüber",
    "voraus",
    "voran",
    "voll",
    "verloren",
    "umher",
    "umeinander",
    "übrig",
    "überein",
    "tot",
    "still",
    "stand",
    "sicher",
    "selig",
    "sein",
    "seil",
    "schwarz",
    "schwer",
    "schief",
    "runter",
    "rund",
    "rum",
    "rüber",
    "richtig",
    "rein",
    "recht",
    "raus",
    "ran",
    "quer",
    "offen",
    "näher",
    "nahe",
    "kürzer",
    "kurz",
    "mal",
    "mass",
    "maß",
    "leer",
    "leicht",
    "kund",
    "krank",
    "klein",
    "klar",
    "kaputt",
    "kahl",
    "irre",
    "inne",
    "hinzu",
    "hinein",
    "hindurch",
    "hinaus",
    "hinauf",
    "hinab",
    "hier",
    "hierher",
    "hervor",
    "herunter",
    "herum",
    "herüber",
    "herein",
    "herbei",
    "heraus",
    "heran",
    "herab",
    "hell",
    "heilig",
    "gut",
    "gross",
    "groß",
    "gerade",
    "fremd",
    "fern",
    "feil",
    "fehl",
    "falsch",
    "eis",
    "einher",
    "drauf",
    "dazu",
    "dazwischen",
    "davon",
    "da",
    "dar",
    "darnieder",
    "darüber",
    "daneben",
    "dahinter",
    "dahin",
    "daher",
    "dafür",
    "dabei",
    "breit",
    "brach",
    "blank",
    "bevor",
    "bereit",
    "bekannt",
    "beiseite",
    "aufrecht",
    "allein",
    "acht",
    "ähnlich",
    "abhanden",
]
roots = []
prefixfoundflag = 0
nondoubledprefixfoundflag = 0
placeholder = ""
token = ""

if __name__ == "__main__":
    with open(input_file, "r") as file:
        content = file.read()
        words = content.split(",")
        for line in words:
            prefixfoundflag = 0
            nondoubledprefixfoundflag = 0
            placeholder = ""
            token = ""
            for i in range(len(line)):
                token += line[i]
                if i >= 1 and nondoubledprefixfoundflag == 0:
                    for prefix in prefixes:
                        if token == prefix:
                            prefixfoundflag = 1
                            if (
                                prefix == "zu"
                                or prefix == "be"
                                or prefix == "gegen"
                                or prefix == "ent"
                                or prefix == "hin"
                                or prefix == "aus"
                                or prefix == "hinter"
                                or prefix == "bei"
                                or prefix == "ab"
                                or prefix == "da"
                                or prefix == "wund"
                                or prefix == "wieder"
                                or prefix == "vor"
                                or prefix == "ver"
                                or prefix == "um"
                                or prefix == "über"
                                or prefix == "hier"
                                or prefix == "her"
                                or prefix == "ein"
                                or prefix == "auf"
                            ):
                                # store token, keep looking, if reach newline and no new prefix found revert to token
                                print("placeholder stored")
                                print(prefix)
                                placeholder = token

                            else:
                                nondoubledprefixfoundflag = 1
                                root = line.partition(token)[2]  #
                                print("nondoubled")
                                print(root)
                                print(line)
                                roots.append(root)
                                break
                            break
            if prefixfoundflag == 0:
                print("no prefix found")
                print(line)
                roots.append(line)

            if prefixfoundflag == 1 and nondoubledprefixfoundflag == 0:
                root = line.partition(placeholder)[2]  #
                print("reverting to placeholder")
                print(line)
                print(root)
                roots.append(root)

        file.close()
        with open("roots.txt", "w") as f:
            rootset = set(roots)
            for root in rootset:
                f.write(root)
                f.write("\n")
        f.close()
