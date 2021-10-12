from collections import deque

graph_list = [[], [2, 3, 4], [1, 5], [1, 6, 7],
              [1, 8], [2, 9], [3, 10], [3], [4], [5], [6]]
root = 1


def bfs(graph, root):
    visit = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visit:
            print('현재', n)
            visit.append(n)
            queue += graph[n]
    return visit


print(bfs(graph_list, root))
