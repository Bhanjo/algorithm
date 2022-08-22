def solution(cacheSize, cities):
    answer = 0
    ch = []
    if cacheSize == 0:
        answer = len(cities) * 5
    else:
        for city in cities:
            city = city.lower()
            if len(ch) < cacheSize:
                if city not in ch:
                    ch.append(city)
                    answer += 5
                else:
                    ch.pop(ch.index(city))
                    ch.append(city)
                    answer += 1
            else:
                if city not in ch:
                    ch.pop(0)
                    ch.append(city)
                    answer += 5
                else:
                    ch.pop(ch.index(city))
                    ch.append(city)
                    answer += 1
    return answer

# 다른 풀이
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize) # 큐 사이즈를 cacheSize만큼 할당
    time = 0
    for i in cities:
        s = i.lower()
        # cache의 maxlen에 의해 사이즈 초과시 자동으로 맨 앞 pop 실행됨
        if s in cache:
            cache.remove(s) # 큐에서 s에 해당하는 요소 삭제
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time

# 2회차
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    if cacheSize == 0:
        return len(cities)*5
    for i in cities:
        i = i.lower()
        # 캐시 일치 판단
        if i in cache:
            cache.remove(i)
            cache.append(i)
            answer += 1
        else:
            if len(cache) < cacheSize:
                cache.append(i)
            else:
                cache.popleft()
                cache.append(i)
            answer += 5
    return answer