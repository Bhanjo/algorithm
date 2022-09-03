from collections import deque
import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
food = []
for i in range(n):
    food.append(int(input()))

foodCnt = []
foodSet = deque()
foodDict = dict()
cnt = 0

# 딕셔너리 초기화
for i in range(d+1):
    foodDict[i] = 0

# 초기값 입력
for i in range(k):
    if foodDict[food[i]] == 0:
        cnt += 1
    foodDict[food[i]] += 1
    foodSet.append(food[i])

if foodDict[c] <= 0:
    foodCnt.append(cnt + 1)
else:
    foodCnt.append(cnt)

# 경우의 수 구하기 (투포인터)
for i in range(n):
    # 맨 앞 제거, 딕셔너리에서도 제거
    rm = foodSet.popleft()
    foodDict[rm] -= 1
    if foodDict[rm] <= 0: # set에 존재하지 않으니 cnt 감소
        cnt -= 1
    
    # 다음 초밥 넣기
    newFood = food[(i+k) % n] # 회전초밥이니 배열 초과 시 처음으로 돌아가기
    if foodDict[newFood] == 0: # 새로운 종류면 cnt 증가
        cnt += 1

    foodDict[newFood] += 1
    foodSet.append(newFood)

    # 쿠폰 넣어도 될지 판별
    if foodDict[c] <= 0:
        foodCnt.append(cnt + 1)
    else:
        foodCnt.append(cnt)

print(max(foodCnt))