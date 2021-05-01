import os

cwd = os.getcwd()


tekst = open(str(cwd)+'/tekst.txt', 'r')
tegnliste = open(str(cwd)+'/tegnliste.txt', 'w')

read_tekst = tekst.read()
set_tekst = set(read_tekst)
sorted_set = sorted(set_tekst, key=str.lower)
remove_first = sorted_set[1:] #Fjerner første linje i listen sorted_set, for at undgå forvirring
repr_tekst = repr(remove_first)
liste1 = repr_tekst.replace(', ', '\n \n')
liste2 = liste1.replace("'", "") #fjerner alle tilfælde af ' i listen, også dem som forekommer i teksten, dvs også "'" som så bliver til ""
liste3 = liste2.replace('""', "'") # tager "" og genindsætter det ' som faktisk findes i teksten.

tegnliste.write("" + liste3)

tekst.close() 
tegnliste.close() 

print("""Din tegnliste er klar 😃

Hav en god dag
-Nikolai Sandbeck """)
