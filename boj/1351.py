# 문제
# 무한 수열 A는 다음과 같다.

# A0 = 1
# Ai = A (i/P) + A (i/Q) (i ≥ 1)
# N, P와 Q가 주어질 때, AN을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 3개의 정수 N, P, Q가 주어진다.

# 출력
# 첫째 줄에 AN을 출력한다.

# 제한
# 0 ≤ N ≤ 10^12
# 2 ≤ P, Q ≤ 10^9

# 힌트
# (x)는 x를 넘지 않는 가장 큰 정수이다.

#7(N) 2(P) 3(Q) -> 7

# 10억, P, Q는 2, 3
# A10억 = A(5억) + A(3.333....억)

import sys

input = sys.stdin.readline

N, P, Q = map(int, input().split())

dp = dict()
dp[0] = 1

def recursive(num):
    if num not in dp:
        dp[num] = recursive(num//P) + recursive(num//Q)
    return dp[num] 

print(recursive(N))

