fname = input("Enter file name: ")
fh = open(fname)

fw = fh.read()

lst = list(fw.split())
lst.sort()
flst=[]

for i in lst:
    if i not in flst:
        flst.append(i)

print(flst)
