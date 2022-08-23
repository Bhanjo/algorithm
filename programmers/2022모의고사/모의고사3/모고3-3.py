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

# 92.9
def solution(distance, scope, times):
    answer = distance
    guard = len(scope)

    for i in scope:
        i.sort()

    # 모든 경비원 순회
    for i in range(guard):
        time = times[i]
        totalTime = time[0] + time[1]
        for j in range(len(scope[i])):
            mok = scope[i][j] // totalTime
            rest = scope[i][j] % totalTime
            if 1 <= rest <= time[0]+1:
                # print('걸림', scope[i][j] % totalTime, i,j)
                temp = [i+1 for i in range(totalTime*mok, totalTime*mok+time[0])]
                for t in temp:
                    if scope[i][0] <= t <= scope[i][1]:
                        answer = min(answer, t)
    
    return answer