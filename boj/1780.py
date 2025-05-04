#현재 탐색하는 범위의 모든 값이 같을 경우 해당 값의 개수를 세줘야 한다.
#만약 다른 값이 존재한다면 종이를 9등분 한다.
#다시 1을 반복, 분할 정복한다.
#즉 9번의 재귀함수 호출
#9등분 후 모든 재귀함수들에선 x, y좌표값들의 시작점이 필요하고 멈출 지점이 필요함
#멈출 지점은 현재 탐색하는 종이의 크기(계속 3등분 됨)
#시작 지점은 x, y 각각 
#9에서 시작 => 0, 3, 6
#27에서 시작 => 0, 9, 18
#81에서 시작 => 0, 27, 54

import sys

input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
cnt = {-1:0, 0:0, 1:0}

def recur(x, y, n):
    #현재 진입 시점의 값
    checkValue = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            #체크할 값과 다른 값이 존재한다면 쪼갠다
            if checkValue != paper[i][j]:
                #다음 탐색 범위
                nextRange = n//3
                for dx in (0, nextRange, 2*nextRange):
                    for dy in (0, nextRange, 2*nextRange):
                        recur(x+dx, y+dy, nextRange)
                return
    cnt[checkValue] += 1

recur(0, 0, N)

print(cnt[-1])
print(cnt[0])
print(cnt[1])