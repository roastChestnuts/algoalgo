# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 "정점 번호가 작은 것을 먼저 방문"하고, 
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 
# 탐색을 시작할 정점의 번호 V가 주어진다. 
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 
# 입력으로 주어지는 "간선은 양방향"이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 
# 그 다음 줄에는 BFS를 수행한 결과를 출력한다. 
# V부터 방문된 점을 순서대로 출력하면 된다.

import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for i in range(N+1)]

for i in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

#정점이 작은 순서대로 방문하기 위한 정렬
for node in graph:
    node.sort()

#DFS
dfs_visited = [False] * (N+1)
dfs_result = []
def dfs(node):
    dfs_visited[node] = True
    dfs_result.append(node)

    for next in graph[node]:
        if dfs_visited[next] == False:
            dfs(next)

#BFS
bfs_visited = [False] * (N+1)
bfs_result = []

def bfs(result):
    queue = deque([result])

    while queue:
        node = queue.popleft()
        if bfs_visited[node] == False:
            bfs_result.append(node)
            bfs_visited[node] = True
            for next in graph[node]:
                queue.append(next)


#출력
dfs(V)
bfs(V)
print(*dfs_result)   
print(*bfs_result, end=' ')                


