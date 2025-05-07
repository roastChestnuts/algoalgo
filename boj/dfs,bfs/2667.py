#dfs 탐색하러 들어갈 때 카운트(단지수)
#dfs 재귀함수 내에서 카운트(단지 내 호수)

import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
count = 0


def dfs(x, y):
    global count
    #방문처리
    visited[x][y] = True
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if visited[nx][ny] == True:
            continue
        if graph[nx][ny] == 0:
            continue
        dfs(nx, ny)

ans = []
for i in range(N):
    for j in range(N):
        if visited[i][j] == True:
            continue
        if graph[i][j] == 0:
            continue
        #여기서 카운트(단지수)
        dfs(i, j)    
        ans.append(count)
        count = 0

print(len(ans))
for num in ans:
    print(num)