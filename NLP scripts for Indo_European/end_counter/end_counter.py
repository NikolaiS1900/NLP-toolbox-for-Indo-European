import glob, os
from collections import Counter

CWD = os.getcwd()
# Går i overmappen.
PATH = os.path.dirname(CWD)

for filename in glob.glob(PATH+'/preprocess/preprocessed_text/*.txt'):
	with open(filename, 'r', encoding="utf8") as f:
		READ_TEXT = f.read()

SPLIT_TEXT = READ_TEXT.split()

END_LIST = []

for item in SPLIT_TEXT:
    END_LIST.append(item[-1])

for val, freq in sorted(Counter(END_LIST).items()):
    print(val, ' : ', freq)
