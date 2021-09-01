import re

def tegnfjerner(tekst):
    set_tekst = set(tekst)
    sorted_set = sorted(set_tekst, key=str.lower)
    streng = ' '.join(sorted_set)
    tegn_set_bogstaver = 'a-zA-Z'
    tegn_set_tal = '0-9'
    tegn_ekstra = 'àÁäåæÆçéöøØýąđėęįķľņşťųсСуӕạụ'
    samlede_tengset = tegn_set_bogstaver+tegn_set_tal+tegn_ekstra
    rens = re.sub('['+samlede_tengset+']', '', streng)
    tegnliste = rens.split()

    for i in tekst:
        if '\\' not in tegnliste:
            tekst = re.sub('\\\\', '', tekst)
        if i in tegnliste:
            tekst = tekst.replace(i, '')
        else:
            pass

    return tekst
