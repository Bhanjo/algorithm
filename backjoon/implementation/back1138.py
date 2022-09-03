import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))
line = [0]*n
for i in range(1, n+1):
    total = h[i-1]
    cnt = 0
    for j in range(n):
        if cnt == total and line[j] == 0:
            line[j] = i
            break
        elif line[j] == 0:
            cnt += 1
print(line)
