from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int, input().split())
q = deque([i+1 for i in range(n)])
answer = []

cnt = 1
while(len(answer) < n):
    if cnt < k:
        q.append(q.popleft())
        cnt += 1
    else:
        answer.append(q.popleft())
        cnt = 1
print('<'+str(answer)[1:-1]+'>')