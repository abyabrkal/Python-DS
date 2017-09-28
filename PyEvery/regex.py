import re

hand = open('./regex.txt')
num = list()

for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) == 0: continue
    for item in stuff:
      num.append(float(item))

print(sum(num))