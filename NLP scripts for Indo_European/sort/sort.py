import glob, os
from path_finder import path_finder

CWD = os.getcwd()
PATH = path_finder()

for filename in glob.glob(PATH+'/preprocess/Result_remove_characters/*.txt'):
	with open(filename, 'r', encoding="utf8") as f:
		READ_TEXT = f.read()

SPLIT_TEXT = READ_TEXT.split()

SET_TEXT = set(SPLIT_TEXT)

SORTED_TEXT = sorted(SET_TEXT, key=str.lower)

TEXT = '\n \n'.join(SORTED_TEXT)

ORDLISTE = open(CWD+'/Result/word_list.txt', 'w', encoding="utf8")

ORDLISTE.write("" + TEXT)

ORDLISTE.close()

print("""
sort.py     done running:

word_list.txt is ready in the Result directory.

Visit my GitHub at: https://github.com/NikolaiS1900
I can be contacted via: sandbecks_github@protonmail.com

Kind regards
- Nikolai Sandbeck
""")
