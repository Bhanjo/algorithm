import sys

input = sys.stdin.readline

n = int(input())
answer = 0
weight = []
for i in range(n):
    weight.append(int(input()))
weight.sort(reverse=True)

for i in range(n):
    answer = weight[i] * (i+1) if answer <= weight[i] * (i+1) else answer

print(answer)
