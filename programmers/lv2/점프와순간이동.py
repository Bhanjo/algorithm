def solution(n):
    ans = 0
    graph = [i for i in range(n + 1)]

    # case1 (시간초과)
    # visit = [0 for _ in range(n + 1)]
    # q = deque()
    # q.append(0)
    
    # while(q):
    #     currPos = q.popleft()
    #     jump = currPos + 1
    #     tell = (currPos * 2)
    #     if tell <= n and visit[tell] < 2:
    #         graph[tell] = min(graph[tell], graph[currPos])
    #         visit[tell] += 1
    #         q.append(tell)
    #     if jump <= n and visit[jump] < 2:
    #         graph[jump] = min(graph[jump], graph[currPos] + 1)
    #         visit[jump] += 1
    #         q.append(jump)
    
    # ans = graph[n]
    # print(ans)

    # case2 (시간초과)
    # pos = 0
    # tell = 0
    # jump = 0
    # while(tell <= n or jump <= n):
    #     tell = pos * 2
    #     jump = pos + 1
    #     if tell <= n:
    #         graph[tell] = min(graph[tell], graph[pos])
    #     if jump <= n:
    #         graph[jump] = min(graph[jump], graph[pos] + 1)
    #     pos += 1
    # ans = graph[n]

    # case3 통과
    while(n):
        if n % 2 == 0:
            n = n // 2
        else:
            n -= 1
            ans += 1
    return ans

solution(5000)