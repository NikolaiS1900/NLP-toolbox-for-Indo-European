# Consonants
pl = '[pPbBtTdDkKgGcC]' #plosives
na = '[mMnN]' #nasales
tr = '[rR]' #trills
fr = '[fFvVþÞðÐsSzZcC]' #fricatives
ap = '[jJwW]' #approximants
la = '[lL]' #laterals
bl = '[pPbBmMwW]' #bilabials
ld = '[fFvV]' #labiodentals
dt = '[tTþÞdDdÐ]' #dentals
al = '[nNrRsSzZlL]' #alveolars and postalveolars
pa = '[jJ]' #palatals
ve = '[kKgG]' #velars
gl = '[hH]' #glottals


# Vowels
bv = '[aAoOuUáÁóÓúÚ]' #back vowels
fv = '[eEiIíÍyYýÝöÖ]' #front vowels

# Long vowels
lbv = '[áÁóÓúÚ]' #long back vowels
lfv = '[éÉíÍýÝ]' #long front vowels

# Short vowels
sbv = '[aAoOuU]' #short back vowels
sfv = '[eEiIyYöÖ]' #short front vowels

# Diphthongs
df = '[eiEIeyEYUauAUæÆ]' #short back vowels


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
    diphthongs = df
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

    if choice == 'df':
        RegEx = df

    else:
        pass

    return RegEx
