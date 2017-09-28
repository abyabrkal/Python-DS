#http://py4e-data.dr-chuck.net/known_by_Fikret.html
#Sequence of names: Fikret Montgomery Mhairade Butchi Anayah C4 P3
#http://py4e-data.dr-chuck.net/known_by_Wu.html C7 P18

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors for https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

todo = list()
url = input('Enter URL - ')
todo.append(url)

count = float(input('Enter count: '))
position = float(input('Enter position: '))

print('Retrieving:', url)

while len(todo) > 0 and count > 0 :
    url = todo.pop()
    count = count - 1

    try:
        html = urllib.request.urlopen(url, context=ctx).read()
    except:
        print("*** Error in retrieval")
        continue

    soup = BeautifulSoup(html, 'html.parser')
    

    # Retrieve all of the anchor tags
    pos = 0
    tags = soup('a')
    for tag in tags:
        newurl = tag.get('href', None)
        pos = pos + 1
        if (newurl is not None and pos == position):
            todo.append(newurl)
            print('Retrieving:', newurl)

str = todo[0]
lastName = str.split('_')[2].split('.')[0]
#print('Answer - ', lastName)
