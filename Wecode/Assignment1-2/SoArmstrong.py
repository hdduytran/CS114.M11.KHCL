a = int(input())
if a ==0:
    a = 1
x = a
from math import log10

n = int(log10(x)) + 1
s = 0
while (x>0):
    d = x%10
    s+= d**n
    x = x// 10
if s == a:
    print(True)
else:
    print(False)