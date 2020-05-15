import urllib.request as ur
import json

url = input('Enter location: ')
print('Retrieving', url)

file = ur.urlopen(url).read()
info = json.loads(file)
print('Retrieved', len(file), 'characters')

cantidad = int()
total = int()

for item in info['comments']:
    x= item['count']
    cantidad = cantidad + 1
    total = total + x

print('Count:', cantidad)
print('Sum:', total)
