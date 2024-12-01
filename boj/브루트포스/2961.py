import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

answer = 1e9
n = int(input())
recipes = [list(map(int, input().split())) for _ in range(n)]


def backtrack(depth, sour, bitter):
  global answer
  
  if depth == n:
    if bitter != 0:
      answer = min(answer, abs(sour-bitter))
    return
  backtrack(depth+1, sour, bitter)  
  backtrack(depth+1, sour*recipes[depth][0], bitter+recipes[depth][1])  
    

backtrack(0, 1, 0)
print(answer)
