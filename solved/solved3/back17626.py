import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1

for i in range(2, n+1):
    minVal = 1e9
    for j in range(1, int(i**(1/2))+1):
        minVal = min(minVal, dp[i-(j**2)])
    dp[i] = minVal + 1
print(dp[n])