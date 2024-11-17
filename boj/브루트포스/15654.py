n, m = map(int, input().split())
ans = []
array = list(map(int, input().split()))
array.sort()

def func():
    if len(ans) == m:
        print(*ans)
        return
    for i in array:
        if i not in ans:
            ans.append(i)
            func()
            ans.pop()
func()    
