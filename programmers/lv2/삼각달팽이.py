def solution(n):
    answer = []
    graph = [[0] * n for _ in range(n)]
    
    x, y = -1, 0
    direction, cnt = 1,1
    while(n >= 0):
        for _ in range(n):
            if direction % 3 == 1:
                x += 1
            elif direction % 3 == 2:
                y += 1
            elif direction % 3 == 0:
                x -=1
                y -= 1
            graph[x][y] = cnt
            cnt += 1
        direction += 1
        n -= 1
    for row in graph:
        for col in row:
            if col > 0: answer.append(col)
    return answer