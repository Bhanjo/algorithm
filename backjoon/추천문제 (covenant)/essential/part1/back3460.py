import sys
input = sys.stdin.readline

tc = int(input())

for t in range(tc):
    num = int(input())
    binary = []
    answer = []
    while(num > 0):
        binary.append(num % 2)
        num = num // 2
    for i, item in enumerate(binary):
        if item == 1:
            answer.append(i)
    print(*answer)