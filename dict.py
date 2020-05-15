f = open('romeo.txt')
h = f.read()

counts = dict()
biggestword = None
biggestcount = None

print(h)
print()

lines = list()
words = list()

for i in h:
    words = h.split()

print('lines', lines)
print('words', words)
print()

for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)
print()

for i,j in counts.items():
    if biggestcount is None or j>biggestcount:
        biggestword = i
        biggestcount = j
    print(i, j)
print()

print(biggestword, biggestcount)
