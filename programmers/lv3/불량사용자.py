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