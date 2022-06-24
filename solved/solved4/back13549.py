from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
q = deque()
load = [-1]*100001
visit = [0 for _ in range(100001)]
visit[n] = 1
load[n] = 0
q.append(n)

while(q):
    currPos = q.popleft()
    if currPos*2 < 100001 and visit[currPos*2] == 0:
        q.appendleft(currPos*2) # 다른 연산보다 우선쉬위를 가지기 위함
        visit[currPos*2] = 1
        load[currPos*2] = load[currPos]
    if currPos+1 < 100001 and visit[currPos+1] == 0:
        q.append(currPos+1)
        visit[currPos+1] = 1
        load[currPos+1] = load[currPos] + 1
    if 0 <= currPos-1 and visit[currPos-1] == 0:
        q.append(currPos-1)
        visit[currPos-1] = 1
        load[currPos-1] = load[currPos]+1
print(load[m])