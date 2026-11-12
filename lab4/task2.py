names = list(input().split())
scores = list(map(int, input().split()))
for n,i in zip(names, scores):
    print(f'{n}: {i}')