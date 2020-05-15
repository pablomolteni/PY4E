# Input de las horas trabajadas. Luego lo convierto a float.
# Para testear utilizar 45 horas
hrs = input("Enter Hours:")
h = float(hrs)

# Input del rate per hour. Luego lo convierto a float.
# para testear utilizar 10.50
rph = input("Enter rate per hour:")
r = float(rph)

if h <= 40:
    p = h*r
else:
    p = ((h-40) * 1.5 + 40) * r
print(p)
