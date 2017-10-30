#read titanic csv


import csv
import sqlite3
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('titan.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Survivors
    (id INTEGER UNIQUE, fname TEXT, lname TEXT,
     pclass INTEGER, age INTEGER, sex TEXT, survived INTEGER)''')

with open('Titanic.csv', 'r') as csvfile:
    read = csv.reader(csvfile)
    for row in read:
        print(row)
        
        #print(' '.join(row))

