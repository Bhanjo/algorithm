def solution(grid):
    answer = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    # key = dx[key, dy[key] / value = 바뀌는 방향
    # key = 0 => 위로 올라갔을 때 right를 만났다면 오른쪽으로, left를 만났다면 왼쪽으로 이동
    rightDir = {0: 3, 1: 2, 2: 0, 3: 1}
    leftDir = {0: 2, 1: 3, 2: 1, 3: 0}
    w, h = len(grid[0]), len(grid)
    visit = [[[0]*4 for _ in range(w)] for _ in range(h)]

    for y in range(h):
        for x in range(w):
            # 4방향
            for i in range(4):
                if visit[y][x][i] == 0:
                    length = 0
                    ty, tx, ti = y, x, i
                    while(True):
                        visit[ty][tx][ti] += 1
                        length += 1
                        curr = grid[ty][tx]
                        if curr =='L':
                            ti = leftDir[ti]
                        elif curr == 'R':
                            ti = rightDir[ti]
                        # 이동
                        ty, tx = (ty + dy[ti]) % h, (tx + dx[ti]) % w
                        # 시작 위치 == 이동 위치 and 처음 이동 예정 방향 == 현재 이동 예정 방향
                        if tx == x and ty == y and ti == i:
                            break
                    answer.append(length)
    answer.sort()
    return answer