import sys
input = sys.stdin.readline

n, m = map(int, input().split())
poketmon = []
poketmonDict = {}

for i in range(n):
    name = input().strip()
    poketmon.append(name)
    poketmonDict[name] = i + 1

for i in range(m):
    findDict = input().strip()
    if(findDict.isdigit()):
        print(poketmon[int(findDict) - 1])
    else:
        print(poketmonDict[findDict])