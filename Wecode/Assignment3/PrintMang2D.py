r, c = map(int, input().split())
m = [list(map(str, list(map(int, input().strip().split())))) for _ in range(r)]


ml = [0 for _ in range(c)]
for i in range(c):
    for j in range(r):
        if len(m[j][i]) > ml[i]:
            ml[i] = len(m[j][i])

for i in range(c):
    for j in range(r):
        m[j][i] = ' '*(ml[i] - len(m[j][i])) + m[j][i]

for i in m:
    print(*i)