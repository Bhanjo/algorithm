import sys
input = sys.stdin.readline

a, p = map(int, input().split())
numbers = [0]*100
numbers[1] = a
i = 2

while(i < len(numbers)):
    num = str(numbers[i-1])
    hap = 0
    for j in range(len(num)):
        hap += int(num[j])**p
    numbers[i] = hap
    i += 1

hash = [0]*1000000
cnt = 0
for i in numbers[1:]:
    hash[i] += 1
print(hash.count(1))
