x = {}

while(1):
    try:
        a, b = map(int, input().split())
    except:
        break
    if a == 1:
        x[b] = 1
    elif a == 2:
        if b not in x:
            print(0)
        else:
            print(1)