def solution(s):
    answer = []
    s = s.lstrip('{').rstrip('}').split('},{')
    s.sort(key = lambda x : len(x))
    for i in s:
        tp = i.split(',')
        for t in tp:
            if int(t) not in answer:
                answer.append(int(t))
    return answer