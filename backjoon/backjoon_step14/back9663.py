import sys

# 퀸이 침범할 수 있는 영역인지 판단
def adjacent(x):
    for i in range(x):
        # 같은 열에 있거나 같은 대각선 인지 판단
        if col[x] == col[i] or abs(col[x] - col[i]) == x - i:
            return False
    return True

def DFS(x):
    global cnt
    if x == n:
        cnt += 1
    else:
        for i in range(n):
            col[x] = i
            if adjacent(x):
                DFS(x + 1)

n = int(sys.stdin.readline())
col = [0] * n
cnt = 0
DFS(0)
sys.stdout.write(str(cnt))