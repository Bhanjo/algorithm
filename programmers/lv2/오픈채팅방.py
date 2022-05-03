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