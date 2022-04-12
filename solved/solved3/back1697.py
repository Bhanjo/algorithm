import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

def bfs():
    q = deque()
    maxLength = 100000
    load = [0] * 100001
    q.append(n)
    while q:
        point = q.popleft()
        if point == k:
            return load[point]
        moves = [point - 1, point + 1, point * 2]
        for i in moves:
            # not load[i] => 한 번도 방문한 적 없는 것을 판별
            if 0 <= i and i <= maxLength and not load[i]:
                load[i] += load[point]+1
                q.append(i)
        print(load[4:18])

print(bfs())