def solution(A):
    maxVal = max(A)
    dict = {i for i in range(1, maxVal+2)}
    for i in A:
        if i in dict:
            dict.remove(i)

    return min(dict) if dict and min(dict) > 0 else 1