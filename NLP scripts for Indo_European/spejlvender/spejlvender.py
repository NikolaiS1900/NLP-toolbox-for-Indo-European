import glob, os
from path_finder import path_finder

CWD = os.getcwd()
PATH = path_finder()

# Indlæser ordlisten dannet af sort.py
for filename in glob.glob(PATH+'/sort/Resultat/*.txt'):
	with open(filename, 'r', encoding="utf8") as f:
		READ_TEKST = f.read()

# Spejlvender ordliste.
TEKST_REVERSING = READ_TEKST[::-1]

# Sætter det i listeform.
TEKST_REVERSING_LIST = TEKST_REVERSING.split()

# Opstiller alt i alfabetisk rækkefølge.
SORTED_TEKST = sorted(TEKST_REVERSING_LIST, key=str.lower)

# Laver listen om til en streng og tilføjer dobbeltlinjeskift imellem hvert item.
TEKST = '\n \n'.join(SORTED_TEKST)

# Danner en tekstfil ved navn spejlvendt_ordliste.
REVERSED_TEKST = open(CWD+'/Resultat/spejlvendt_ordliste.txt', 'w')

# Skriver indholdet af variablen TEKST til tekstfilen.
REVERSED_TEKST.write("" + TEKST)

# Lukker tekstfilen.
REVERSED_TEKST.close()
