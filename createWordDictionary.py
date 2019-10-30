import nltk
import io
import sys
import json

wordfreq = {}

if len(sys.argv) == 3:
    print(sys.argv[1])
    input_file = open(sys.argv[1], 'r')
    input = json.load(input_file)
    corpus_file = open(sys.argv[2], 'r')
    corpus = json.load(corpus_file)
else:
    sys.exit("Usage:  python createWordDictionary.py <json for data> <json for corpus>")

for c in corpus:
    wordfreq[c] = 0
i = 0
for line in input:
##
##    print("")
    i += 1
    print(i)

    l = str(line).split(" ")

##    print(str(l) + "\n")

    for w in l:
        a = ''.join(filter(str.isalnum, w)).lower()
##        print(str(a))
        
##        print("Did we get here?")
    
        for t in wordfreq:
            if(t == a):
                wordfreq[t] += 1
##                print("Item is in wordfreq: ")
##                print(t)
                break;

        
            
##
##for i, j in wordfreq.items():
##    print((str(i) + ": " + str(j)))
##
x=0
for a in wordfreq:
    if wordfreq[a] != 0:
        x += 1
        print(x)
        print(a + ": " + str(wordfreq[a]))


with open('word-dictionary.json', 'w') as f:
    json.dump(wordfreq, f, ensure_ascii=False, indent=2)
    

##def wordcount(wordfromreview):
##    print("Did we get here?")
##    for t in range(0,len(wordfreq)):
##        if(wordfreq[t] == a):
##           print("Item is in wordfreq")
##        else:
##           print("Item is not in wordfreq")
