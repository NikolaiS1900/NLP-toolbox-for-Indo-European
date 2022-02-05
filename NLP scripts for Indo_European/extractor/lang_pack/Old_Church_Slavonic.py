# Consonants
pl = '[pPbBtTdDkKgG]' #plosives
na = "[mMnNn'N'ńŃ]" #nasales
tr = '[rR]' #trills
af = '[čČtsTSdzDZ]' #affricatives
fr = '[fFvVþÞðÐsSzZžŽšŠdŽDštŠTxXchCH]' #fricatives
ap = '[jJwW]' #approximants
la = '[lL]' #laterals
bl = '[pPbBmM]' #bilabials
ld = '[fFvV]' #labiodentals
dt = '[tTdDtsTSdzDZ]' #dentals
al = '[nNrRsSzZlLžŽšŠ]' #alveolars and postalveolars
pa = "[jJr'R'l'L'čČŕŔ]" #palatals
ve = '[kKgGxX]' #velars


# Vowels
bv = '[yYъЪaAuUoOǫǪ]' #back vowels
fv = '[iIьЬeEěĚęĘ]' #front vowels

# Nasal vowels
nbv = '[ǫǪ]' # long back vowels
nfv = '[ęĘ]' # long front vowels


# IPA character pickers
# https://schwa.dk/filer/ipacharpick/
# https://r12a.github.io/pickers/ipa/

# Dania tegnvælger
# http://schwa.dk/filer/daniategnvaelger/


def Sounds():
    print("""
    plosives = pl
    nasals = na
    trills = tr
    affricatives = af
    fricatives = fr
    approximants = ap
    laterals = la
    bilabials = bl
    labiodentals = ld
    dentals = dt
    alveolars and postalveolars = al
    palatals = pa
    velars = ve
    back vowels = bv
    front vowels = fv
    nasal back vowels = nbv
    nasal front vowels = nfv

""")


    choice = input('What sounds?: ').lower()
    if choice == 'pl':
        RegEx = pl

    if choice == 'na':
        RegEx = na

    if choice == 'tr':
        RegEx = tr

    if choice == 'af':
        RegEx = af

    if choice == 'fr':
        RegEx = fr

    if choice == 'ap':
        RegEx = ap

    if choice == 'la':
        RegEx = la

    if choice == 'bl':
        RegEx = bl

    if choice == 'ld':
        RegEx = ld

    if choice == 'dt':
        RegEx = dt

    if choice == 'al':
        RegEx = al

    if choice == 'pa':
        RegEx = pa

    if choice == 've':
        RegEx = ve

    if choice == 'bv':
        RegEx = bv

    if choice == 'fv':
        RegEx = fv

    if choice == 'nbv':
        RegEx = nbv

    if choice == 'nfv':
        RegEx = nfv

    else:
        pass

    return RegEx
