# 1회차
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

# 2회차
def solution(want, number, discount):
    answer = 0
    foods = {}

    # 딕셔너리 초기값 세팅
    for i in range(len(number)):
        foods[want[i]] = number[i]
    
    # 1일차 세팅
    for i in range(10):
        if discount[i] in foods:
            foods[discount[i]] -= 1
    # 회원가입 가능 판별
    newFoods = list(foods.items())
    for j in range(len(newFoods)):
        if newFoods[j][1] != 0:
            break
        if j == len(want)-1:
            if newFoods[j][1] == 0:
                answer += 1
    
    # 2일차 이후 반복
    for i in range(1, len(discount) - 9):
        # 이전값 되돌리기
        if discount[i-1] in foods:
            foods[discount[i-1]] += 1
        # 끝값 넣기
        if discount[i+9] in foods:
            foods[discount[i+9]] -= 1
        
        # 회원가입 가능 판별
        newFoods = list(foods.items())
        for j in range(len(newFoods)):
            if newFoods[j][1] != 0:
                break
            if j == len(want)-1:
                if newFoods[j][1] == 0:
                    answer += 1
    return answer