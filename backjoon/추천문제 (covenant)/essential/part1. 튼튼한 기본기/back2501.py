import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = 0
cnt = 0

for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == m:
        answer = i
        break

print(answer)