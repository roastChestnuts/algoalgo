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



#로그 계산법
#10^3 = 1000 / log₁₀ 1000 = 3

# 1. t단계 후 크기 = (n/k^t)  #10억을 최소 2로 계속해서 나눠 나간다면 10/2^t
# 2. 종료 조건 : (n/k^t <= 1)  #값이 결국 0,1이 된다면 종료된다고 가정
# 3. 양변 곱 → (n <= k^t)
# 4. 로그 정의 → (t >= logkn)  
# 5. 단계 수 = ⌈logₖ n⌉ = Θ(log n) **빅오표기법
