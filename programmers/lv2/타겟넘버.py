def solution(numbers, target):
    answer = 0
    length = len(numbers)

    def dfs(index, hap):
        if(index == length):
            if(hap == target):
                nonlocal answer
                answer += 1
            return
        dfs(index + 1, hap + numbers[index])
        dfs(index + 1, hap - numbers[index])

    dfs(0,0)
    return answer
solution([1,1,1,1,1],3)
