import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = []
cnt = 0
for i in range(n):
    s.append(input().strip())
for i in range(m):
    word = input().strip()
    cnt = cnt + 1 if word in s else cnt
print(cnt)