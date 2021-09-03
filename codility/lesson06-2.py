def solution(A):
    A.sort()
    R1 = A[len(A)-1]

    # 비교1
    Q1 = A[len(A)-2]
    P1 = A[len(A)-3]

    # 비교2
    P2 = A[0]
    Q2 = A[1]

    result = P1*Q1*R1 if P1*Q1*R1 > P2*Q2*R1 else P2*Q2*R1
    return result
    pass
