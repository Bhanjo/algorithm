import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

dp = [0 for _ in range(10001)]
dp[0], dp[1], dp[2], dp[3] = 1, 1, 2, 3

for i in range(4, 10001):
    dp[i] = dp[i-1] + (dp[i-2] - dp[i-3])
    if i % 3 == 0:
        dp[i] += 1

for i in nums:
    print(dp[i])