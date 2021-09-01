import os, re, glob

# Remove the #'s belows to activate.
from Proto_Germanic import Sounds



cwd = os.getcwd()

for filename in glob.glob(cwd+'/Måltekst/*.txt'):
	with open(filename, 'r', encoding="utf8") as f:
		read_tekst = f.read()

print('''Tast 1 for søgning i forlyd.
Tast 2 for søgning i indlyd.
Tast 3 for søgning i udlyd.

Søgningen vil finde alle ord der opfylder dine søgekriterier, og gemme disse ord i en seperat tekstfil.
''')


def start():

    valg = input("Indtast tal: ")

    if valg == "1":
        forlyd()
    elif valg == "2":
        indlyd()
    elif valg == "3":
        udlyd()
    else:
        exit(0)


def forlyd():
    indput = input("hvilken forlyd vil du søge på?: ")
    if indput == "RegEx":
        pattern = Sounds()+"\w*"
    else:
        pattern = indput+"\w*"
    result = re.findall(pattern, read_tekst, re.IGNORECASE)
    read_tekst_list = read_tekst.split()

    Result = []
    for a in result:
        for b in read_tekst_list:
            if a == b:
                Result.append(a)
    navn = "forlyd"
    make_file(Result, navn)


def indlyd():
    indput = input("hvilken indlyd vil du søge på: ")
    if indput == "RegEx":
        pattern = "\w+"+Sounds()+"\w+"
    else:
        pattern = "\w+"+indput+"\w+"
    result = re.findall(pattern, read_tekst, re.IGNORECASE)
    navn = "indlyd"
    make_file(result, navn)


def udlyd():
    indput = input("hvilken indlyd vil du søge på: ")
    if indput == "RegEx":
        pattern = "\w*"+Sounds()
    else:
        pattern = "\w*"+indput
    result = re.findall(pattern, read_tekst, re.IGNORECASE)
    navn = "udlyd"
    make_file(result, navn)

def make_file(result, navn):
    set_tekst = set(result)
    sorted_tekst = sorted(set_tekst, key=str.lower)
    nice_list = '\n \n'.join(sorted_tekst)
    ordliste = open(cwd+'/Resultat/'+navn+'_ordliste.txt', 'w', encoding='UTF8')
    ordliste.write("" + nice_list)
    ordliste.close()


start()

print("""
Resultatet er klart.
- Mvh. Nikolai Sandbeck

Besøg min github: https://github.com/NikolaiS1900
Jeg kan kontaktes på: sandbecks_github@protonmail.com""")
