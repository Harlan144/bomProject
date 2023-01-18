import pandas as pd
import re

df = pd.read_csv('bomDF')

inputSentance = input("What would you like to search?")
#remove punctuation
desc = re.sub('[^a-zA-Z]', ' ', inputSentance)

#remove tags
desc=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",desc)

#remove digits and special chars
desc=re.sub("(\\d|\\W)+"," ",desc)
tokens = desc.lower().split()

new_vector = model.infer_vector(tokens)

sims = model.dv.most_similar([new_vector]) #gives you top 10 document tags and their cosine similarity
print(sims)
verse = df.iloc[sims[1][0]]
print(verse)