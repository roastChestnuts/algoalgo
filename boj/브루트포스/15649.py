n, m = map(int, input().split())
check = [True for _ in range(n+1)]
ans = []

def backtrack():
    if len(ans) == m:
        print(*ans)
        return
    
    for i in range(1, n+1):
        if check[i]:
            check[i] = False
            ans.append(i)
            backtrack()
            ans.pop()
            check[i] = True
backtrack()    
