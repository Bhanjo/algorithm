import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, r, c = map(int, input().split())
N = pow(2, n)
cnt = -1

def divcon(x,y,size):
    global cnt
        
    if not (x <= r < x + size and y <= c < y + size):
        cnt += size * size
        return

    if size == 2:
        for i in range(x, x + size):
            for j in range(y, y + size):
                cnt += 1
                if i == r and j == c:
                    print(cnt)
                    exit(0)
        return

    divcon(x,y,size//2)
    divcon(x,y + size//2,size//2)
    divcon(x + size//2,y,size//2)
    divcon(x + size//2,y + size//2,size//2)

divcon(0,0,N)