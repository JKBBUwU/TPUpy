s = input().split()
d1 = {x: len(x) for x in s}
d2 = {}
for i in s:
    d2[i] = len(i)
print(d1)
print("---------")
print(d2)