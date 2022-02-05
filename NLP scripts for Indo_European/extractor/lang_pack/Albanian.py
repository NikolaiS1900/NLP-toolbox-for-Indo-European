# Consonants
pl = '[pPbBtTdDkKgG]' #plosives
na = '[mMnNnjNJ]' #nasales
tr = '[rRrrRR]' #trills
fr = '[fFthTHdhDHcCxXsSzZçÇxhXHshSHzhZHhH]' #fricatives
ap = '[jJ]' #approximants
la = '[lLllLL]' #laterals
bl = '[pPbBmM]' #bilabials
ld = '[fFvV]' #labiodentals
dt = '[tTdthTHdhDH]' #dentals
al = '[nNrRsSzZlLcCxXsSzZrrRRçÇxhXHshSHzhZH]' #alveolars and postalveolars
pa = '[qQgjGJ]' #palatals
ve = '[kKgG]' #velars
gl = '[hH]' #glottals

# Vowels
bv = '[aAoOuU]' #back vowels
fv = '[eEiIyY]' #front vowels
schwa = '[ëË]' #schwa

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
    fricatives = fr
    approximants = ap
    laterals = la
    bilabials = bl
    labiodentals = ld
    dentals = dt
    alveolars and postalveolars = al
    palatals = pa
    velars = ve
    glottals = gl
    back vowels = bv
    front vowels = fv
    long back vowels = lbv
    long front vowels = lfv
    short back vowels = sbv
    short front vowels = sfv
""")


    choice = input('What sounds?: ').lower()
    if choice == 'pl':
        RegEx = pl

    if choice == 'na':
        RegEx = na

    if choice == 'tr':
        RegEx = tr

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

    if choice == 'gl':
        RegEx = gl

    if choice == 'schwa':
        RegEx = schwa

    else:
        pass

    return RegEx
