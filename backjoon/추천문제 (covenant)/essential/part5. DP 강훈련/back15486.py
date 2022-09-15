import sys
input = sys.stdin.readline

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)] # 시간, 비용
dp = [0 for _ in range(n+1)]
maxValue = 0

for day in range(n): # 퇴사일을 하루씩 늘려가기
    maxValue = max(maxValue, dp[day])
    time, cost = table[day]
    # 오늘 상담 진행 => 퇴사일 초과 => 상담 안함
    if day + time > n:
        continue
    # dp = (오늘상담 끝나는 시점 수익) vs (지금까지 수익+오늘 끝나는 상담 수익)
    dp[day+time] = max(dp[day+time], maxValue+cost)

print(max(dp))