import glob, os, re
from path_finder import path_finder

## Uncomment to activate. You can only activate one at the time. (Uncomment = remove hash tag)
#from Albanian import Sounds
#from Danish_Norwegian_Swedish import Sounds
#from Faroese import Sounds
#from Icelandic import Sounds
#from Latin import Sounds
#from Proto_Germanic import Sounds
#from Old_Church_Slavonic import Sounds
#from Old_Danish import Sounds
#from Old_Icelandic import Sounds

CWD = os.getcwd()
PATH = path_finder()


for filename in glob.glob(PATH+'/sort/Result/*.txt'):
    with open(filename, 'r', encoding="utf8") as f:
        read_tekst = f.read()


print('''
Tast 1 for søgning i forlyd (absolut forlyd).
Tast 2 for søgning i indlyd.
Tast 3 for søgning i udlyd (absolut udlyd).
Tast 4 for søgning i det hele af ordene.

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
    elif valg == "4":
        hel_ord()
    else:
        exit(0)


def forlyd():
    print("""
Her kan du søge på i absolut forlyd. Du har nu følgende valg; indtaster du:

1     Frisøgning
2     Frisøgning + Lydgruppe
3     Lydgruppe + Frisøgning

Ved både 2 og 3 kan du vælge at ikke indtaste noget sælg, bare vælge en lydgruppe.
""")

    indput = input("\nIndtast dit valg: ")
    if indput == "1":
        indput = input("\nSkriv dit ord med eller uden regular expression: ")
        pattern = r"\b"+indput+r"\w*"
    elif indput == "2":
        indput = input("Skriv dit ord med eller uden regular expression: ")
        pattern = r"\b"+indput+Sounds()+r"\w*"
    elif indput == "3":
        indput = input("Skriv dit ord med eller uden regular expression: ")
        pattern = r"\b"+Sounds()+indput+r"\w*"
    else:
        exit(0)

    result = re.findall(pattern, read_tekst, re.IGNORECASE)
    navn = "forlyd"
    make_file(result, navn)


def indlyd():
    print("""
Her kan du søge på i indlyd. Du har nu følgende valg; indtaster du:

1     Frisøgning
2     Frisøgning + Lydgruppe
3     Lydgruppe + Frisøgning

Ved både 2 og 3 kan du vælge at ikke indtaste noget sælg, bare vælge en lydgruppe.
""")

    indput = input("\nIndtast dit valg: ")
    if indput == "1":
        indput = input("\nSkriv dit ord med eller uden regular expression: ")
        pattern = r"\w+"+indput+r"\w+"
    elif indput == "2":
        indput = input("Skriv dit ord med eller uden regular expression: ")
        pattern = r"\w+"+indput+Sounds()+r"\w+"
    elif indput == "3":
        indput = input("Skriv dit ord med eller uden regular expression: ")
        pattern = r"\w+"+Sounds()+indput+r"\w+"
    else:
        exit(0)
    result = re.findall(pattern, read_tekst, re.IGNORECASE)
    navn = "indlyd"
    make_file(result, navn)


def udlyd():
    print("""
Her kan du søge på i absolut udlyd. Du har nu følgende valg; indtaster du:

1     Frisøgning
2     Frisøgning + Lydgruppe
3     Lydgruppe + Frisøgning

Ved både 2 og 3 kan du vælge at ikke indtaste noget sælg, bare vælge en lydgruppe.
""")

    indput = input("\nIndtast dit valg: ")
    if indput == "1":
        indput = input("\nSkriv dit ord med eller uden regular expression: ")
        pattern = r"\w*"+indput
    elif indput == "2":
        indput = input("Skriv dit ord med eller uden regular expression: ")
        pattern = r"\w*"+indput+Sounds()
    elif indput == "3":
        indput = input("Skriv dit ord med eller uden regular expression: ")
        pattern = r"\w*"+Sounds()+indput
    else:
        exit(0)
    
    result = re.findall(pattern, read_tekst, re.IGNORECASE)
    navn = "udlyd"
    make_file(result, navn)


def hel_ord():
    print("""
Her kan du søge på i indlyd. Du har nu følgende valg; indtaster du:

1     Frisøgning
2     Frisøgning + Lydgruppe
3     Lydgruppe + Frisøgning

Ved både 2 og 3 kan du vælge at ikke indtaste noget sælg, bare vælge en lydgruppe.
""")

    indput = input("\nIndtast dit valg: ")
    if indput == "1":
        indput = input("\nSkriv dit ord med eller uden regular expression: ")
        pattern = r"\b\w*"+indput+r"\w*"
    elif indput == "2":
        indput = input("Skriv dit ord med eller uden regular expression: ")
        pattern = r"\b\w*"+indput+Sounds()+r"\w*"
    elif indput == "3":
        indput = input("Skriv dit ord med eller uden regular expression: ")
        pattern = r"\b\w*"+Sounds()+indput+r"\w*"
    else:
        exit(0)
    result = re.findall(pattern, read_tekst, re.IGNORECASE)
    navn = "hel_ord"
    make_file(result, navn)


def make_file(result, navn):
    set_tekst = set(result)
    sorted_tekst = sorted(set_tekst, key=str.lower)
    nice_list = '\n\n'.join(sorted_tekst)
    ordliste = open(CWD+'/Result/'+navn+'_ordliste.txt', 'w', encoding='UTF8')
    ordliste.write("" + nice_list)
    ordliste.close()


start()

print("""
extractor.py     done running:

word_list.txt is ready in the Result directory.

Visit my GitHub at: https://github.com/NikolaiS1900
I can be contacted via: sandbecks_github@protonmail.com

Kind regards
- Nikolai Sandbeck
""")
