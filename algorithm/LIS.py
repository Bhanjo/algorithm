# 백준 2565번
import sys
input = sys.stdin.readline

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
nums.sort(key=lambda k:k[0]) # 왼쪽 기준 ASC
dp = [1 for _ in range(n)]

# LIS 알고리즘
for i in range(n):
    for j in range(i):
        if nums[j][1] < nums[i][1]: # 기준(i) 보다 작다면 dp 갱신
            dp[i] = max(dp[i], dp[j]+1) # j의 최대 수열(dp[j])에 자기 자신(i) 추가
print(n - max(dp)) # max(dp) = 최대 연결 가능한 개수, 총 개수 - max(dp) = 제거할 전기줄 개수