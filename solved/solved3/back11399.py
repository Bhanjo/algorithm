import sys
input = sys.stdin.readline

human = int(input())
task = list(map(int, input().split()))
task.sort()
workTime = task[0]
waitTime = 0

for i in range(1, len(task)):
    workTime += task[i]
    waitTime += task[i - 1]
    workTime += waitTime

print(workTime)