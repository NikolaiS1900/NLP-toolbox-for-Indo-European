import gensim, os, glob
from gensim import models
from path_finder import path_finder
import matplotlib.pyplot as plt

CWD = os.getcwd()
PATH = path_finder()

for filename in glob.glob(PATH+'/preprocess/preprocessed_text/*.txt'):
	with open(filename, 'r', encoding="utf8") as f:
		READ_TEXT = f.read()


# preprocess text
PREPROCESSED_TEXT = READ_TEXT.lower()

# list of list
PREPROCESSED_TEXT = [READ_TEXT.split()]

# train word embeddings model
MODEL = gensim.models.Word2Vec(PREPROCESSED_TEXT, vector_size=2, window=5, min_count=1, workers=2, sg=1)

WORD1 = MODEL.wv['kat'] # blue
WORD2 = MODEL.wv['kat'] # orange
WORD3 = MODEL.wv['kat'] # purple

print(f"vector of WORD1: {WORD1}")
print(f"vector of WORD2: {WORD2}")
print(f"vector of WORD3: {WORD3}")


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


plt.axis([-5, 5, -5, 5])
plt.show()
