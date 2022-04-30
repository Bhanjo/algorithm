from itertools import permutations

def solution(k, dungeons):
    permu = list(permutations(dungeons))
    cnt = 0
    for i in permu:
        condi = k
        temp = 0
        for j in i:
            if condi >= j[0]:
                temp += 1
                condi -= j[1]
        cnt = max(cnt, temp)
    return cnt


# dfs 이용한 풀이
answer = 0
visit = []

def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and visit[i] == 0:
            visit[i] = 1
            dfs(k - dungeons[i][1], cnt + 1, dungeons)
            visit[i] = 0

def solution(k, dungeons):
    global visit
    visit = [0] * len(dungeons)
    dfs(k, 0, dungeons)
    return answer

solution(80, [[80,20],[50,40],[30,10]])