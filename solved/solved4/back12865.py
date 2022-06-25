import sys
input = sys.stdin.readline

n,m = map(int, input().split())
items = []
items.append([0,0])
for i in range(n):
    items.append(list(map(int, input().split())))
dp = [[0]*(m+1) for _ in range(n+1)] # n번째 물건 까지 살펴봤을 때 무게가 m인 배낭의 최대 가치

for i in range(1, n+1):
    for j in range(1, m+1):
        weight = items[i][0]
        value = items[i][1]
        if j < weight: # 물건을 담을 수 없을 때
            dp[i][j] = dp[i-1][j] # 이전 배낭 그대로 가져가기
        else:
            # 이전 배낭 그대로 가져가는 것과 이전 배낭 중 (j-weight)값 + value 중 더 큰 것 가져가기
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)

print(dp[n][m])