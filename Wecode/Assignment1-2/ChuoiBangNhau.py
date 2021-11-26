import re
n = int(input())
for i in range(n):
    s = input()
    print('YES' if re.search(f'[{s}]',input()) else 'NO')
