import pandas as pd
import re

df = pd.read_csv('bomDF')
book = input("What book? ")
chapter = input("What chapter? ")
verse = input("What verse? ")

if (book not in df['Book']):
    print("try again!")
index = df.index[(df['Book'] == book) & (df['Chapter'] == int(chapter)) & (df["VerseNum"]== int(verse))]
print(index[0])



similarVerses = []
if len(index)>0:
    with open("mostSimilarVerses1") as file:
        for i, line in enumerate(file):
            if i== index[0]:
                regex = '\'index\': (\d+)'
                similarVerses = re.findall(regex, line) 
                print(similarVerses)

for i in similarVerses:
    print(df.iloc[int(i)])
