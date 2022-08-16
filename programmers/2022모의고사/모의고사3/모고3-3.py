#  38 / 100
def solution(distance, scope, times):
    answer = distance
    for i in range(len(scope)):
        time = times[i][0] + times[i][1]
        for j in range(1, distance, time):
            # 일 하는 시간 [start, end]
            work = [j, j + times[i][0] - 1]
            # 일 하는 시간에 범위 안에 탐색 범위가 있다면
            if work[0] <= scope[i][0] <= work[1]:
                answer = min(answer, scope[i][0])
            if work[0] <= scope[i][1] <= work[1]:
                answer = min(answer, scope[i][1])

    return answer