from math import ceil

n,m,a = map(int,input().split())
n = ceil(n/a)
m = ceil(m/a)

print(n*m)