l = [0, 1, 2, 3, 4, 5]
k = tuple(l)
print(type(l), type(k))
print(id(l), id(k))
l [2] = 22
k2 = tuple(l)
print(id(l), id(k2))
