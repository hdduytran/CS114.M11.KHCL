n = int(input())
a = [int(x) for x in input().split()]
k,x = map(int,input().split())

b = [abs(i-x) for i in a]
a = [i for _,i in sorted(zip(b,a))]
a = sorted(a[:k])
print(*a,sep=' ')