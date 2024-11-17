n, m = map(int, input().split())
ans = []
def func():
    if len(ans) == m:
        print(*ans)
        return
    for i in range(1, n+1):
        ans.append(i)
        func()
        ans.pop()
func()  
