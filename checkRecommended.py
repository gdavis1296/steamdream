import nltk
import io
import sys
import json

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
for line in input:
    if ", u'recommended': " in line:
        i = i+1
        print(i)
    
