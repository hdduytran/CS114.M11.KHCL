n,m = input().split()
if m == n:
    print(1)
else:
    x = len(m) - len(n)
    if x == 0:
        print(1)
    else:
        res = int(m[:x])
        if m[x:] >= n:
            res += 1
        print(res)