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

# 2회차
answer = 0

def dfs(numbers, target, depth, hap):
    global answer
    if depth == len(numbers):
        if hap == target:
            answer += 1
        return
    dfs(numbers, target, depth + 1, hap + numbers[depth])
    dfs(numbers, target, depth + 1, hap - numbers[depth])

def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return answer