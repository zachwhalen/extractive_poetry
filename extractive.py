# imports
import random
import re
from textblob import TextBlob
import nltk
nltk.download('punkt')


# open the file
with open("/content/time.txt") as f:
  text = f.read()

# blobify it
blob = TextBlob(text)

# get a list of sentences
sentences = blob.sentences

# create an empty list to store sentences starting with pronouns
pro_sents = []

for s in sentences:
  if (len(s.words) > 0):
    if (s.words[0] in ["She","He","They","We","It"]):
      pro_sents.append(s)

# pick a random word for the title
title = random.choice(blob.words)

# print that title word in all caps
print("\n\n\n" + title.upper() + ", a poem. \n")

# get a list of sentences shorter than some specified length
short_sentences = []
for ps in pro_sents:
  if (len(ps.words) < 4):
    short_sentences.append(ps)


# shuffle those sentences
random.shuffle(short_sentences)

for s in short_sentences:
  # remove linebreaks
  s = s.replace("\n",' ')
  print(s)
