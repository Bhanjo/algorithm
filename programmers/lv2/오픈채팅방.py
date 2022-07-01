def solution(record):
    answer = []
    names = {}
    for i in record:
        userInfo = list(i.split(" "))
        if len(userInfo) == 3:
            names[userInfo[1]] = userInfo[2]
            
    for i in record:
        #  [상태, id, 닉네임]
        info = i.split(" ")
        if info[0] == 'Enter':
            answer.append([info[1], '님이 들어왔습니다.'])
        elif info[0] == 'Leave':
            answer.append([info[1], '님이 나갔습니다.'])

    ans = []
    for i in answer:
        nickname = names[i[0]]
        ans.append(''.join([nickname, i[1]]))
    return ans

# 2회차
def solution(record):
    answer = [] # uid, 멘트
    users = dict()
    for i in record:
        info = list(map(str, i.split())) # cmd, uid, name 혹은 cmd, uid
        if info[0] == 'Leave':
            answer.append([info[1], '님이 나갔습니다.'])
        else:
            if info[1] not in users: # 첫 방문이면 users에 추가
                users[info[1]] = info[2]
            if info[0] == 'Enter':
                if users[info[1]] != info[2]: # 이미 왔던 사람이 닉네임 바꿔서 왔는지 판단
                    users[info[1]] = info[2]
                answer.append([info[1], '님이 들어왔습니다.'])
            if info[0] == 'Change':
                users[info[1]] = info[2]
                
    ans = []
    for i in answer:
        ans.append(users[i[0]]+i[1])
    return ans