# Consonants
pl = '[pPbBtTdDkKgGquQU]' #plosives
na = '[mMnN]' #nasales
tr = '[rR]' #trills
fr = '[fFvVþÞðÐsSzZ]' #fricatives
ap = '[jJwWiIuU]' #approximants
la = '[lL]' #laterals
bl = '[pPbBmM]' #bilabials
ld = '[fFvV]' #labiodentals
dt = '[tTdD]' #dentals
al = '[nNrRsSzZlL]' #alveolars and postalveolars
pa = '[jJiI]' #palatals
ve = '[kKgGquQU]' #velars
gl = '[hH]' #glottals


# Vowels
bv = '[aAoOuUāĀōŌūŪ]' #back vowels
fv = '[eEiIēĒīĪyYȳȲ]' #front vowels

# Only long vowels
lbv = '[āĀōŌūŪ]' #long back vowels
lfv = '[ēĒīĪȳȲ]' # long front vowels

# Only short vowels
sbv = '[aAoOuU]' #short back vowels
sfv = '[eEiIyY]' #short front vowels

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

    if choice == 'gl':
        RegEx = gl

    if choice == 'bv':
        RegEx = bv

    if choice == 'fv':
        RegEx = fv

    if choice == 'lbv':
        RegEx = lbv

    if choice == 'lfv':
        RegEx = lfv

    if choice == 'sbv':
        RegEx = sbv

    if choice == 'sfv':
        RegEx = sfv

    else:
        pass

    return RegEx
