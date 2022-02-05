import glob, os, re
from collections import Counter

CWD = os.getcwd()
# Går i overmappen.
PATH = os.path.dirname(CWD) 

for filename in glob.glob(PATH+'/preprocess/preprocessed_text/*.txt'):
	with open(filename, 'r', encoding="utf8") as f:
		READ_TEXT = f.read()


FIND = re.findall('\w{2}', READ_TEXT)

RESULT = []

for val, freq in sorted(Counter(FIND).items()):
    RESULT.append(f"{val} : {freq}")

NICE_LIST = '\n\n'.join(RESULT)

PRINT = open(CWD+'/Result/sound_combi_count.txt', 'w', encoding='utf8')
PRINT.write('' + NICE_LIST)
PRINT.close()


print("""
sound_combi_counter.py     done running:

sound_combi_count.txt is ready in the Result directory.

Visit my GitHub at: https://github.com/NikolaiS1900
I can be contacted via: sandbecks_github@protonmail.com

Kind regards
- Nikolai Sandbeck
""")
