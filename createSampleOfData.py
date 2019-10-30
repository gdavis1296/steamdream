#!/usr/bin/python
import sys
import random
import io
import json

#Ensure that the value you input when running this program is double of what you would like in each set.
#Half of the input size will be put into test-data.json and the other half will be placed into sample-data.json
#to ensure the reviews were all unique.

#To use inside the directory containing the data set:
# type 'python createSampleOfData.py (DESIRED NUM OF REVIEWS) steam_reviews.json


if len(sys.argv) == 3:
    input = open(sys.argv[2],'r')
elif len(sys.argv) == 2:
    input = sys.stdin;
else:
    sys.exit("Usage:  python samplen.py <lines> <?file>")
 
N = int(sys.argv[1]);
sample = [];
test = [];

 
for i,line in enumerate(input):
    if i < N:
        if i % 2 == 0:
            test.append(line)
        else:
            sample.append(line)
    elif i >= N and random.random() < N/float(i+1):
        if i % 2 == 0:
            replace = random.randint(0,len(sample)-1)
            sample[replace] = line
        else:
            replace = random.randint(0,len(sample)-1)
            test[replace] = line
 
for line in sample:
    sys.stdout.write(line)
    sys.stdout.write("EOL")

with open('sample-data.json', 'w') as f:
    json.dump(sample, f, ensure_ascii=False, indent=2)
    
with open('test-data.json', 'w') as f:
    json.dump(test, f, ensure_ascii=False, indent=2)
