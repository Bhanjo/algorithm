def solution(numbers):
    answer = -1
    nums = [1,2,3,4,5,6,7,8,9,0]
    for i in numbers:
        nums.remove(i)
    print(sum(nums))
    return answer