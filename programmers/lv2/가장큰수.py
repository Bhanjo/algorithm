def solution(numbers):
    arr = list(map(str,numbers))
    arr.sort(key=lambda x:x*3, reverse = True)
    return str(int(''.join(arr)))

solution([9,938])