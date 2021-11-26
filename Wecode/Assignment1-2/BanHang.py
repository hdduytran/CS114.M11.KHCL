from math import ceil

q = int(input())
for k in range(q):
    n = int(input())
    a =[int(x) for x in input().split()]
    res = ceil(sum(a)/n)
    print(res)