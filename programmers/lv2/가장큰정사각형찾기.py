def solution(board):
    dp = [[0] * len(board[0]) for i in range(len(board))]
    dp[0] = board[0]
    for i in range(1, len(board)):
        dp[i][0] = board[i][0]
    
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

    maxVal = 0
    for i in range(len(dp)):
        maxVal = max(dp[i]) if max(dp[i]) > maxVal else maxVal
    return maxVal * maxVal

solution([[0,0,1,1],[1,1,1,1]])