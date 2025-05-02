# if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
#     1

# if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
#     w(20, 20, 20)

# if a < b and b < c, then w(a, b, c) returns:
#     w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

# otherwise it returns:
#     w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)


# [입력범위]
# -50 ≤ a, b, c ≤ 50
# [종료조건]
# -1, -1, -1

import sys

input = sys.stdin.readline

dp = dict()

for i in range(-50, 51):
    for j in range(-50, 51):
        for k in range(-50, 51):
            dp[(i,j,k)] = 0

def w(a, b, c):
    if dp[(a,b,c)] == 0:
        if a <= 0 or b <= 0 or c <= 0:
            dp[(a,b,c)] = 1
        elif a > 20 or b > 20 or c > 20:
            dp[(a,b,c)] = w(20, 20, 20)
        elif a < b and b < c:
            dp[(a,b,c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        else:
            dp[(a,b,c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    return dp[(a,b,c)]    

while True:
    a, b, c = map(int, input().split())
    
    if a == -1 and b == -1 and c == -1:
        break

    result = w(a,b,c)
    
    print(f'w({a}, {b}, {c}) = {result}')
