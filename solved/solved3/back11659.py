import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int,input().split()))
answer = [0]
for i in range(n):
    answer.append(answer[i] + nums[i])
for i in range(m):
    start, end = map(int, input().split())
    print(answer[end] - answer[start - 1])