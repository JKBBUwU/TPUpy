l = [0, 1, 2, 3, 4, 5]
k = set(l)
print(type(l), type(k))
print(id(l), id(k))
l [2] = 22
k2 = set(l)
print(id(l), id(k2))