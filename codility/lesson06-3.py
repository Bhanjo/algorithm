def solution(A):
    A.sort()
    for i in range(len(A)-2):
        P = A[i]
        Q = A[i+1]
        R = A[i+2]
        if P+Q > R and Q+R > P and R+P > Q:
            return 1
    return 0
    pass
