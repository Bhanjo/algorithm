import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(5)]
answer = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,depth,nums):
    # 5번 순환했으면 답 갱신
    if depth == 5:
        if nums not in answer:
            answer.append(nums)
        return

    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < 5 and 0 <= my < 5:
            dfs(mx,my,depth+1,nums+str(graph[mx][my]))


for i in range(5):
    for j in range(5):
        dfs(i,j,0, str(graph[i][j]))

print(len(answer))