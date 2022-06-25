def solution(routes):
    answer = 0
    routes.sort(key = lambda x:x[1])
    end = -30001

    for i in range(len(routes)):
        start = routes[i][0]
        if end < start:
            end = routes[i][1]
            answer += 1
    return answer