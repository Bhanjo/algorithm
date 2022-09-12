import sys
input = sys.stdin.readline

n = int(input())
graph = []
# 가로 경우의 수, 세로 경우의 수, 대각선 경우의 수를 가지는 3차원 배열
dp = [[[0]*n for _ in range(n)] for _ in range(3)]

for i in range(n):
    graph.append(list(map(int, input().split())))

dp[0][0][1] = 1 # 파이프는 항상 가로로 시작

# dp에서 윗 행을 쓰기 위해 첫 번째 행을 초기화
for i in range(2,n):
    if graph[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]

for i in range(1,n):
    for j in range(1,n):
        # 대각선 가능
        if graph[i][j] == 0 and graph[i][j-1] == 0 and graph[i-1][j] == 0:
            dp[2][i][j] = dp[2][i-1][j-1] + dp[1][i-1][j-1] + dp[0][i-1][j-1]
        if graph[i][j] == 0:
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1] # 가로 가능
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j] # 세로 가능
    
print(dp[0][n-1][n-1] + dp[1][n-1][n-1] + dp[2][n-1][n-1])
