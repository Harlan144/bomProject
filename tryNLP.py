from gensim.models import word2vec, FastText
from gensim.models import Word2Vec

from gensim.models.doc2vec import Doc2Vec, TaggedDocument

from nltk.tokenize import word_tokenize

import pandas as pd
import re

from sklearn.decomposition import PCA

from matplotlib import pyplot as plt
import plotly.graph_objects as go

import numpy as np

import warnings
warnings.filterwarnings('ignore')


df = pd.read_csv("bomDF")

corpus = []
for verse in df["CleanedVerse"]:
   word_list = verse.split(" ")
   new_list = [x for x in word_list if x != '']

   corpus.append(new_list)

#show first value
print(len(df["CleanedVerse"]))
print(len(corpus))

#generate vectors from corpus


verses = [TaggedDocument(verse,[i]) for i, verse in enumerate(corpus)]
print(verses)
model = Doc2Vec(vector_size=300, min_count=2, epochs=20)
model.build_vocab(verses)

model.train(verses, total_examples=model.corpus_count, epochs=20)
model.save("d2v.model")

