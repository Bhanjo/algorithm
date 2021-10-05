import sys
input = sys.stdin.readline
tc = int(input())

for _ in range(tc):
    num = int(input())
    saveNum = dict()
    saveNum[0] = [1, 0]
    saveNum[1] = [0, 1]
    for i in range(2, num+1):
        saveNum[i] = [saveNum[i-1][0]+saveNum[i-2]
                      [0], saveNum[i-1][1]+saveNum[i-2][1]]
    print(*saveNum[num])
