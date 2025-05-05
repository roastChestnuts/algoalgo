# 1(1) - 1
# 2(3) - ll = ㅁ
# 3(5) - lll =l l= ㅁl lㅁ
# 4(11) - llll ll= llㅁ ㅁll ㅁ= 
# 5(21)
# 6(43)
# 7(85)
# 8(171)

import sys

input = sys.stdin.readline

n = int(input())

dp = [0, 1, 3]

for i in range(3, 1001):
    dp.append(dp[i-1]+dp[i-2]*2)

print(dp[n]%10007)    