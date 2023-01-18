import pandas as pd
import re
dfList = []

with open("bom") as file:
    book = ""
    chapter = ""
    verseNum = -1
    verse = []
    for line in file:
        line = line.strip()
        if line:
            l = line.split()
            if "Chapter" in l:
                chapterIndex= l.index("Chapter")
                book = " ".join(l[:chapterIndex])
                print(book)
                chapter = l[chapterIndex+1]
                print(chapter)
            elif ":" in l[0]:
                #check chapter:
                chapAndVerse = l[0].split(":")
                if chapAndVerse[0].isdigit():
                    if chapAndVerse[0] != chapter:
                        print("Ya goofed!", line)
                    verseNum = chapAndVerse[1]
                    verse.extend(l[1:])
            else:
                verse.extend(l)

        else: #if the line is blank
            if verse:
                df2 = {'Book':book,
                'Chapter':chapter,
                'VerseNum':verseNum,
                'Verse': " ".join(verse)
                }
                dfList.append(df2)
            
            verse = []

df = pd.DataFrame(dfList)

clean_txt = []
for w in range(len(df)):
   desc = df['Verse'][w].lower()

   #remove punctuation
   desc = re.sub('[^a-zA-Z]', ' ', desc)

   #remove tags
   desc=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",desc)

   #remove digits and special chars
   desc=re.sub("(\\d|\\W)+"," ",desc)
   clean_txt.append(desc)

df['CleanedVerse'] = clean_txt
df = df.drop('Verse', axis=1)
df.to_csv("bomDF")