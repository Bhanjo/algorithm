import sys
input = sys.stdin.readline

num = int(input())  # 1~10^6
dp = [0]*(num+1)

for i in range(2, num+1):
    dp[i] = 1 + dp[i-1]  # 케이스1) 1을 빼고 이전 최소연산횟수
    if i % 2 == 0:  # 케이스2-1) min(케이스1, 2로 나눈 몫의 최소연산횟수)
        dp[i] = min(dp[i], 1+dp[i//2])
    if i % 3 == 0:  # 케이스2-2) min(케이스1, 3으로 나눈 몫의 최소연산횟수)
        dp[i] = min(dp[i], 1+dp[i//3])
print(dp[num])
