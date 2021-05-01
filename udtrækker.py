import os
import re

cwd = os.getcwd()

# Åbner filen tekst.txt i r (read mode)
tekst = open(str(cwd)+'/tekst.txt', 'r')

# Læser variablen "tekst"
read_tekst = tekst.read()

print('''Ud fra tallene, kan du vælge hvilket ord du vil søge efter.
1. søg på begyndelsen af ord (forlyd).
2. søg inde i ord (indlyd).
3. søg på endelsen af ord (udlyd).

Søgningen vil finde alle ord der opfylder dine søgekriterier, og gemme disse ord i en seperat tekstfil.
''')


def start():

    valg = input("vælg funktion: ")

    if valg == "1":
        forlyd()
    elif valg == "2":
        indlyd()
    elif valg == "3":
        udlyd()
    else:
        exit(0)


def forlyd():
	#Danner ordlisten forlyd_ordliste.txt i w (write mode)
	forlyd_ordliste = open(str(cwd)+'/forlyd_ordliste.txt', 'w')

	# Spørger brugeren hvad ordene skal ende med, og tilføjer det til variablen "indput"
	indput = input("hvad skal ordene begynde med?: ")

	# bruger RegEX. w* som betyder "nul eller flere bogstaver" og så siger +indput, som tilføjer variablen indput.
	pattern = indput+"\w*"

	# Finder alle eksempler på det indput der er givet.
	result = re.findall(pattern, read_tekst)

	#sortere alle dubletter fra
	set_tekst = set(result)

	# Opstiller alle ordene i alfabetisk rækkefølge, uden at skelne mellem store og små bogstaver. Den laver dog teksten om til en liste
	sorted_tekst = sorted(set_tekst, key=str.lower)

	# Konverterer teksten tilbage til en streng
	repr_tekst = repr(sorted_tekst)

	# opstiller alle ordene på en liste med dobbeltlinjeafstand.
	liste = repr_tekst.replace(', ', '\n \n') 

	# nu skrives variablen "liste" til ordliste.txt
	forlyd_ordliste.write("" + liste)

	tekst.close() #lukker tekst
	forlyd_ordliste.close() #lukker ordliste


def indlyd():
	indlyd_ordliste = open(str(cwd)+'/indlyd_ordliste.txt', 'w')

	indput = input("hvad skal ordene indholde?: ")

	pattern = "\w*"+indput+"\w*"

	result = re.findall(pattern, read_tekst)

	set_tekst = set(result)

	sorted_tekst = sorted(set_tekst, key=str.lower)

	repr_tekst = repr(sorted_tekst)

	liste = repr_tekst.replace(', ', '\n \n') 

	indlyd_ordliste.write("" + liste)

	tekst.close()
	indlyd_ordliste.close()


def udlyd():
	udlyd_ordliste = open(str(cwd)+'/udlyd_ordliste.txt', 'w')

	indput = input("hvad skal ordene ende med?: ")

	pattern = "\w*"+indput

	result = re.findall(pattern, read_tekst)

	set_tekst = set(result)

	sorted_tekst = sorted(set_tekst, key=str.lower)

	repr_tekst = repr(sorted_tekst)

	liste = repr_tekst.replace(', ', '\n \n') 

	udlyd_ordliste.write("" + liste)

	tekst.close()
	udlyd_ordliste.close()



start()
