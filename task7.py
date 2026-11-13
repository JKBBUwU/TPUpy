prod = list(input().split())
ammount = list(map(int, input().split()))
s = [i for i,n in zip(prod, ammount) if n < 10]
print(s)
