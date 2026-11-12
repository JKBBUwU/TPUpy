a = 1
s =[]
a = list(input().split())
while a[0] != '0':
    d ={"name": a[0], "score": int(a[1]), "attempts": int(a[-1])}
    s.append(d)
    a = list(input().split())
ss = [i["name"] for i in s if i["score"]>=60 and i["attempts"] <=3]
n = []
for i in s:
    if i["score"]>=60 and i["attempts"] <=3:
        n.append(i["name"])
print("list compression")
print(ss)
print("append")
print(n)