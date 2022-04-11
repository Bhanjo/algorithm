def solution(n):
    answer = 0
    triple = []
    while(n > 0):
        triple.append(n % 3)
        n = n // 3
    triple.reverse()
    for i in range(len(triple)):
        answer += triple[i] * (3**i)
    return answer
solution(125)