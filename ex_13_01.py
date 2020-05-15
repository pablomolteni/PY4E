import urllib.request as ur
import xml.etree.ElementTree as ET

url = input('Enter location: ')
print('Retrieving', url)

file = ur.urlopen(url).read()
print('Retrieved', len(url), 'characters')

tree = ET.fromstring(file)

counts = tree.findall('.//count')

cantidad = 0
total = 0

for count in counts:
    total = int(count.text) + total
    # total = count + total
    cantidad = cantidad + 1

print('Count:', cantidad)
print('Sum:', total)
