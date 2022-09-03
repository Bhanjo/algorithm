import sys
input = sys.stdin.readline

n = int(input())
dir = {}

for i in range(n):
    book = input().strip()
    if book not in dir:
        dir[book] = 1
    else:
        dir[book] += 1

answer = list(dir.items())
answer.sort(key=lambda x:(-x[1], x[0]))
print(answer[0][0])
