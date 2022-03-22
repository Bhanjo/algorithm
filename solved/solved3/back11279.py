import sys
import heapq

input = sys.stdin.readline
h = []

tc = int(input())
for i in range(tc):
    num = int(input())
    if(num == 0):
        if(len(h) == 0):
            print(0)
        else:
            print(heapq.heappop(h)[1])
    else:
        # 튜플을 이용해 우선순위 부여 (우선순위, 값)
        heapq.heappush(h, (-num, num))