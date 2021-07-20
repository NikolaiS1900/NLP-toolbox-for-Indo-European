import glob, os, re

cwd = os.getcwd()

for filename in glob.glob(cwd+'/Måltekst/*.txt'):
	with open(filename, 'r', encoding="utf8") as f:
		read_target = f.read()

for filename in glob.glob(cwd+'/Tegnliste/*.txt'):
	with open(filename, 'r', encoding="utf8") as f:
		read_tegnliste = f.read()

list_tegnliste = read_tegnliste.split()

backslash = '\\'

for i in read_target:
    if backslash in list_tegnliste:
        read_target = re.sub('\\\\', '', read_target)
    if i in list_tegnliste:
        read_target = read_target.replace(i, '')
    else:
        pass

renset_tekst = open(str(cwd)+'/Resultat/renset_tekst.txt', 'w', encoding="utf8")

renset_tekst.write("" + read_target)
renset_tekst.close

print("""Resultatet er klart.
- Mvh. Nikolai Sandbeck

Besøg min github: https://github.com/NikolaiS1900
Jeg kan kontaktes på: sandbecks_github@protonmail.com""")
