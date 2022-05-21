from collections import deque
import sys
input = sys.stdin.readline

tc = int(input())

for t in range(tc):
    commands = str(input()).rstrip()
    stSize = int(input())
    reverseCount = 0
    st = input().rstrip()[1:-1].split(',')
    q = deque(st)
    isCorrect = True
    if(stSize == 0):
        q = []
    for i in commands:
        if i == 'R':
            reverseCount += 1
        if i == 'D':
            if len(q) > 0:
                if reverseCount % 2 == 1:
                    q.pop()
                else:
                    q.popleft()
            else:
                isCorrect = False
                print('error')
                break
    if isCorrect:
        if reverseCount % 2 == 1:
            q.reverse()
            print('['+','.join(q)+']')
        else:
            print('['+','.join(q)+']')