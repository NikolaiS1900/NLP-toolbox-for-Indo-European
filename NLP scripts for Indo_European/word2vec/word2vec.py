import gensim, os, glob
from gensim import models
import matplotlib.pyplot as plt

CWD = os.getcwd()
# Går i overmappen.
PATH = os.path.dirname(CWD) 

# Går til mappen preprocess og så videre ned i preprocessed_text, og tager teksfilen
# der ligger der, og læser den ind.
for filename in glob.glob(PATH+'/preprocess/preprocessed_text/*.txt'):
	with open(filename, 'r', encoding="utf8") as f:
		READ_TEXT = f.read()


# Gør alle bogstaver små
#LOWER_CASE = READ_TEXT.lower()

# Moddellen Word2Vec skal bruge en liste af lister.
LIST_OF_LISTS = [READ_TEXT.split()]

# Kører moddellen. Husk at window størrelsen kan justeres.
# Hvis den er sat til 3, vil hvert ords vektorværdi blive påvirket af de næste tre ord frem og de forrige tre ord tilbage.
MODEL = gensim.models.Word2Vec(LIST_OF_LISTS, vector_size=2, window=3, min_count=0, workers=2, sg=1)

# Her kan man skrive hvilken værdi ens variabler skal have.
WORD_1 = 'bonde' # blue
WORD_2 = 'konung' # orange
WORD_3 = 'man' # purple

WORD1 = MODEL.wv[WORD_1] # blå
WORD2 = MODEL.wv[WORD_2] # orange
WORD3 = MODEL.wv[WORD_3] # lilla

# Gør et label til x-aksen klar.
XLABEL = f"""
vector of {WORD_1} (blue arrow): {WORD1}\n
vector of {WORD_2} (orange arrow): {WORD2}\n
vector of {WORD_3} (purple arrow): {WORD3}
"""

## plot vectors
## comment to deactive and uncomment to deactive

# WORD1
try:
  plt.arrow(0, 0, WORD1[0], WORD1[1], width=0.03, color='blue') # WORD1
except:
  pass

# WORD2
try:
  plt.arrow(0, 0, WORD2[0], WORD2[1], width=0.03, color='orange') # WORD2
except:
  pass

# WORD3
try:
  plt.arrow(0, 0, WORD3[0], WORD3[1], width=0.03, color='purple') # WORD3
except:
  pass

plt.xlabel(XLABEL)
plt.axis([-5, 5, -5, 5])
plt.show()
