import sys
input = sys.stdin.readline

result = 1
numbers = [0]*10
for _ in range(3):
    result *= int(input())
changeResult = str(result)
for i in changeResult:
    numbers[int(i)] += 1
for j in numbers:
    print(j)
