x,y = map(int,(input().split()))
for i in range(0,x+1):
    a = i
    b = x-a
    if a*2 + b*4 == y:
        print(a,b)
        break