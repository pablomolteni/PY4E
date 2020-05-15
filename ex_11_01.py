name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_42.txt"
handle = open(name)

import re

# totalsum=int()
# for line in handle:
#     line=line.rstrip()
#     words=line.strip()
#     for word in words:
#         numeros=re.findall('[0-9]+',word)
#         print(numeros)

        # totalsum = totalsum + int(numeros)

numeros=re.findall('[0-9]+', handle.read())

print(numeros)
totalsum=int()
for numero in numeros:
    # if numero is not None:
        totalsum=totalsum+int(numero)

print(totalsum)
