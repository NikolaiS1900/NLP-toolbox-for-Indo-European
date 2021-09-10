import glob, os, re
from path_finder import path_finder
from collections import Counter

CWD = os.getcwd()
PATH = path_finder()

for filename in glob.glob(PATH+'/preprocess/preprocessed_text/*.txt'):
	with open(filename, 'r', encoding="utf8") as f:
		READ_TEXT = f.read()


FIND = re.findall('\w{2}', READ_TEXT)

for val, freq in sorted(Counter(FIND).items()):
    print(val, ' : ', freq)
