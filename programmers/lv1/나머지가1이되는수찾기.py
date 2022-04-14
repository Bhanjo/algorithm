def solution(n):
    answer = 0
    if n % 2 == 0:
        for i in range(1, 1000000, 2):
            if n % i == 1:
                answer = i
                break
    else:
        for i in range(2, 1000000, 2):
            if n % i == 1:
                answer = i
                break
    return answer