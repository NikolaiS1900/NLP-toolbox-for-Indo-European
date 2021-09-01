import glob, os, re
from path_finder import path_finder

CWD = os.getcwd()
PATH = path_finder()

for filename in glob.glob(PATH+'/Target_text/*.txt'):
	with open(filename, 'r', encoding='UTF-8') as f:
		READ_TEXT = f.read()

for filename in glob.glob(CWD+'/Result_character_list/*.txt'):
	with open(filename, 'r', encoding='UTF-8') as f:
		CHAR_LIST_STRING = f.read()


CHAR_LIST = CHAR_LIST_STRING.split()

BACKSLASH = '\\'

for i in READ_TEXT:
    if BACKSLASH in CHAR_LIST:
        READ_TEXT = re.sub('\\\\', '', READ_TEXT)
    if i in CHAR_LIST:
        READ_TEXT = READ_TEXT.replace(i, '')
    else:
        pass

CHARS_GONE = open(CWD+'/Result_remove_characters/cleaned_text.txt', 'w', encoding='UTF-8')
CHARS_GONE.write("" + READ_TEXT)
CHARS_GONE.close()


print("""
2_remove_characters.py     done running:

word_list.txt is ready in the Result directory.

Visit my GitHub at: https://github.com/NikolaiS1900
I can be contacted via: sandbecks_github@protonmail.com

Kind regards
- Nikolai Sandbeck
""")
