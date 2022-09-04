def timeChange(goal):
    hour = goal // 60
    if hour < 10: hour = '0' + str(hour)
    else: hour = str(hour)

    mini = goal % 60
    if mini < 10: mini = '0' + str(mini)
    else: mini = str(mini)
    
    return hour + ':' + mini

def solution(n, t, m, timetable):
    answer = ''
    
    # 크루 도착 시간을 분으로 환산
    crew = []
    for i in timetable:
        h, mi = i.split(':')
        h = int(h) * 60
        mi = int(mi) + h
        crew.append(mi)
    crew.sort(reverse=True) # pop을 위해 내림차순 정렬
    
    # 버스 도착 시간 구하기 (첫 차는 9시)
    bus = [540]
    for i in range(1, n):
        bus.append(bus[-1] + t)
    bus.sort(reverse=True) # pop을 위해 내림차순 정렬
    
    # 마지막 버스일 때까지 태울 수 있으면 다 태우기
    while(len(bus) > 1):
        comeBus = bus.pop()
        cnt = 0 # 몇 명 탔는지 확인
        
        # 버스 도착 시간에 크루들이 대기하고 있는가?
        while(crew):
            firstCrew = crew.pop()
            # 대기중인 크루 없거나 버스 정원이면 보내기
            if firstCrew > comeBus or cnt >= m:
                crew.append(firstCrew)
                break
            cnt += 1
    
    # 마지막 버스 시간 < 가장 일찍 온 사람의 시간
    if len(crew) == 0 or bus[0] < crew[-1]:
        answer = timeChange(bus.pop())
        return answer
    
    # 정원 미달?
    if m > len(crew):
        answer = timeChange(bus[0])
    
    # 정원에 딱 맞음 => 가장 마지막 사람보다 1분 빠르게 도착
    if m == len(crew):
        answer = timeChange(crew[0] - 1)
    
    # 정원 초과 => 마지막에 타는 사람보다 1분 더 빠르게 도착
    if m < len(crew):
        answer = timeChange(crew[len(crew)-m] - 1)
    
    return answer