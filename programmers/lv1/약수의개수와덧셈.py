def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        nums = []
        for j in range(1, int(i**(1/2))+1):
            if i % j == 0:
                nums.append(i // j)
                if j * j != i:
                    nums.append(j)
        if len(nums) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
solution(13, 17)