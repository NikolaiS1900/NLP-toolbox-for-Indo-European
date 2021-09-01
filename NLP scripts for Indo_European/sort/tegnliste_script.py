import glob, os

CWD = os.getcwd()

for filename in glob.glob(CWD+'/Måltekst/*.txt'):
	with open(filename, 'r', encoding='UTF-8') as f:
		read_tekst = f.read()

tegnliste = open(CWD+'/Tegnliste/tegnliste.txt', 'w', encoding='UTF-8')

set_tekst = set(read_tekst)

sorted_set = sorted(set_tekst, key=str.lower)

streng = ''.join(sorted_set)

liste = []

for i in streng:
	liste.append(i)

tegn = ''.join(liste)

tegnliste.write("" + tegn)

tegnliste.close()

print("""Resultatet er klart.
- Mvh. Nikolai Sandbeck

Besøg min github: https://github.com/NikolaiS1900
Jeg kan kontaktes på: sandbecks_github@protonmail.com""")
