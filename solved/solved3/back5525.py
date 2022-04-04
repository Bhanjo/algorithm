import sys
input = sys.stdin.readline

N = int(input())
num = int(input())
s = input().strip()

cnt = 0
ioiCounter = 0
i = 0
while(i < num - 1):
    if s[i:i + 3] == "IOI":
        ioiCounter += 1
        i += 2
        if ioiCounter == N: # ioi가 N개 있다면 일치
            cnt += 1
            ioiCounter -= 1 # ioioi 일 때 ioiCounter = 2니까 1감소해서 이어 검사
    else:
        ioiCounter = 0
        i += 1
print(cnt)