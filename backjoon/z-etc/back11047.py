import sys
input = sys.stdin.readline

num, money = map(int, input().split())
coins = []
for i in range(num):
    coins.append(int(input()))

ans = 0
for i in range(num - 1, -1, -1):
    if(coins[i] <= money):
        ans += money // coins[i]
        money = money % coins[i]
print(ans)