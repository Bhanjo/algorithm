def solution(nums):
    answer = len(list(set(nums)))
    if answer > len(nums) // 2:
        answer = len(nums) // 2
    return answer
print(solution([3,3,3,2,2,2]))