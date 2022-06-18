import glob, os

CWD = os.getcwd()
# Går i overmappen.
PATH = os.path.dirname(CWD) 

# Indlæser ordlisten dannet af sort.py
for filename in glob.glob(PATH+'/sort/Result/*.txt'):
	with open(filename, 'r', encoding="utf8") as f:
		READ_TEXT = f.read()

# Spejlvender ordliste.
TEXT_MIRRORING = READ_TEXT[::-1]

# Sætter det i listeform.
TEXT_MIRRORING_LIST = TEXT_MIRRORING.split()

# Opstiller alt i alfabetisk rækkefølge.
SORTED_TEXT = sorted(TEXT_MIRRORING_LIST, key=str.lower)

# Laver listen om til en streng og tilføjer dobbeltlinjeskift imellem hvert item.
TEXT = '\n \n'.join(SORTED_TEXT)

# Danner en tekstfil ved navn spejlvendt_ordliste.
MIRRORED_TEXT = open(CWD+'/Result/mirrored_word_list.txt', 'w')

# Skriver indholdet af variablen TEKST til tekstfilen.
MIRRORED_TEXT.write("" + TEXT)

# Lukker tekstfilen.
MIRRORED_TEXT.close()

print("""
mirror.py     done running:

word_list.txt is ready in the Result directory.

Visit my GitHub at: https://github.com/NikolaiS1900
I can be contacted via: sandbecks_github@protonmail.com

Kind regards
- Nikolai Sandbeck
""")
