fruit = 'banana'
index=0
while index < len(fruit):
  print (index,fruit[index])
  index= index+1

print()

fruit2 = 'apple'
for i in fruit2:
    print (i)

print ()

count = 0
for i in fruit2:
    if i == 'p':
        count = count + 1
print ('Cantidad de p en apple: ', count)

print()

print(fruit[3:6])

print()

'n' in fruit

print (dir(fruit))
