def cnt(logs, start, end):
    count = 0
    for log in logs:
        if log[0] < end and log[1] >= start:
            count += 1
    return count

def solution(lines):
    answer = 0
    logs = []
    
    # 로그 정보를 시작, 끝 시간으로 변환(밀리초 단위)
    for i in lines:
        date, time, duration = i.split()
        time = time.split(":")
        duration = duration.replace("s","")
        duration = float(duration) * 1000
        
        # 종료 시간을 밀리초 단위로 변환
        endSec = (int(time[0]) * 3600 + int(time[1]) * 60 + float(time[2])) * 1000
        # 시작 시간 = 종료시간 - 처리경과 시간 + 1
        startSec = endSec - duration + 1
        
        logs.append([startSec, endSec])
    
    # 초당 최대 처리량 구하기
    for i in logs:
        temp1 = cnt(logs, i[0], i[0]+1000)
        temp2 = cnt(logs, i[1], i[1]+1000)
        answer = max(answer, temp1, temp2)
    return answer