n = int(input())
k = int(input())
a = int(input())
b = int(input())
if k > n:
    print(-1)
if (k%2==0):
  c=b
else:
  if (b == 1):
    c = 2
  elif(b == 2):
    c = 1
d = (a - 1) * 2 + (b - 1)
if d-k>=0:
  print((d-k)//2+1,c)
elif d+k<=n-1:
  print((d+k)//2+1,c)
else:
  print(-1)