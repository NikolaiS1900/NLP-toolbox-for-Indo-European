import glob, os, re
from path_finder import path_finder

CWD = os.getcwd()
PATH = path_finder()

for filename in glob.glob(PATH+'/Target_text/*.txt'):
	with open(filename, 'r', encoding='UTF-8') as f:
		READ_TARGET_TEXT = f.read()

SET_TEXT = set(READ_TARGET_TEXT)

SORTED_SET = sorted(SET_TEXT, key=str.lower)

STRING = ''.join(SORTED_SET)

LIST = []

for item in STRING:
	LIST.append(item)

CHARACTERS = ' '.join(LIST)

#CHARACTERS_NO_WHITE_SPACE = re.sub('\s', '', CHARACTERS)
#CHARACTERS_SPACE = CHARACTERS_NO_WHITE_SPACE.replace('', ' ')
CHARACTERS_SPACE_LIST = CHARACTERS.split()
CHARACTERS_SPACE_STRING = ' '.join(CHARACTERS_SPACE_LIST)

CHAR_LIST = open(CWD+'/Result_character_list/character_list.txt', 'w', encoding='UTF-8')

CHAR_LIST.write("" + CHARACTERS_SPACE_STRING)

CHAR_LIST.close()

print("""
1_character_list.py     done running:

word_list.txt is ready in the Result directory.

Visit my GitHub at: https://github.com/NikolaiS1900
I can be contacted via: sandbecks_github@protonmail.com

Kind regards
- Nikolai Sandbeck
""")
