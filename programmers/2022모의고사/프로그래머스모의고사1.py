def solution(X, Y):
    answer = ''
    dic = {
        '0': 0, '1': 0, '2': 0, '3': 0, '4': 0,
        '5': 0, '6': 0, '7': 0, '8': 0, '9': 0,
    }
    nums = []

    for i in X:
        dic[i] += 1

    for i in Y:
        if dic[i] > 0:
            dic[i] -= 1
            nums.append(i)
    
    if not nums:
        answer = "-1"
        return answer

    nums.sort(reverse=True)
    if nums.count("0") == len(nums):
        nums = ["0"]
    answer = ''.join(nums)
    answer = str(answer)

    return answer