import os, re, glob
from path_finder import path_finder

CWD = os.getcwd()
PATH = path_finder()

file_list = glob.glob(os.path.join(PATH+"/preprocess/preprocessed_text/*.txt"))

CORPUS = []

for file_path in file_list:
    with open(file_path) as f_input:
        CORPUS.append(f_input.read())

KORPUS_TEKST = ' '.join(CORPUS)

INDPUT = input("write search word: ")

# Finder eksempler i det samlede korpus, og sorterer den alle dubletter fra.
FIND_PATTERN = re.findall(INDPUT, KORPUS_TEKST, re.IGNORECASE)


PATTERN = '文'.join(FIND_PATTERN)
PATTERN = PATTERN.lower()
PATTERN = PATTERN.split('文')
SET_PATTERN_LIST = set(PATTERN)


# Denne funktioner finder linjenumrene i tekstfilerne

def word_search(key, filename):
    with open(PATH+'/preprocess/preprocessed_text/'+filename) as file:  # opening the file using with to ensure it closes after the block of code is executed
        lines = file.readlines()  # reading the lines of the files in order
        lines = '文'.join(lines)
        lines = lines.lower()
        lines = lines.split('文')
    for number, line in enumerate(lines, 1):  # using enumerate to map each line of the file to it's line_number
        if key in line:  # searching for the keyword in file
            print(f"er på linje: {number}")  # returning the line number if the keyword
        else:
            pass


# Denne funktioner tager hvert item, som jo er en streng, og finder linjenummer (via word_search) og så finder den
# Hvilke dokumenter der har den sætning og så citerer den sætningen

TARGET_DIRECTORY= (PATH+'/preprocess/preprocessed_text/')
directory = os.listdir(TARGET_DIRECTORY)

def quote_examples(item):
    #print(item)
    for fname in directory:
        if os.path.isfile(TARGET_DIRECTORY + os.sep + fname):
            # Full path
            with open(TARGET_DIRECTORY + os.sep + fname, 'r', encoding='utf8') as f:
                f = f.read().lower()
            if item in f:
                print(f'{item}\n')
                word_search(item, fname)
                print(f'\ni dokument: %s' % fname)
        else:
            pass


# Denne comprehension list udskriver det hele til terminalen.
# For at få det gemt i en tekstfil, kan man i både Bash Shell, PowerShell og CMD skrive:
# whereis.py > oversigt.txt

PRINT = [quote_examples(item) for item in SET_PATTERN_LIST]

