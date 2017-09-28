

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

total = 0
count = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

spans = soup('span')
for span in spans:
    #print('Contents:', span.contents[0])
    total = total + float(span.contents[0])
    count = count + 1

print('Count', count)
print('Sum', total)