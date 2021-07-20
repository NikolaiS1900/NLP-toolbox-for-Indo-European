import glob, os

cwd = os.getcwd()

for filename in glob.glob(cwd+'/Måltekst/*.txt'):
	with open(filename, 'r', encoding='UTF-8') as f:
		read_tekst = f.read()

tegnliste = open(str(cwd)+'/Resultat/tegnliste.txt', 'w', encoding='UTF-8')

set_tekst = set(read_tekst)

sorted_set = sorted(set_tekst, key=str.lower)

streng = ''.join(sorted_set)

liste = []

for i in streng:
	liste.append(i+'\n \n')

tegn = ''.join(liste)

tegnliste.write("" + tegn)

tegnliste.close()

print("""Resultatet er klart.
- Mvh. Nikolai Sandbeck

Besøg min github: https://github.com/NikolaiS1900
Jeg kan kontaktes på: sandbecks_github@protonmail.com""")
