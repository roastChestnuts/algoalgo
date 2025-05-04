# 자신의 아래 층의 1호~x호 까지의 사람수의 합만큼이 내 집에 살아야 한다.
# 시작 층은 0층
# 시작 호수는 1호
# 0층은 각 호에 i만큼의 인원이 거주

#T - 횟수
#k - 층 n - 호

#1~14층 1~14호

#[풀이]
#각각의 층과 호수에 dp테이블을 통해 인원수를 미리 생성

import sys

input = sys.stdin.readline

dp = [[i for i in range(15)] for _ in range(15)]

for i in range(1, 15):
    for j in range(1, 15):
        dp[i][j] = sum(dp[i-1][:j+1])2
T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    print(dp[k][n])