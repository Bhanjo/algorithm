def isPrime(num):
    if num == 1: return False
    for i in range(2, int(num**(1/2)) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    num = []
    # k 진수 변환
    while(n):
        num.append(str(n%k))
        n = n // k
    num.reverse()
    
    num = ''.join(num).split("0")
    for i in num:
        if len(i) > 0 and int(i) != 1 and isPrime(int(i)):
            answer += 1
    
    return answer