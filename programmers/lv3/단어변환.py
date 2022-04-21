from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    cost = dict()
    visit = dict()
    
    cost[begin] = 0
    for i in range(len(words)):
        cost[words[i]] = 0
        visit[words[i]] = False

    if target not in words:
        return answer
    
    q.append(begin)
    if begin in words:
        visit[begin] = True

    while(q):
        popWord = q.popleft()
        if popWord == target:
            answer = cost[popWord]

        for i in words:
            differCnt = 0
            if visit[i] == False:
                for j in range(len(popWord)):
                    if i[j] != popWord[j]:
                        differCnt += 1
                        if differCnt > 1: break
                if differCnt <= 1:
                    q.append(i)
                    cost[i] += cost[popWord] + 1
                    visit[i] = True
    return answer

print(solution("hit", "hot", ["hit", "hot", "lot"]))