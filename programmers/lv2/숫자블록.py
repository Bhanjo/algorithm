def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        if i == 1:
            answer.append(0)
            continue
        isPrime = True
        for j in range(2, int(i**(1/2))+1):
            if i % j == 0 and i // j <= 10000000:
                answer.append(i // j)
                isPrime = False
                break
        if isPrime:
            answer.append(1)
    return answer