def solution(n, computers):
    answer = 0
    visit = [0 for _ in range(n)]

    def dfs(node, visit):
        if visit[node] == 0:
            visit[node] = 1
            for i in range(n):
                if computers[node][i] == 1:
                    dfs(i, visit)
        return

    for i in range(n):
        if visit[i] == 0:
            answer += 1
            dfs(i, visit)
    return answer

# print(solution(3, [[1,1,0],[1,1,0],[0,0,1]]))
# print(solution(3, [[1,1,0],[1,1,1],[0,1,1]]))
print(solution(5, [[1,1,1,0,0],[1,1,0,0,0],[1,0,1,0,0],[0,0,0,1,1],[0,0,0,1,1]]))