s = list(input().split())
for i in range(len(s)):
    print(f"{i+1}: {s[i]}")
print("Enumerate:")
for i,n in enumerate(s):
    print(f"{i+1}: {n}")