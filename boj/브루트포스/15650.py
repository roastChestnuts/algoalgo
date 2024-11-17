n, m = map(int, input().split())
ans = []

def backtrack(start):
    if len(ans) == m:
        print(*ans)
        return
        
    for i in range(start, n+1):
        ans.append(i)
        backtrack(i+1)
        ans.pop()
        
backtrack(1)   
