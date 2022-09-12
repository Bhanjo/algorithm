import sys
input = sys.stdin.readline

INF = 10**6
n,k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [INF for _ in range(k+1)]
dp[0] = 1

for coin in coins:
    for k in range(coin, k+1):
        div = 10**7
        if k % coin == 0:
            div = k // coin
        dp[k] = min(dp[k], dp[k-coin]+1, div)

print(dp[k] if dp[k] != INF else -1)