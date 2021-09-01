import glob, os
from tegnfjerner import tegnfjerner

CWD = os.getcwd()

for filename in glob.glob(CWD+'/Måltekst/*.txt'):
	with open(filename, 'r', encoding="utf8") as f:
		READ_TEKST = f.read()

RENS_TEKST = tegnfjerner(READ_TEKST)

SPLIT_TEKST = RENS_TEKST.split()

SET_TEKST = set(SPLIT_TEKST)

SORTED_TEKST = sorted(SET_TEKST, key=str.lower)

TEKST = '\n \n'.join(SORTED_TEKST)

ORDLISTE = open(CWD+'/Resultat/ordliste.txt', 'w', encoding="utf8")

ORDLISTE.write("" + TEKST)

ORDLISTE.close()

print("""Resultatet er klart.
- Mvh. Nikolai Sandbeck

Besøg min github: https://github.com/NikolaiS1900
Jeg kan kontaktes på: sandbecks_github@protonmail.com""")
