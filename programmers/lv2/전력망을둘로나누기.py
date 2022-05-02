WIRES = []
visit = []
div = 0

def dfs(x):
    global div
    if visit[x] == 0:
        div += 1
        visit[x] = 1
        for i in WIRES:
            if i[0] == x:
                dfs(i[1])
            elif i[1] == x:
                dfs(i[0])

def solution(n, wires):
    answer = 10**10
    global WIRES, visit, div

    for i in range(1, n):
        WIRES = wires[0:i - 1] + wires[i:]
        visit = [0] * (n+1)
        counters = []
        for i in range(1, n + 1):
            if visit[i] == 0:
                dfs(i)
                counters.append(div)
                div = 0
        answer = min(answer, (max(counters) - min(counters)))

    return answer

solution(4,[[1,2],[2,3],[3,4]])