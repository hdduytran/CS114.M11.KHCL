from sys import stdin

x = set()

while(1):
    try:
        a, b = map(int, stdin.readline().split())
    except:
        break
    if a == 1:
        x.add(b)
    elif a == 2:
        if b not in x:
            print(0)
        else:
            print(1)
    elif b in x:
        x.remove(b)