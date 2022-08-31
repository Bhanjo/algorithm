"""
    에라토스테네스의 체
    - 정해진 범위 안에서 소수들 찾기
    - 0~n 까지 숫자 배열 생성
    - 최대 진행을 n**1/2로 설정 (target)
    - 2부터 target 까지 진행 (i)
    - 인덱스 i의 값이 소수 일 때 소수의 배수들을 False 처리
    - True인 값들이 곧 소수가 됨
"""
def prime_list(n):
    nums = [True for _ in range(n)]
    nums[0], nums[1] = False, False
    target = int(n**1/2)
    for i in range(2, target+1):
        if nums[i]:
            for j in range(2*i, n, i):
                nums[j] = False
    return nums

print(prime_list(100))

# 번외: 해당 수가 소수 인지 판별
def isPrime(n):
    isPrime = True
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            isPrime = False
            break
    return isPrime