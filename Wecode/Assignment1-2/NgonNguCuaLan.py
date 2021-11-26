s = input().split()

def NN(s):
    a = ['lios','etr','initis','liala','etra','inites']
    for w in range(len(s)):
        check = False
        for i in range(6):
            if s[w].endswith(a[i]):
                s[w] = i
                check = True
                break
        if not check:
            return False
    if len(s)==1:
        return True
    if max(s)>2 and min(s)<3:
        return False
    if s!=sorted(s):
        return False
    s = list(filter(lambda t: t in [1,4],s))
    if len(s)==1:
        return True
    return False
print('YES' if NN(s) else 'NO')