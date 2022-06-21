import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)

graph = []
while True: # input을 받을 수 있을 때 까지 받기
    try:
        graph.append(int(input()))
    except:
        break

def dfs(start, end):
    if start > end: # 더이상 탐색 불가 시 종료
        return

    idx = end+1 # 나눌 기준점
    for i in range(start+1, end+1):
        if graph[start] < graph[i]: # root보다 큰 값이 있나 확인
            idx = i # 있다면 그래프를 왼쪽, 오른쪽으로 나눌 수 있음. 즉, idx = 오른쪽 노드
            break
    dfs(start+1, idx-1) # 왼쪽 탐색
    dfs(idx, end) # 오른쪽 탐색
    
    print(graph[start])

dfs(0, len(graph)-1)