def solution(m, n, board):
    board = [list(i) for i in board] # bard를 문자열이 아닌 2차원 배열로 변환
    answer = 0

    while(True):
        check = [] # 터트릴 아이템 좌표
        for x in range(m - 1):
            for y in range(n - 1):
                if board[x][y] == '0': continue
                if board[x][y] == board[x+1][y] == board[x][y+1] == board[x+1][y+1]:
                    check.append((x,y))
                    check.append((x,y+1))
                    check.append((x+1,y))
                    check.append((x+1,y+1))
        
        if len(check) == 0:
            break
        else:
            answer += len(set(check)) # 좌표 중복 제거
            for i in check:
                board[i[0]][i[1]] = '0' # 터트릴 곳을 0으로 변환
            
            # 빈 공간의 위에 있는 것을 아래로 내리기
            for i in check:
                xTop = i[0] - 1 # 위
                xBottom = i[0]  # 아래
                while xTop >= 0:
                    # 빈 공간이 있고 그 바로 위에 내려올 아이템이 있을 때
                    if board[xBottom][i[1]] == '0' and board[xTop][i[1]] != '0':
                        board[xBottom][i[1]] = board[xTop][i[1]]
                        board[xTop][i[1]] = '0'
                    xBottom -= 1
                    xTop -= 1

    return answer
solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"])