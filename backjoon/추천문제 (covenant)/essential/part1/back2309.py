import sys
import copy
input = sys.stdin.readline

troll = []
visit = [False for _ in range(9)]
for i in range(9):
    troll.append(int(input()))
troll.sort()

temp = []
answer = []
def dfs(target):
    global answer
    if len(temp) == 7:
        if sum(temp) == 100:
            answer = copy.deepcopy(temp)
        return
    for i in range(target, 9):
        if not visit[i]:
            visit[i] = True
            temp.append(troll[i])
            dfs(i)
            temp.pop()
            visit[i] = False

dfs(0)
for i in answer:
    print(i)

