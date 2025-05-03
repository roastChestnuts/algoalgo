#주어진 입력에서 bfs를 통해 그림의 개수, 가장 큰 그림의 크기를 구하는 것이 문제
#탐색을 진입하는 시점에 count를 세주기
#탐색이 끝나는 시점에 max값을 측정해서 변수에 할당해주기

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
count = 0
result = 0
graph = []


for i in range(N):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[False]*M for _ in range(N)]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    #시작지점도 체크 및 넓이에 포함
    visited[x][y] = True
    width = 1 

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny] == True:
                continue
            if graph[nx][ny] == 0:
                continue
            q.append([nx, ny])
            width += 1
            visited[nx][ny] = True
    return width        

for i in range(N):
    for j in range(M):
        if visited[i][j] == False and graph[i][j] == 1:
            count += 1
            result = max(result, bfs(i, j))

print(count)
print(result)            