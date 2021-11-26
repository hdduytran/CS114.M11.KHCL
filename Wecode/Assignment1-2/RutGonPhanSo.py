from math import gcd
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    c = gcd(a,b)
    a//=c
    b//=c
    if b==1:
        print(a)
    else:
        print(a,b)
