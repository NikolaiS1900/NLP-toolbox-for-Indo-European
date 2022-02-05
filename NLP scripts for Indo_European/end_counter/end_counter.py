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

RESULT = []

for val, freq in sorted(Counter(END_LIST).items()):
    RESULT.append(f"-{val} : {freq}")

NICE_LIST = '\n\n'.join(RESULT)

PRINT = open(CWD+'/Result/end_count_list.txt', 'w', encoding='utf8')
PRINT.write('' + NICE_LIST)
PRINT.close()


print("""
end_counter.py     done running:

end_count_list.txt is ready in the Result directory.

Visit my GitHub at: https://github.com/NikolaiS1900
I can be contacted via: sandbecks_github@protonmail.com

Kind regards
- Nikolai Sandbeck
""")
