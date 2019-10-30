import nltk
import io
import sys
import json
from collections import OrderedDict
from operator import itemgetter    

if len(sys.argv) == 2:
    print(sys.argv[1])
    input_file = open(sys.argv[1], 'r')
    input = json.load(input_file)
else:
    sys.exit("Usage:  python createWordDictionary.py <json file>")

result = OrderedDict(sorted(input.items(), key = itemgetter(1), reverse = True))
with open('ordered-word-dictionary.json', 'w') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
