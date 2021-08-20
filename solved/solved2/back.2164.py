import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dq = deque([i + 1 for i in range(n)])
while(True):
    if len(dq) == 1:
        sys.stdout.write(str(dq.pop()))
        break
    dq.popleft()
    m = dq.popleft()
    dq.append(m)