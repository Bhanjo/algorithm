import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num_list = [i+1 for i in range(n)]
result = []
running = -1

while(True):
    for i in range(k):
        if running == len(num_list)-1:
            running = 0
        else:
            running += 1

        if i == k-1 and num_list:
            result.append(num_list[running])
            num_list.remove(num_list[running])
            running -= 1

    if len(num_list) == 0:
        print("<",end='')
        for i in range(len(result)):
            if i == len(result) - 1:
                print(result[i], end='')
            else:
                print(result[i],end=', ')
        print(">",end='')
        break
            
# 덱을 이용한 풀이
# from collections import deque
# n, k = map(int, input().split())
# s = deque([])
# for i in range(1, n + 1):
#     s.append(i)
# print('<', end='')
# while s:
#     for i in range(k - 1):
#         s.append(s[0])
#         s.popleft()
#     print(s.popleft(), end='')
#     if s:
#         print(', ', end='')
# print('>')
