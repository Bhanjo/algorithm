import sys
input = sys.stdin.readline
n = int(input())
paper = []
for i in range(n):
    garo = list(map(int, input().split()))
    paper.append(garo)

white = 0
blue = 0

def divcon(x,y,size):
    global white
    global blue
    currPaper = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if currPaper != paper[i][j]:
                divcon(x + size // 2, y, size // 2)
                divcon(x, y + size // 2, size // 2)
                divcon(x + size // 2, y + size // 2, size // 2)
                divcon(x, y, size // 2)
                return
    if currPaper == 1:
        blue += 1
    else:
        white += 1

divcon(0,0,n)
print(white)
print(blue)