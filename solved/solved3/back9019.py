from collections import deque
import sys
input = sys.stdin.readline

tc = int(input())

for t in range(tc):
    A, B = map(int,input().split())
    visit = [0 for _ in range(10000)]
    
    q = deque()
    q.append((A, ''))

    while(q):
        info = q.popleft()
        visit[info[0]] == 1

        if info[0] == B:
            print(info[1])
            break

        num = (info[0]*2)%10000
        if visit[num] == 0:
            visit[num] = 1
            q.append((num, info[1] + 'D'))

        num = (info[0]-1)%10000
        if visit[num] == 0:
            visit[num] = 1
            q.append((num, info[1] + 'S'))

        num = (10 * info[0] + (info[0] // 1000)) % 10000
        if visit[num] == 0:
            visit[num] = 1
            q.append((num, info[1] + 'L'))

        num = (info[0] // 10 + (info[0] % 10) * 1000) % 10000
        if visit[num] == 0:
            visit[num] = 1
            q.append((num, info[1] + 'R'))