def solution(tickets):
    answer = []
    graph = {}
    
    for start, end in tickets:
        if start not in graph:
            graph[start] = [end]
        else:
            graph[start].append(end)
    
    # "역순" 정렬 => stack pop을 통해 알파벳 순으로 접근하기 위해
    for i in graph:
        graph[i].sort(reverse=True)
    
    stack = ["ICN"]
    # 완전 탐색
    while(stack):
        top = stack.pop()
        # (graph에 top 존재x => 가장 마지막 위치, graph[top] 존재x) => 더이상 갈 수 있는 곳 없음 => 정답에 추가
        if top not in graph or not graph[top]:
            answer.append(top)
        else:
            # 더 들어갈 수 있으면 pop했던거 다시 집어넣고 다음 목적지로 이동
            stack.append(top)
            stack.append(graph[top].pop())
    
    
    return answer[::-1]