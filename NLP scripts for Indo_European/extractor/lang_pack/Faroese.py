# Consonants
pl = '[pPbBtTdDkKgGcC]' #plosives
na = '[mMnN]' #nasales
tr = '[rR]' #trills
fr = '[fFvVðÐsSzZcC]' #fricatives
ap = '[jJwW]' #approximants
la = '[lL]' #laterals
bl = '[pPbBmMwW]' #bilabials
ld = '[fFvV]' #labiodentals
dt = '[tTdDðÐ]' #dentals
al = '[nNrRsSzZlL]' #alveolars and postalveolars
pa = '[jJ]' #palatals
ve = '[kKgG]' #velars
gl = '[hH]' #glottals


# Vowels (historic value)
bv = '[aAoOuUáÁóÓúÚ]' #back vowels
fv = '[eEiIíÍyYýÝøØæÆ]' #front vowels

# Historic long vowels
lbv = '[áÁóÓúÚ]' #historic long back vowels
lfv = '[éÉíÍýÝ]' #historic long front vowels

# Historic short vowels
sbv = '[aAoOuU]' #historic short back vowels
sfv = '[eEiIyYæÆøØ]' #historic short front vowels

# Diphthongs
df = '[eiEIoyOYUeyEY]' #historic short back vowels


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
    long back vowels (historic value) = lbv
    long front vowels (historic value) = lfv
    short back vowels (historic value) = sbv
    short front vowels (historic value) = sfv
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
