def solution(want, number, discount):
    answer = 0
    food = {}

    for i in range(len(want)):
        food[want[i]] = number[i]
    
    for i in range(10):
        if discount[i] in food:
            food[discount[i]] -= 1
    
    for i in range(len(want)):
        if food[want[i]] != 0:
            break
        if food[want[i]] == 0 and i == len(want) - 1:
            answer = 1
    
    for i in range(1, len(discount)-9):
        if discount[i-1] in food:
            food[discount[i-1]] += 1
        if discount[i+9] in food:
            food[discount[i+9]] -= 1
        for i in range(len(want)):
            if food[want[i]] != 0:
                break
            if food[want[i]] == 0 and i == len(want) - 1:
                answer += 1

    return answer