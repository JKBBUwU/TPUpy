s = [i**2 for i in range(0, 101) if i%2 ==0]
ss = []
for i in range(0,101):
    if i%2==0:
        ss.append(i**2)
print((ss==s))