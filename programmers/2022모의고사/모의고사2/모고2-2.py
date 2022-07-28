# 100/100
from collections import deque

def solution(topping):
    topping = deque(topping)
    answer = 0

    arr1 = dict()
    arr1Items = 0

    arr2 = dict()
    for i in topping:
        if i not in arr2:
            arr2[i] = 1
        else:
            arr2[i] += 1
    arr2Items = len(arr2)

    while(topping):
        t = topping.popleft()
        if arr2[t] > 0:
            arr2[t] -= 1
        if arr2[t] <= 0:
            arr2Items -= 1

        if t not in arr1:
            arr1[t] = 1
            arr1Items += 1
        
        if arr1Items == arr2Items:
            answer += 1
    return answer