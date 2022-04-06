def solution(n, lost, reserve):
    newReserve = set(reserve) - set(lost)
    newLost = set(lost) - set(reserve)
    for i in newReserve:
        if i - 1 in newLost:
            newLost.remove(i-1)
            continue
        if i + 1 in newLost:
            newLost.remove(i+1)
    n -= len(newLost)
    return n

solution(5,[2,4],[1,3,5])