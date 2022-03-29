import sys
input = sys.stdin.readline

n = int(input())
timeTable = []

for i in range(n):
    s, e = map(int, input().split())
    timeTable.append([s,e])
timeTable = sorted(timeTable, key = lambda x:(x[1],x[0]))

endTime = 0
cnt = 0
for s, e in timeTable:
    if s >= endTime:
        endTime = e
        cnt += 1

print(cnt)