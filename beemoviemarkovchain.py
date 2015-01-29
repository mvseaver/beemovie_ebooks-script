from __future__ import with_statement
import random

filename = "beemoviescript.txt"
wordList = []
wordDictionary = {}

with open(filename) as f:
    for line in f:
        for i in range(len(line.split())):
            wordList.append(line.split()[i])

for i in range(len(wordList)):
    if wordList[i] not in wordDictionary:
        wordDictionary[wordList[i]] = []
    if i > 0:
        wordDictionary[wordList[i-1]].append(wordList[i])

uniqueWordList = wordDictionary.keys()

print wordDictionary

for i in range(100):
    word = random.choice(uniqueWordList)

    output = word

    while len(output) < 140:
        word = random.choice(wordDictionary[word])
        output = output + " " + word

    output = output[:140]

    print output
