import sys
input = sys.stdin.readline

n = int(input())

for t in range(n):
    braket = input().strip()
    stack = []
    isCorrect = True
    for i in braket:
        if i == '(':
            stack.append('(')
        else:
            if not stack:
                isCorrect = False
                break
            stack.pop()
    if stack:
        isCorrect = False
    print('YES' if isCorrect else 'NO')