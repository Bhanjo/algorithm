def solution(N, stages):
    answer = []
    rank = [[0,0]] * (N+1)

    for i in range(1, N+1):
        rank[i] = [stages.count(i), i]
        goal = 0
        for j in stages:
            if j >= i:
                goal += 1
        rank[i][0] = rank[i][0] / goal if (goal > 0) else 0

    sortRank = rank[1:]
    sortRank.sort(key = lambda x:x[0], reverse=True)

    for i in range(len(sortRank)):
        answer.append(sortRank[i][1])

    return answer
solution(5, [2,1,2,6,2,4,3,3])