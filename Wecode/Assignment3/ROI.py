h,w = map(int,input().split())
a = []
for i in range(h):
    a.append(list(map(int,input().split())))
t,l,b,r = map(int,input().split())
x = [[0 for j in range(w)] for j in range(h)]
for i in range(t,b+1):
    x[i][l:r+1]=a[i][l:r+1]
for i in range(h):
	print(' '.join(map(str,x[i])))