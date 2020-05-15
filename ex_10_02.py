name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours=list()
counts=dict()
x=str()

# Comienzo a recorrer el archivo (handle).
# Cada línea que comienza con 'From ' la spliteo.
# La 5ta palabra del spliteo la adjunto a la lista hours.
for line in handle:
    if line.startswith('From '):
        words=line.split()
        x=words[5]
        hours.append(x[:2])

# Cargo en el dictionary counts cada hora con su cantidad de ocurrencias
for hour in hours:
    counts[hour]=counts.get(hour, 0) + 1

# Creo la lista temporal tmplst para cargarle las tuplas con hora y ocurrencias.
#Creo la tupla temporal tmptup que luego cargaré en tmplst
# con un for in .items voy anexando cada tupla que encuentro en counts a tmplst
tmplst=list()
tmptup=tuple()
for i,j in counts.items():
    tmptup=(i,j)
    tmplst.append(tmptup)

# Ordeno tmplst por horas de menor a mayor
tmplst=sorted(tmplst)

# Con un for in recorro tmplst y voy imprimiendo de la forma requerida
for i,j in tmplst:
    print (i, j)
