import math


def solution(fees, records):
    answer = []
    baseTime, baseFee, plusTime, plusFee  = fees
    parkingDict = {}
    timeDict = {}

    for i in range(len(records)):
        records[i] = records[i].split()
    for car in records:
        h, m = car[0].split(":")
        car[0] = (int(h) * 60) + int(m)
    
    # 입출차 판단
    for car in records:
        if car[2] == "IN":
            parkingDict[car[1]] = car[0]
        elif car[2] == "OUT":
            inTime = parkingDict[car[1]]
            if car[1] in timeDict:
                timeDict[car[1]] += car[0] - inTime
            else:
                timeDict[car[1]] = car[0] - inTime
            parkingDict[car[1]] = -1

    # parkingDict에 남아있는 값 전부 빼기
    while(parkingDict):
        name, time = parkingDict.popitem()
        if time >= 0:
            if name in timeDict:
                timeDict[name] += ((23*60) + 59) - time
            else:
                timeDict[name] = ((23*60) + 59) - time
    
    # 딕셔너리 to 리스트 and 사전형 정렬
    timeDict = list(timeDict.items())
    timeDict.sort(key = lambda x : x[0])

    # 요금 계산
    for car in timeDict:
        isOver = True
        if car[1] - baseTime <= 0:
            isOver = False
        
        if isOver:
            answer.append(baseFee + (math.ceil((car[1] - baseTime) / plusTime) * plusFee))
        else:
            answer.append(baseFee)
    
    return answer

solution([1, 461, 1, 10],["00:00 1234 IN"])