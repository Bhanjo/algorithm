# dfs 알고리즘 기초

graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']


def stack_dfs(graph, start_node):  # stack을 이용한 방법
    not_visited, visited = list(), list()
    not_visited.append(start_node)

    while not_visited:
        node = not_visited.pop()
        if node not in visited:
            print(node)
            visited.append(node)
            not_visited.extend(graph[node])

    return visited


# stack_dfs(graph, 'A')

def recursive_dfs(graph, start, visited=[]):  # 재귀 dfs
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            recursive_dfs(graph, node, visited)
            print(node)
    return visited


recursive_dfs(graph, 'A')
