s = input().strip()
n = int(input())
count = len(s)

while s != '':
    if count <= n:
        print(s)
        break
    for i in reversed(range(n)):
        if s[n] != ' ':      
            if s[i] == ' ':
                print(s[:i+1])
                s = s[i+1:]
                count -= (i+1)
                break

            elif i == 0:
                if ' ' not in s[n:]:
                    print(s)
                    s = ''
                    break
                else:
                    j = s.index(' ',n)
                    print(s[:j+1])
                    s = s[j+1:]
                    count -= (j+1)
                if s[0] == ' ':
                    s = s[1:]
                    count += 1  
        else:
            print(s[:n])
            s = s[n:]
            count -= (n )
            break
