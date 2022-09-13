from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

q = deque()
q.append([n,0]) # 값, 시간, 이동경로
visit = [-1 for _ in range(100001)]
visit[n] = n
path = []

while(q):
    pos, cnt = q.popleft()
    if pos == m:
        print(cnt)
        idx = pos
        while pos != n:
            path.append(pos)
            pos = visit[pos]
        path.append(n)
        break

    pos1,pos2,pos3 = pos+1,pos-1,pos*2
    if 0 <= pos1 <= 100000 and visit[pos1] == -1:
        visit[pos1] = pos
        q.append([pos1, cnt+1])
    
    if 0 <= pos2 <= 100000 and visit[pos2] == -1:
        visit[pos2] = pos
        q.append([pos2, cnt+1])
    
    if 0 <= pos3 <= 100000 and visit[pos3] == -1:
        visit[pos3] = pos
        q.append([pos3, cnt+1])

print(*path[::-1])