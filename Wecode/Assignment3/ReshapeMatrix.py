n, m = map(int, input().split())
r, c = map(int, input().split())

a=[]
x = []
for i in range(0, n):
    a.append(list(map(int,input().strip().split())))
    x += a[i]

if n*m != r*c:
    for i in range(n):
        print(*a[i])
else:
    for i in range(r):
        for j in range(c):
            print(x[i*c + j], end=' ')
        print()