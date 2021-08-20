from collections import deque
import sys
input = sys.stdin.readline
dq = deque()
n = int(input())
# front = 오른쪽, back = 왼쪽

for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'push_front':
        dq.append(cmd[1])
    elif cmd[0] == 'push_back':
        dq.appendleft(cmd[1])
    elif cmd[0] == 'pop_front':
        print(dq.pop()) if len(dq) > 0 else print(-1)
    elif cmd[0] == 'pop_back':
        print(dq.popleft()) if len(dq) > 0 else print(-1)
    elif cmd[0] == 'size':
        print(len(dq))
    elif cmd[0] == 'empty':
        print(1) if len(dq) < 1 else print(0)
    elif cmd[0] == 'front':
        print(dq[len(dq)-1]) if len(dq) > 0 else print(-1)
    elif cmd[0] == 'back':
        print(dq[0]) if len(dq) > 0 else print(-1)
