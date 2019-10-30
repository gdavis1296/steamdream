import nltk
import io
import sys
import json
from nltk.corpus import stopwords

#desc: This program is made to take in a list of steam reviews, extract the reviews and tokenize the strings to get a list of every word in all the reviews.
#from there, the program will make a dictionary from the list of words to get a wordcount dictionary.

#To Execute: in the same directory as this script along with the json file that contains steam reviews, run the following in command prompt (for windows)
#   'python createWordDictionary.py <json file>'

if len(sys.argv) == 2:
    print(sys.argv[1])
    input_file = open(sys.argv[1], 'r')
    input = json.load(input_file)
else:
    sys.exit("Usage:  python createWordDictionary.py <json file>")

i = 0
corpus = []
for line in input:
    b = line.index("u'text': u")
    if ", u'hours': " not in line:
        e = line.index(", u'recommended': False")
    else:
        e = line.index(", u'hours': ")
    
    review = line[b+11:e-2].split()
##    for w in review:
####        print("the word isssssssssssssssss " + w)
##        a = ''.join(filter(str.isalnum, w)).lower()
##        if a not in corpus:
####            print(a)
##            if a != '': 
##                corpus.append(a)
                
    i = i+1
    if(i % 10 == 0):
        print(i)

##print("woof")
##filtered_words = [word for word in corpus if word not in stopwords.words('english')]

print("meow")
with open('Unique_Words-sample-data(1).json', 'w') as f:
    json.dump(filtered_words, f, ensure_ascii=False, indent=2)



