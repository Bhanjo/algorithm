def solution(nums):
    answer = 0

    # 에라토스테네스의 체
    primes = [True] * 3001
    primes[0] = False
    primes[1] = False
    for i in range(2, int(3001**1/2)+1):
        if primes[i] == True:
            j = 2
            while i * j <= 3001:
                primes[i*j] = False
                j += 1

    for i in range(len(nums) - 2):
        for j in range(i+1, len(nums) - 1):
            for k in range(j+1, len(nums)):
                if primes[nums[i] + nums[j] + nums[k]]:
                    answer += 1
    return answer
solution([1,2,3,4])