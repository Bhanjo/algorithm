import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visit = [False for _ in range(n)]

hap = 10**8
team = []
def dfs(target):
    global hap
    # 크기의 절반 => 방문한 팀 = 스타트, 방문 안한 팀 = 링크
    # 방문 조건은 사전순 증가 조건으로 시간 단축
    # ex) (1,2,3 / 4,5,6) == (4,5,6 / 1,2,3), (2,4,1,7 / 3,5,6,8) == (1,2,4,7 / 3,5,6,8) 이기 때문에 가능함
    if len(team) == n // 2:
        t1, t2 = 0, 0
        # 2차원 배열 순회
        # 하는 이유) (1,2,3) => (1,1), (1,2), (1,3), (2,1), (2,2) (2,3), (3,1), (3,2), (3,3) 능력치 계산 위해
        for i in range(n):
            for j in range(n):
                # 방문 했으면 1팀 안했으면 2팀
                if visit[i] and visit[j]:
                    t1 += graph[i][j]
                elif not visit[i] and not visit[j]:
                    t2 += graph[i][j]
        hap = min(hap, abs(t1-t2))
        return
    for i in range(target, n):
        if not visit[i]:
            visit[i] = True
            team.append(i)
            dfs(i)
            team.pop()
            visit[i] = False

dfs(0)
print(hap)
