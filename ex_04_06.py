def computepay (h, r):
    if h <= 40:
        p = h*r
    else:
        p = ((h-40) * 1.5 + 40) * r
    return p

hours = input ("Enter hours: ")
rate = input ("Enter rate: ")
h = float (hours)
r = float (rate)

print ("Pay",computepay(h, r))
