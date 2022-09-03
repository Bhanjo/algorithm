import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = []
answer = 0

# 집 좌표 입력과 정렬 (이분탐색 조건: 정렬 필요)
for i in range(N):
    target = int(input())
    house.append(target)
house.sort()

# 이분 탐색
def binarySearch(start, end, house):
    global answer
    while(start <= end):
        mid = (start + end) // 2 # 설치 간격
        currentHouse = house[0]
        counter = 1
        for i in range(1, N): # 설치 가능한지 판단
            # house[i]가 현재 집에서 최소 mid만큼 떨어져 있는가
            if house[i] >= mid + currentHouse:
                counter += 1
                currentHouse = house[i]
        
        # 공유기 남음 => 범위를 더 좁게
        if counter < C:
            end = mid - 1

        # 공유기 부족 또는 딱 맞음 => 최대 거리 갱신 및 범위 넓게
        if counter >= C:
            start = mid + 1
            answer = max(answer, mid)


start = 1
end = house[-1] - house[0]
binarySearch(start, end, house)

print(answer)