#ex_09_04.py

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
biggestmail= None
biggestcount= None
mails=list()

for line in handle:
    if line.startswith('From: '):
        x = line.split()
        mails.append(x[1])

counts=dict()

for eachmail in mails:
    counts[eachmail] = counts.get(eachmail, 0) + 1

for i,j in counts.items():
    if biggestcount is None or j>biggestcount:
        biggestcount = j
        biggestmail=i

print(biggestmail, biggestcount)
