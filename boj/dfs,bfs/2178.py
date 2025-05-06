import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input().rstrip())))

visited = [[False]*M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 0 or visited[nx][ny] == True:
                continue
            q.append((nx, ny))
            visited[nx][ny] = True
            graph[nx][ny] = graph[x][y] + 1

bfs(0, 0)
print(graph[N-1][M-1])