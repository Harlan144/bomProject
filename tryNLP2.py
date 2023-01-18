from sentence_transformers import SentenceTransformer, util
import pandas as pd
import re
import numpy as np
import torch

df = pd.read_csv("bomDF")
model = SentenceTransformer('all-MiniLM-L6-v2')

verses = df['CleanedVerse']

#Sentences are encoded by calling model.encode()
embeddings = model.encode(verses, convert_to_tensor=True)

#Print the embeddings
# cosine_scores = util.cos_sim(embeddings, embeddings)
# print(len(cosine_scores))
# versePairs = []

print("Writing to file...")

# with open("mostSimilarVerses","w") as outFile:
#     for i in range(len(cosine_scores)):
#         print(i)
#         pairs = []
#         for j in range(len(cosine_scores)):
#             if j!=i:
#                 pairs.append({'index': j, 'score': cosine_scores[i][j]})
                
#         pairs = sorted(pairs, key=lambda x: x['score'], reverse=True)
#         versePairs.append({i:pairs[0:5]}) 
    
#     for i in versePairs:
#         outFile.write(str(i) +"\n")



torch.save(embeddings, 'tensor.pt')

# with open("verseWithEmbeddings", "w") as outFile:
#     for i, embedding in enumerate(embeddings):
#         outFile.write(f"{i}: {embedding}"+"\n")
