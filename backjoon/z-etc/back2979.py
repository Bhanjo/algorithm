import sys
input = sys.stdin.readline

answer = 0
fee = list(map(int, input().split()))
car = [list(map(int, input().split())) for _ in range(3)]
stack = []

for i in range(1, 101):
    if (stack):
        answer += fee[len(stack)-1] * len(stack)
    for c in car:
        if c[0] == i:
            stack.append(c)
    idx = 0
    while(idx < len(stack)):
        if stack[idx][1] == i:
            stack.pop(idx)
            idx = 0
        idx += 1

print(answer)