import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    commend = input().split()
    if commend[0] == 'push':
        stack.append(int(commend[1]))
    elif commend[0] == 'pop':
        print(stack.pop()) if len(stack) > 0 else print(-1)
    elif commend[0] == 'size':
        print(len(stack))
    elif commend[0] == 'empty':
        print(0) if len(stack) > 0 else print(1)
    elif commend[0] == 'top':
        print(stack[len(stack)-1]) if len(stack) > 0 else print(-1)

# 해설
# 스택은 후입선출(LIFO) 구조다
# push: 스택 끝에 데이터를 삽입
# pop: 스택 끝의 데이터를 꺼냄
# size: 현재 스택에 있는 데이터 개수를 출력
# empty: 스택이 비어있는지 판단
# top: 끝 데이터를 읽음(꺼내지는 않는다)