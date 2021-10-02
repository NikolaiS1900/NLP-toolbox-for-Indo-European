import glob
import os
from path_finder import path_finder

# CWD = current working directory = den gældende arbejdsmappe.
CWD = os.getcwd()

# path_finder er en funktion jeg selv har skrevet, den gennemgås en anden gang.
# Den gør bare, at når det kommer til at importere og gemme tekstfiler, så er det underordnet om scriptet køres
# på Windows eller styresystemer MacOS, UNIX og LINUX.
# path_finder hjælper scriptet, til at finde hovedmappen, som de andre mapper med værktøjer er gemt i.
PATH = path_finder()

# Indlæser tekstiflen og gemmer den i variablen READ_TARGET_TEXT.
for filename in glob.glob(PATH+'/Target_text/*.txt'):
    with open(filename, 'r', encoding='UTF-8') as f:
        READ_TARGET_TEXT = f.read()

# Splitter hele teksten op i alle individuelle tegn og fjerner alle dubletter.
# Dette gemmes i variablen SET_TEXT
SET_TEXT = set(READ_TARGET_TEXT)

# Stiller indholdet af variablen SET_TEXT op i alfabetisk rækkefølge.
# Dette bliver gemt som i liste i variablen SORTED_TEXT
SORTED_SET = sorted(SET_TEXT, key=str.lower)

# Metoden ''.join() bruges her til at opløse listen.
# Mellemrummet ' ' gør at hvert element får et mellemrum imellem sig
# Så ikke alle tegn, kommmer til at stå klods op ad hinanden.
CHARACTERS_SPACE_STRING = ' '.join(SORTED_SET)

# Dette fjerner lige undøvendige mellemrum og linjeskift før og efter.
STRIPPED_STRING = CHARACTERS_SPACE_STRING.strip()

# Danner en tekstfil ved navn character_list.txt, og gemmer den i mappen Result_character_list.
CHAR_LIST = open(CWD+'/Result_character_list/character_list.txt', 'w', encoding='UTF-8')

# Gemmer indholdet af variablen STRIPPED_STRING i tekstfilen.
CHAR_LIST.write("" + STRIPPED_STRING)

# Lukker tekstfilen pænt.
CHAR_LIST.close()

# Udskriver en hilsen.
print("""
1_character_list.py     done running:

character_list.txt is ready in the Result directory.

Visit my GitHub at: https://github.com/NikolaiS1900
I can be contacted via: sandbecks_github@protonmail.com

Kind regards
- Nikolai Sandbeck
""")
