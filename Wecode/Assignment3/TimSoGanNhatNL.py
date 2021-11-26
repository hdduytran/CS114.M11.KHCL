from sys import stdin
from bisect import bisect_left as bl


def input():
    return stdin.readline()


n = int(input())
a = [int(x) for x in input().split()]

while 1:
    t = input()
    if len(t) == 1:
        exit()
    k, x = map(int, t.split())
    i = bl(a, x, 0, len(a) - 1)
    l = max(0, i - k + 1)
    r = l + k - 1
    while (r + 1) < len(a) and a[r + 1] - x < x - a[l]:
        l += 1
        r += 1
    print(a[l], a[r])
