#input() 자동 strip
#sys input -> 한 줄 단위로 입력받기 때문에 rstrip() 해줘야함
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []

for i in range(N):
    graph.append(list(map(int, input().rstrip())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(i, j):
    #방문처리
    graph[i][j] = 1
    for k in range(4):
        if 0<= i+dx[k] < N and 0 <= j+dy[k] < M:
            if graph[i+dx[k]][j+dy[k]] == 0:
                dfs(i+dx[k], j+dy[k])

count = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            count += 1
            dfs(i, j)


print(count)