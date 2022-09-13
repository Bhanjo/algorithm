from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
q = deque()
q.append([n,0])
answer = []
step = [10**6 for _ in range(201001)]
step[n] = 0

while(q):
    now, cnt = q.popleft()
    step[now] = min(step[now],cnt)
    if now == m:
        answer.append(cnt)
    if 0 <= now <= 100500:
        if step[now-1] == 10**6:
            q.append([now-1,cnt+1])
        if step[now+1] == 10**6:
            q.append([now+1,cnt+1])
        if step[now*2] == 10**6:
            q.append([now*2,cnt+1])

minval = min(answer)
print(minval)
print(answer.count(minval))