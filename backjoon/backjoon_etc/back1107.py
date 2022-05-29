import sys
input = sys.stdin.readline

n = int(input())
buttonCount = int(input())
breakButtons = list(map(int,input().split()))
answer = abs(n - 100)

# 원하는 채널은 50만 이하 단, 채널 자체는 무한대 => 1백만 범위
for i in range(1000001):
    num = str(i)
    numLength = len(num)
    for j in range(numLength):
        # 숫자에 고장난 버튼 있으면 다음 숫자 진행
        if int(num[j]) in breakButtons:
            break
        # 끝까지 도달 => 고장난 버튼 x => 최소 숫자 계산하기
        if j == numLength - 1:
            answer = min(answer, abs(i - n) + numLength)

print(answer)