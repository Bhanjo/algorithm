def solution(arr):
    answer = 0
    maxNum = max(arr)
    cnt = 1
    while True:
        answer = maxNum * cnt
        isPerfect = True
        for i in arr:
            if (answer % i != 0):
                cnt += 1
                isPerfect = False
                break
        if(isPerfect):
            break

    return answer