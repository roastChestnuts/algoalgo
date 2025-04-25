import sys

input = sys.stdin.readline

N, M = map(int, input().split())
x, y, d = map(int, input().split())

#0(북)1(동)2(남)3(서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[False]*M for _ in range(N)]

room = []
result = 0

for i in range(N):
    room.append(list(map(int, input().split())))

while True:
    if visited[x][y] == False and room[x][y] == 0:
        result += 1
        visited[x][y] = True

    check = False
    for i in range(4):    
        nx = x + dx[i]
        ny = y + dy[i]
        if not(0 <= nx < N and 0 <= ny < M):
            continue
        #방문할 곳이 있다면
        if room[nx][ny] == 0 and visited[nx][ny] == False:    
            check = True

    #4군데 중 청소할 곳이 없다면        
    if check == False:
        x += -dx[d] #후진
        y += -dy[d] #후진
        #범위를 벗어나면 종료
        if N <= x or x < 0 or M <= y or y < 0:
            break
        #후진하는 곳이 벽이라도 종료
        if room[x][y] == 1:
            break

    #청소할 곳이 있다면 반시계로 90도 회전
    if check == True:
        d -= 1
        #0에서 반시계로 90도 회전하는 경우 3으로 조정
        if d == -1:
            d = 3
        nx = x + dx[d]
        ny = y + dy[d]
        #회전 후 바라보는 곳의 앞이 청소되지 않은 곳이라면
        if 0 <= nx < N and 0 <= ny < M:
            if room[nx][ny] == 0 and visited[nx][ny] == False:
                #전진
                x = nx
                y = ny
    
print(result)