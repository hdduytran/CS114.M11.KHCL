from sys import stdin

x=[]

while 1:
    a = [int(i) for i in stdin.readline().split()]
    if (a[0]==0):
        x.insert(0,a[1])
    elif (a[0]==1):
        x.append(a[1])
    elif (a[0]==2):
        if(a[1] in x):
            x.insert(x.index(a[1])+1,a[2])
        else:
            x.insert(0,a[2])
    elif (a[0]==3):
        if a[1] in x:
            x.remove(a[1])
    elif (a[0]==4):
        while a[1] in x:
            x.remove(a[1])
    elif (a[0]==5):
        if len(x)!=0:
            x.pop(0)
    elif (a[0]==6):
        break
if len(x)==0:
    print("blank")
else:
    print(*x,sep=' ')