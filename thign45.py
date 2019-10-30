import csv
import random
import sys

fid = open("steam_reviews.csv",'r',errors="replace")

li = fid.readlines()
fid.close()

random.shuffle(li)

fid = open("shuffle.csv", "w",errors="replace")
fid.writelines(li)
fid.close()
print('Finished shuffling')
###########################################################
outFile = open('recommended.csv', 'w')
outFile2 = open('not_recommended.csv', 'w')
with open("shuffle.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    count = 0
    recommended_count = 0
    not_recommended_count = 0
    for row in csv_reader:
        recommended = row[5]
        if (recommended == "Recommended" ):
            for item in row:
                outFile.write(item)
                outFile.write(',')
            outFile.write('\n')
        else:#if (recommended == "Not Recommended"):
            for item in row:
                outFile2.write(item)
                outFile2.write(',')
            outFile2.write('\n')
outFile.close()
outFile2.close()
print("Finished splitting out files")
############################################################
testing = open('testing.csv', 'w')
training = open('training.csv', 'w')

rec = open('recommended.csv','r')
not_rec = open('not_recommended.csv', 'r')

recline = rec.readlines()
notrecline = not_rec.readlines()
rec.close()
not_rec.close()

random.shuffle(recline)
random.shuffle(notrecline)

i=0
j=0
with open("recommended.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if (i < 5025):
            for item in row:
                testing.write(item)
                testing.write(',')
            testing.write('\n')
            i+=1
        elif (j < 3025):
            for item in row:
                training.write(item)
                training.write(',')
            training.write('\n')
            j+=1
            
with open("not_recommended.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if (i < 10025):
            for item in row:
                testing.write(item)
                testing.write(',')
            testing.write('\n')
            i+=1
        elif (j < 6025):
            for item in row:
                training.write(item)
                training.write(',')
            training.write('\n')
            j+=1

testing.close()
training.close()
print("finished adding data to files")

thing = open('testing.csv','r')
thing2 = open('training.csv','r')

testline = thing.readlines()
trainingline = thing2.readlines()
thing.close()
thing2.close()
random.shuffle(testline)
random.shuffle(trainingline)

