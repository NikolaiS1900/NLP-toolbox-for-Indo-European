import os

cwd = os.getcwd() #finder current working director, altså stien som scriptet ligger i


tekst = open(str(cwd)+'/tekst.txt', 'r') #tager stien og laver det om til en streng og tilføjer det til strengen /tekst.txt, så har vi filen på stien og så bliver filen åbnet i read-mode.
ordliste = open(str(cwd)+'/ordliste.txt', 'w') #Laver en ny tekst ved navn "ordliste.txt" og kører den i write-mode, og overskriver hvis der er en i forvejen af samme navn og filtype.

read_tekst = tekst.read() 

split_tekst = read_tekst.split() #indeler tekstens ord
set_tekst = set(split_tekst) #sortere alle dubletter fra
sorted_tekst = sorted(set_tekst, key=str.lower) #opstiller alt i alfabetisk rækkefølge. key=str.lower()  gør at store og småbogstaver behandles ens, uden at store bogstaver bliver gjort til småbogstaver.
repr_tekst = repr(sorted_tekst) #den laver listen om til en streng, der kan tillægges ordliste.txt.
liste = repr_tekst.replace(', ', '\n \n') #erstatter hvert tilfælde af (, ) fra variablen repr_tekst med dobbelt linjeskift.


ordliste.write("" + liste) #Nu bliver variablen "liste" tilføjet til ordliste.txt som gemmes som ordliste.txt i mappen

tekst.close() #lukker tekst
ordliste.close() #lukker ordliste

print("""Din ordliste er klar 😃

Hav en god dag
-Nikolai Sandbeck """)
