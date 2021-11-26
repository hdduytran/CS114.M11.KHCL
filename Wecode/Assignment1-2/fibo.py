n = int(input())
if n not in range(1,31):
    print(f'So {n} khong nam trong khoang [1,30].')
else:
    a = 1
    b = 1
    for i in range(n-2):
        temp = b
        b+= a
        a = temp
    print(b)