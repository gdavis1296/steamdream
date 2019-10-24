import json

def thing(dictonary, inputList):
    outFile = open('Text.csv', 'a')
    newInputList = []
    i=0
    inputList = inputList.split()
    for word in inputList:
        newInputList.append(word.lower())
    for word in newInputList:
        if word in dictonary:
            outFile.write('1')
        else:
            outFile.write('0')
        outFile.write(', ')
    outFile.write('\n')
    i+=1
    

BOW= {'thing':500,
      'where':40,
      'there':50}


count = 0
data = {}

with open("sample_reviews.json") as json_reviews:
    for line in json_reviews.readlines():
        if count < 15:
            object = eval(line)
            #print(object['text'])
            thing(BOW, object['text'])
            count+=1
        else:
            break
