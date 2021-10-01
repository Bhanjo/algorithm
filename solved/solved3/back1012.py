import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)


def dfs(ground, check, x, y):
    global cnt
    if ground[x][y] == 1 and check[x][y] == 0:
        check[x][y] = 1
        if x == 0:
            dfs(ground, check, x+1, y)
        elif x > 0 and x < m - 1:
            dfs(ground, check, x-1, y)
            dfs(ground, check, x+1, y)
        else:
            dfs(ground, check, x-1, y)

        if y == 0:
            dfs(ground, check, x, y+1)
        elif y > 0 and y < n - 1:
            dfs(ground, check, x, y-1)
            dfs(ground, check, x, y+1)
        else:
            dfs(ground, check, x, y-1)


tc = int(input())
for _ in range(tc):
    m, n, k = map(int, input().split())
    ground = [[0]*n for a in range(m)]
    check = [[0]*n for b in range(m)]

    for i in range(k):
        x, y = map(int, input().split())
        ground[x][y] = 1

    cnt = 0
    for j in range(m):
        for k in range(n):
            if ground[j][k] == 1 and check[j][k] == 0:
                dfs(ground, check, j, k)
                cnt += 1
    print(cnt)
