amigos = ['Jose', 'Juan', 'Maria', 'Alvaro']

print(len(amigos))
print(range(5))

for i in amigos:
    print(i)

print()

for i in range(len(amigos)):
    amigo = amigos[i]
    print(i+1, amigo)

x = 'Jose' in amigos
print(x)

amigos.sort()
print(amigos)
