#각각의 경우의 수를 그때 그때 구하려면...매우 힘들듯
#메모이제이션을 통해 각각 경우의 수를 더해주기
# 1 : l
# 2 : ll =
# 3 : l= lll =l
# 4 : llll ll= == =ll
# 5 : lllll lll= l== l=ll ==l =l=
import sys

input = sys.stdin.readline

n = int(input())

dp = [0, 1, 2]

for i in range(3, 1001):
    dp.append(dp[i-1]+dp[i-2])

print(dp[n]%10007)    