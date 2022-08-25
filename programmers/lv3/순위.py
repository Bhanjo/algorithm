def solution(n, results):
    answer = 0
    graph = [[0]*n for _ in range(n)]
    
    # a가 b에게 이겼으면 1 and b가 a에게 졌으면 -1
    for i in results:
        graph[i[0]-1][i[1]-1] = 1
        graph[i[1]-1][i[0]-1] = -1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # 자기 자신 혹은 이미 싸운 사람은 건너뜀 => 직접 싸우지 않은 것만 판별
                if i == j or graph[i][j] in [-1,1]:
                    continue
                # i가 k를 이김, k가 j를 이김 => i가 j를 이김 성립 => 직접 싸운 것으로 취급
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1 # i -> j 이김
                    graph[k][i] = -1 # k -> i짐
                    graph[j][k] = -1 # j -> k짐
                    graph[j][i] = -1 # j -> i 짐
    
    # 순위가 결정됐는지 판단 (자기자신 제외 => 0개수가 1개일 때)
    for i in graph:
        if i.count(0) == 1:
            answer += 1
    return answer