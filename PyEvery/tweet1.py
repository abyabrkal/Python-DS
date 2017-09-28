import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
if len(url) < 1: print('Invalid link')

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
print('Count: ', len(info))

sum = 0
for item in info["comments"]:
    sum = sum + float(item['count'])

print('Sum: ', sum)