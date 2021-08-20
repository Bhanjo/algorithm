# # push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다

import sys
input = sys.stdin.readline

n = int(input())
queue = []
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'push':
        queue.insert(0, cmd[1])
    elif cmd[0] == 'pop':
        print(queue.pop()) if len(queue) > 0 else print(-1)
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        print(1) if len(queue) < 1 else print(0)
    elif cmd[0] == 'front':
        print(queue[len(queue)-1]) if len(queue) > 0 else print(-1)
    elif cmd[0] == 'back':
        print(queue[0]) if len(queue) > 0 else print(-1)