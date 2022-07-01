def solution(board, moves):
    boards = [[0]*len(board) for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            boards[i][j] = board[j][i]

    answer = 0
    st = []
    for i in moves:
        pickUp = 0
        while(True):
            if len(boards[i-1]) == 0:
                break
            pickUp = boards[i-1].pop(0)
            if len(boards[i-1]) == 0 or pickUp > 0:
                break
        if pickUp > 0:
            st.append(pickUp)
            if len(st) > 1:
                if st[len(st) - 1] == st[len(st) - 2]:
                    st.pop()
                    st.pop()
                    answer += 2
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
# print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,1,1,2,2,2,3,5]))

# best
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer

# 2회차
def solution(board, moves):
    answer = 0
    depth = len(board)
    st = []
    for i in moves:
        idx = i-1
        for j in range(depth):
            if board[j][idx] > 0:
                item = board[j][idx]
                board[j][idx] = 0
                if len(st) == 0:
                    st.append(item)
                else:
                    if item == st[-1]:
                        st.pop()
                        answer += 2
                    else:
                        st.append(item)
                break
    return answer