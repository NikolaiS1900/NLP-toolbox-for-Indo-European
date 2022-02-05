import glob, os, re

# Finder stien på den pågældende mappe vi er i (current working directory)
CWD = os.getcwd()

# Går i overmappen.
PATH = os.path.dirname(CWD) 

# Fra overmappen går den ind i Target_text, og finder målteksten.
for filename in glob.glob(PATH+'/Target_text/*.txt'):
	with open(filename, 'r', encoding='UTF-8') as f:
		READ_TEXT = f.read()

# Fra CWD, går den ind i mappen Result_character_list, og finder tekstilen
# der inde.
for filename in glob.glob(CWD+'/Result_character_list/*.txt'):
	with open(filename, 'r', encoding='UTF-8') as f:
		CHAR_LIST_STRING = f.read()

# Vores tegnliste laves nu om til en liste
CHAR_LIST = CHAR_LIST_STRING.split()


# Denne for loop, tager alle tegn CHAR_LIST,
# kigger efter dem i READ_TEXT og erstatter tegnene
# med ingen ting.
for item in CHAR_LIST:
    READ_TEXT = READ_TEXT.replace(item, '')

# Går ind i mappen preprocessed_text og danner en tekstfil ved navn preprocessed_text.txt
CHARS_GONE = open(CWD+'/preprocessed_text/preprocessed_text.txt', 'w', encoding='UTF-8')
# Skriver indholdet af READ_TEXT til tekstiflen.
# Hvis der er en tekstfil ved navn preprocessed_text.txt i forvejen, vil indholdet blive overskrevet.
CHARS_GONE.write("" + READ_TEXT)
# Lukker tekstfilen.
CHARS_GONE.close()


print("""
preprocess.py     done running:

word_list.txt is ready in the Result directory.

Visit my GitHub at: https://github.com/NikolaiS1900
I can be contacted via: sandbecks_github@protonmail.com

Kind regards
- Nikolai Sandbeck
""")
