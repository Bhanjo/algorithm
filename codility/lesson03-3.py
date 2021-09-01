def solution(A):
    hap = []
    for i in range(len(A)-1):
        sum1 = 0
        sum2 = 0
        for j in range(0, i+1):
            sum1 += A[j]
        for k in range(i+1, len(A)):
            sum2 += A[k]
        hap.append(abs(sum1 - sum2))
    return min(hap)
    pass

# 풀이2


def solution(A):
    hap = []
    sum1 = 0
    sum2 = sum(A)
    for i in range(len(A)-1):
        sum1 += A[i]
        sum2 -= A[i]
        hap.append(abs(sum1 - sum2))
    return min(hap)
    pass
