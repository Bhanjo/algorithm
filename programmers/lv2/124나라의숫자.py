def solution(n):
    answer = []
    while(n > 0):
        restNum = n % 3
        n = n // 3
        if restNum == 0:
            answer.append('4')
            n -= 1
        elif restNum == 1:
            answer.append('1')
        elif restNum == 2:
            answer.append('2')
    answer.reverse()
    return ''.join(answer)