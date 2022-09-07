import sys
input = sys.stdin.readline

n,m = map(int, input().split())
coins = []
answer = 0

for i in range(n):
    coins.append(int(input()))

dp = [0 for _ in range(m+1)]
dp[0] = 1 # x원 동전으로 x원을 만들 수 있는 경우의 수 = 1

# 핵심: 각 동전은 몇 개라도 쓸 수 있다
for coin in coins:
    for k in range(coin, m+1):
        # coin = 1원, k = 1원일 때 => 1-1 = 0 => dp[0] = 1
        # => coin동전으로 k원을 만들 수 있는 경우의 수 = 1

        # 왜 k-coin? => 3원을 만들 때 1원으로 만들 수 있는 경우의 수는 이미 구함
        # => 3 = [1,1,1] 처럼 이미 coin = 1 일 때 dp[3] = 1로 갱신되었음
        # => 이제 남은 것 => 1과 2로 3원 구하기
        # => coin(2원) 을 썼을 때 남은 금액 => 3-2 = 1 (핵심에 의해 똑같은 동전 계속 사용 가능)
        # => 1원 만들 수 있는 경우의 수 = 1
        # => [1,1,1], [2,1] = 2개
        dp[k] += dp[k-coin]
    print(dp)

print(dp)