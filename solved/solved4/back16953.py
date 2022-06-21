from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def bfs(n, target):
    q = deque()
    q.append((n,1))
    while(q):
        value, count = q.pop()
        if value == target:
            print(count)
            return
        if value < target:
            q.append((value*2,count+1))
            q.append((int(str(value)+"1"),count+1))
    print(-1)

bfs(n, m)