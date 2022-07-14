import sys
input = sys.stdin.readline

tc = int(input())

for t in range(tc):
    col = int(input())
    graph = [list(map(int,input().split())) for _ in range(2)]
    
    dp = [[0]*col for _ in range(2)]
    dp[0][0] = graph[0][0]
    dp[1][0] = graph[1][0]

    for y in range(1, col):
        dp[0][y], dp[1][y] = graph[0][y], graph[1][y]
        if y == 1:
            dp[0][y] = dp[1][y-1] + graph[0][y]
            dp[1][y] = dp[0][y-1] + graph[1][y]
        else:
            dp[0][y] = max(dp[1][y-1] + graph[0][y], dp[1][y-2] + graph[0][y])
            dp[1][y] = max(dp[0][y-1] + graph[1][y], dp[0][y-2] + graph[1][y])
    print(max(dp[0][col-1], dp[1][col-1]))