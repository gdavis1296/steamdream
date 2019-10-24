import json

def thing(dictonary, inputList, isRecommended):
    outFile = open('Text.csv', 'a')
    newInputList = []
    if count < 1:
        outFile.write(', ')
        outFile.write('isRecommended')
        outFile.write(', ')
        for key in dictonary:
            outFile.write(key)
            outFile.write(',')
        outFile.write('\n')
        
    inputList = inputList.split()
    
    for word in inputList:
        newInputList.append(word.lower())
    outFile.write("Review"+str(count))
    outFile.write(', ')
    outFile.write(str(isRecommended))
    #if (isRecommended == True):
    #    outFile.write('1')
    #else:
    #    outFile.write('0')
    outFile.write(', ')
    for word in dictonary:
        if word in newInputList:
            outFile.write('1')
        else:
            outFile.write('0')
        outFile.write(', ')
    outFile.write('\n')
    
    

BOW= {'thing':500,
      'where':40,
      'there':50,
      'support':50,
      'a':50,
      'for': 60,
      'are': 70,
      'trash': 80}

count = 0
data = {}

with open("sample_reviews.json") as json_reviews:
    for line in json_reviews.readlines():
        
        if count < 15:
            object = eval(line)
            thing(BOW, object['text'],object['recommended'])
            count+=1
            
        else:
            break

