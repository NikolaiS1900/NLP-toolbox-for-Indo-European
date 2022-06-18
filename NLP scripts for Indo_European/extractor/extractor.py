import glob, os, re

## Uncomment to activate. You can only activate one at the time. (Uncomment = remove hash tag)
#from lang_pack.Albanian import Sounds
#from lang_pack.Danish_Norwegian_Swedish import Sounds
#from lang_pack.Faroese import Sounds
#from lang_pack.Icelandic import Sounds
#from lang_pack.Latin import Sounds
#from lang_pack.Proto_Germanic import Sounds
#from lang_pack.Old_Church_Slavonic import Sounds
from lang_pack.Old_Danish import Sounds
#from lang_pack.Old_Icelandic import Sounds

CWD = os.getcwd()
# Går i overmappen.
PATH = os.path.dirname(CWD) 


# Går ind i mappen sort, og så ind i mappen Result og indlæser
# tekstfilen som ligger der.
for filename in glob.glob(PATH+'/sort/Result/*.txt'):
    with open(filename, 'r', encoding="utf8") as f:
        READ_TEXT = f.read()



# Gemmer en generisk besked i variablen FUNK_GUIDE.
# Denne variable kan nu bruges i funktionerne.
FUNK_GUIDE = """
Her kan du søge på i absolut forlyd. Du har nu følgende valg; indtaster du:

1     Frisøgning
2     Frisøgning + Lydgruppe
3     Lydgruppe + Frisøgning

Ved både 2 og 3 kan du vælge at ikke indtaste noget sælg, bare vælge en lydgruppe.
"""


# Denne funktion bruges i alle de andre funktion.
# Den behandler og gemmer resultet fra de andre funktioner.
# Indholdet af argumentet "resultat" og "navn" defineres i de andre funktion.
def _make_file(result, navn):
    set_tekst = set(result)
    sorted_tekst = sorted(set_tekst, key=str.lower)
    nice_list = '\n\n'.join(sorted_tekst)
    ordliste = open(CWD+'/Result/'+navn+'_ordliste.txt', 'w', encoding='UTF8')
    ordliste.write("" + nice_list)
    ordliste.close()



# Denne funktion gør det muligt at søge på lyde i forlyd
def forlyd():
    # Printer FUNK_GUIDE
    print(FUNK_GUIDE)

    # Prompter brugeren til at træffe et valg.
    # Valget er beskrevet i FUNK_GUIDE
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
    
    # søger efter mønsteret i READ_TEXT, og ignorerer forskellem mellem store og små bogstaver.
    result = re.findall(pattern, READ_TEXT, re.IGNORECASE)

    navn = "forlyd"
    # Kalder funktionen _make_file(result, navn), og giver den resultat og navn.
    _make_file(result, navn)


def indlyd():
    print(FUNK_GUIDE)

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
    result = re.findall(pattern, READ_TEXT, re.IGNORECASE)
    navn = "indlyd"
    _make_file(result, navn)


def udlyd():
    print(FUNK_GUIDE)

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
    
    result = re.findall(pattern, READ_TEXT, re.IGNORECASE)
    navn = "udlyd"
    _make_file(result, navn)


def hel_ord():
    print(FUNK_GUIDE)

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
    result = re.findall(pattern, READ_TEXT, re.IGNORECASE)
    navn = "hel_ord"
    _make_file(result, navn)


# Det er her brugeren starter når scriptet køres.

print('''
Tast 1 for søgning i forlyd (absolut forlyd).
Tast 2 for søgning i indlyd.
Tast 3 for søgning i udlyd (absolut udlyd).
Tast 4 for søgning i det hele af ordene.

Søgningen vil finde alle ord der opfylder dine søgekriterier, og gemme disse ord i en seperat tekstfil.
''')

VALG = input("Indtast tal: ")

if VALG == "1":
    forlyd()
elif VALG == "2":
    indlyd()
elif VALG == "3":
    udlyd()
elif VALG == "4":
    hel_ord()
else:
    exit(0)

print("""
extractor.py     done running:

word_list.txt is ready in the Result directory.

Visit my GitHub at: https://github.com/NikolaiS1900
I can be contacted via: sandbecks_github@protonmail.com

Kind regards
- Nikolai Sandbeck
""")
