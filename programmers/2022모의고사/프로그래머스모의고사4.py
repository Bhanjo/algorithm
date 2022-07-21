from collections import deque

# 25 dfs?
def solution(beginning, target):
    answer = 10**8
    visit = [[0]*(len(beginning[0])) for _ in range(len(beginning))]
    q = deque()
    q.append([0,0,beginning, 0, visit])
    isReversed = False

    while(q):
        x, y, graph, cnt, visit = q.popleft()

        # 판단2 행 뒤집기
        for c in range(len(graph[0])):
            graph[x][c] = 0 if graph[x][c] == 1 else 1
        if graph == target:
            isReversed = True
            answer = min(answer, cnt)
        # print("행 뒤집기")
        # for i in graph:
        #     print(i)

        # 판단1
        for c in range(len(graph[0])):
            graph[x][c] = 0 if graph[x][c] == 1 else 1
        if graph == target:
            isReversed = True
            answer = min(answer, cnt)
        # print("원본")
        # for i in graph:
        #     print(i)

        # 판단3 열 뒤집기
        for r in range(len(graph)):
            graph[r][y] = 0 if graph[r][y] == 1 else 1
        if graph == target:
            isReversed = True
            answer = min(answer, cnt)
        # print("열 뒤집기")
        # for i in graph:
        #     print(i)


        # 아직 방문 안했으면 방문 했다 표시
        if visit[x][y] == 0:
            visit[x][y] = 1

        # 다음 경우의 수 넣기
        for i in range(len(graph)):
            for j in range(len(graph[0])):
                if visit[i][j] == 0:
                    q.append([i,j,graph,cnt+1,visit])

    # 단 한 번도 갱신x => -1
    if not isReversed:
        answer = -1
    return answer