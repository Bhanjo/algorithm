def solution(board, skill):
    xSize, ySize = len(board), len(board[0])
    answer = 0
    attack = [[0]*(ySize+1) for _ in range(xSize+1)]
    
    # 누적합 초기화
    for s in skill:
        ty, r1, c1, r2, c2, cost = s
        if ty == 2: cost = -cost # 힐이라면 값 변경
        attack[r1][c1] += cost
        attack[r2+1][c1] += -cost
        attack[r1][c2+1] += -cost
        attack[r2+1][c2+1] += cost
        
    # 누적합 계산 (좌,우)
    for x in range(xSize):
        for y in range(ySize):
            attack[x][y+1] += attack[x][y]
    
    # 누적합 계산 (상,하)
    for y in range(ySize):
        for x in range(xSize):
            attack[x+1][y] += attack[x][y]

    for i in range(xSize):
        for j in range(ySize):
            if board[i][j] - attack[i][j] > 0:
                answer += 1
    
    return answer