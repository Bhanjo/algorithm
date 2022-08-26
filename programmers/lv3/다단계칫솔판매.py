def solution(enroll, referral, seller, amount):
    answer = {}
    graph = {} # 자식 = [부모]
    cost = {}
    graph["root"] = []
    cost["root"] = []
    
    for i in range(len(enroll)):
        graph[enroll[i]] = []
        cost[enroll[i]] = []
        if referral[i] == "-":
            graph[enroll[i]].append("root")
        else:
            graph[enroll[i]].append(referral[i])
    
    def dfs(user, money):
        discount = money // 10
        cost[user].append(money - discount)
        if graph[user] == 'root' or discount == 0:
            return
        # 부모로 올라가기
        for i in graph[user]:
            dfs(i, discount)
    
    for i in range(len(seller)):
        dfs(seller[i], amount[i]*100)
    
    for i in cost:
        answer[i] = sum(cost[i])
    
    printAnswer = []
    for i in answer:
        if i == 'root': continue
        printAnswer.append(answer[i])
        
    return printAnswer