def solution(n, results):
    answer = 0
    graph = [[0]*(n+1) for _ in range(n+1)]
    
    # a가 b에게 이겼으면 1 and b가 a에게 졌으면 -1
    for win, loose in results:
        graph[win][loose] = 1
        graph[loose][win] = -1
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                # 자기 자신 혹은 이미 싸운 사람은 건너뜀 => 직접 싸우지 않은 것만 판별
                if i == j or graph[i][j] in [-1,1]: continue
                # i가 k를 이김, k가 j를 이김 => i가 j를 이김 성립 => 직접 싸운 것으로 취급
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1 # i -> j 이김
                    graph[j][i] = -1 # j -> i 짐
    
    # 순위가 결정됐는지 판단 (자기 자신 포함 0개수 2개 이하일 때, index0도 그래프에 있기 때문)
    for i in graph:
        if i.count(0) <= 2:
            answer += 1
    return answer