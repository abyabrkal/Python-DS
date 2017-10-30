#read titanic csv
import csv

with open('Titanic.csv', 'r') as csvfile:
    read = csv.reader(csvfile)
    for row in read:
        print(row)
        pclass = row[2]
        age = row[3]
        sex = row[4]
        survived = row[6]
        name = row[1]
        #fname = 
        #lname = 
        print(pclass+'/'+age+'/'+sex+'/'+survived+'/'+name)

        
        #print(' '.join(row))