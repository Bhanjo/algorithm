import sys
input = sys.stdin.readline

n = int(input())
scores = [0 for i in range(301)]
dp = [0 for i in range(301)]

for i in range(n):
    scores[i] = int(input())

dp[0] = scores[0]
dp[1] = scores[0] + scores[1]
# 계단 총 2개를 오를때, 계단 총 1개를 오를때를 비교함
dp[2] = max(scores[1] + scores[2], scores[0] + scores[2])

# 3번째 계단에서부터 끝까지 탐색
for i in range(3, n):
    # 마지막 계단은 필수방문 요망
    # 마지막 계단을 밟을 수 있는 경우(1: 마지막-1 / 2: 마지막-2)
    # 마지막-1 의 경우 연속 3계단을 밟을 수 없다는 규칙이 적용됨
    dp[i] = max(dp[i-3] + scores[i-1] + scores[i], dp[i-2] + scores[i])

print(dp[n-1])
