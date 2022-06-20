import sys
input = sys.stdin.readline

n = int(input())
garo = [0 for _ in range(n)]
ans = 0

def isPromising(x):
    for i in range(x): # 가로를 쭉 검사
        # 같은 열에 배치 or (x1-x2) == (y1-y2) 인지 검사 [오른쪽, 왼쪽 위 대각선 검사]
        if garo[i] == garo[x] or abs(garo[x] - garo[i]) == abs(x-i):
            return False
    return True

def nQueen(x):
    global ans

    if x == n:
        ans += 1 # 끝까지 배치 완료
        return
    else:
        for i in range(n):
            garo[x] = i # (x,i)에 퀸 배치
            if isPromising(x): # 배치할 수 있는가?
                nQueen(x+1)

nQueen(0)
print(ans)