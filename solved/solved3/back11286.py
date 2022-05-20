import heapq
import sys
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
        heapq.heappush(h, (abs(num),num))
