import sys
input = sys.stdin.readline

n = int(input())
temp = []
answer = []

def isPrime(num):
    num = int(num)
    if num == 1:
        return False
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True

def permu():
    if len(temp) == n:
        answer.append(int(''.join(temp)))
        return
    for i in range(1,10):
        num = ''.join(temp)
        if isPrime(num + str(i)):
            temp.append(str(i))
            permu()
            temp.pop()

permu()
for i in answer:
    print(i)