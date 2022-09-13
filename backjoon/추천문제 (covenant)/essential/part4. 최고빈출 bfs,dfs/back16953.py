from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

q = deque()
q.append([n,1])
answer = -1

while(q):
    num, cnt = q.popleft()
    if num == m:
        answer = cnt
        break
    num2 = num*2
    num3 = int(str(num)+'1')
    if num2 <= m: q.append([num2,cnt+1])
    if num3 <= m: q.append([num3,cnt+1])

print(answer)