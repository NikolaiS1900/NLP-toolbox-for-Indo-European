import glob, os

cwd = os.getcwd()

for filename in glob.glob(cwd+'/Måltekst/*.txt'):
	with open(filename, 'r', encoding="utf8") as f:
		read_tekst = f.read()

ordliste = open(str(cwd)+'/Resultat/ordliste.txt', 'w', encoding="utf8")

split_tekst = read_tekst.split()

set_tekst = set(split_tekst)

sorted_tekst = sorted(set_tekst, key=str.lower)

tekst = '\n \n'.join(sorted_tekst)

ordliste.write("" + tekst)

ordliste.close()

print("""Resultatet er klart.
- Mvh. Nikolai Sandbeck

Besøg min github: https://github.com/NikolaiS1900
Jeg kan kontaktes på: sandbecks_github@protonmail.com""")
