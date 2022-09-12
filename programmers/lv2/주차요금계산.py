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

# 2회차
def toMin(time):
    arr = time.split(':')
    hour = int(arr[0]) * 60
    return hour + int(arr[1])

def solution(fees, records):
    answer = {}
    cars = {}
    
    # 자동차 입출차 기록
    for infos in records:
        info = infos.split(" ") # 시간 번호 입출차
        mini = toMin(info[0])
        
        if int(info[1]) not in cars:
            cars[int(info[1])] = [mini]
        else:
            cars[int(info[1])].append(mini)
    
    # 시간 계산
    for key in cars:
        # 마지막 출차 기록 없는지 확인
        if len(cars[key]) % 2 != 0:
            cars[key].append(toMin('23:59'))
        
        # 최종 이용 시간 계산
        while(cars[key]):
            outTime = cars[key].pop()
            inTime = cars[key].pop()
            if key not in answer:
                answer[key] = outTime - inTime
            else:
                answer[key] += outTime - inTime
    
    # 최종 비용 (fee = 기본시간 기본요금 단위시간 단위요금)
    for key in answer:
        totalTime = answer[key]
        if totalTime <= fees[0]:
            answer[key] = fees[1]
        else:
            rest = totalTime - fees[0]
            overFee = 0
            if rest % fees[2] != 0:
                overFee = (rest // fees[2]) + 1
            else: 
                overFee = rest // fees[2]
            answer[key] = fees[1] + (overFee * fees[3])
    
    answer = list(answer.items())
    answer.sort(key = lambda x:x[0])
    
    finalAnswer = []
    for key in answer:
        finalAnswer.append(key[1])
    
    return finalAnswer