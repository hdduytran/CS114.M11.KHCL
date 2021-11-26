n,m,c = map(int,input().split())
board = []
for i in range(n):
    board.append(list(input()))
move = list(input())

h = [(-1,0),(0,1),(1,0),(0,-1)]
#Find head
head = None
for i in range(n):
    for j in range(m):
        if board[i][j] in '<^>v':
            head=(i,j)
            break
    if head != None:
        break

#define snake
snake = []
cx,cy = head
status = '^>v<'.index(board[cx][cy])
snake.append((cx,cy))
conti = True


while conti:
    conti = False
    for x,y in h:
        nx,ny = cx+x,cy+y
        if nx<0 or nx> n-1 or ny<0 or ny>m-1:
            continue
        if board[nx][ny] == '*' and (nx,ny) not in snake:
            snake.append((nx,ny))
            cx,cy=nx,ny
            conti = True
snake.reverse()

#print snake
def print_snake(live):
    if live:
        for i in range(n):
            for j in range(m):
                if (i,j) in snake:
                    if (i,j) == snake[-1]:
                        print('^>v<'[status],end='')
                    else:
                        print('*',end='')
                else:
                    print('.',end='')
            print()
    else:
        for i in range(n):
            for j in range(m):
                if (i,j) in snake:
                    print('X',end='')
                else:
                    print('.',end='')
            print()

def go(status,dir):
    return (status+dir)%4

live = True
for mo in move:
    cx,cy = head
    if mo=='R':
        status = go(status,1)
        continue
    elif mo=='L':
        status = go(status,-1)
        continue
    nx,ny = h[status]
    nx,ny = cx+nx,ny+cy
    if (nx,ny) in snake and (nx,ny)!=snake[0] or nx<0 or nx> n-1 or ny<0 or ny>m-1:
        live = False
        break
    else:
        snake.pop(0)
        snake.append((nx,ny))
        head=((nx,ny))

    if not live:
        break

print_snake(live)
