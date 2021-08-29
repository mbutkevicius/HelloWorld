parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[0])

print()

print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[0 - 14])

print(parrot[0:6])
print(parrot[3:5])
print(parrot[-14:-8])
print(parrot[-11:-9])

print()

print(parrot[0:9])
print(parrot[:9])
print(parrot[-14:-5])
print(parrot[:-5])

print()

print(parrot[10:14])
print(parrot[10:])
print(parrot[-4:-1])
print(parrot[-4:])

print()

print(parrot[:6])
print(parrot[6:])
print(parrot[:6] + parrot[6:])
print(parrot[:])

print(parrot[-4:-2])
print(parrot[-4:12])

print()

print(parrot[0:6:2]) #step of two is what the last line means
print(parrot[0:6:3])

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split() #this won't make sense yet
print([int(val) for val in values])