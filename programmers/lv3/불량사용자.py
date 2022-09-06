def isCorrect(user, ban):
    if len(user) != len(ban): return False

    # 유저 길이 = 밴 길이
    for i, j in zip(user, ban):
        if j == '*': continue
        if i != j:
            return False
    
    return True

answer = []

def solution(user_id, banned_id):
    global answer
    temp = []
    visit = [False for _ in range(len(user_id))]
    
    def dfs():
        global answer
        if len(temp) == len(banned_id):
            # 확인
            cnt = 0
            for a, b in zip(temp, banned_id):
                if isCorrect(a,b):
                    cnt += 1
            
            if cnt == len(banned_id):
                if set(temp) not in answer:
                    answer.append(set(temp))
            return
        
        for i in range(len(user_id)):
            if not visit[i]:
                visit[i] = True
                temp.append(user_id[i])
                dfs()
                visit[i] = False
                temp.pop()

    dfs()
    
    return len(answer)


# 2회차
import copy

def solution(user_id, banned_id):
    answer = []
    limit = len(banned_id)
    temp = []
    visit = [False for _ in range(len(user_id))]
    
    def isConsist(temp):    
        # temp 목록을 전부 *로 대체 (기준: 벤idx의 요소)
        newTemp = []
        for idx, user in enumerate(temp):
            newUser = list(user)
            if len(user) != len(banned_id[idx]):
                return False
            for i in range(len(banned_id[idx])):
                if banned_id[idx][i] == '*':
                    newUser[i] = '*'
            newTemp.append(''.join(newUser))
        
        if newTemp != banned_id:
            return False
    
        return True
    
    def permu():
        if len(temp) == limit:
            # 벤 아이디와 일치하는지 판별
            isTrue = isConsist(temp)
            if isTrue:
                newTemp = copy.deepcopy(temp)
                newTemp.sort()
                newTemp = list(set(newTemp))
                if len(newTemp) == len(banned_id) and newTemp not in answer:
                    answer.append(newTemp)
            return
        for idx in range(len(user_id)):
            if not visit[idx]:
                temp.append(user_id[idx])
                visit[idx] = True
                permu()
                visit[idx] = False
                temp.pop()
    
    permu()
    
    return len(answer)