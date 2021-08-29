
for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()

print("Pi is approximately {0:12}".format(22/7))    #Default format prints 15 decimals
print("Pi is approximately {0:12f}".format(22/7))   #(f = floating point) prints 6 digits after decimal point
print("Pi is approximately {0:12.50f}".format(22/7))#Ignores the field width of 12 because the 50 floating point is larger
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:72.50f}".format(22/7))
print("Pi is approximately {0:0.02f}".format(22/7))
print("Pi is approximately {0:1.02f}".format(22/7))
print("Pi is approximately {0:5.02f}".format(22/7))