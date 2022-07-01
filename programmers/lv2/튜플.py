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

# 2회차
def solution(s):
    answer = []
    s = s.lstrip("{{").rstrip("}}").split("},{")
    for i in range(len(s)):
        s[i] = list(map(int, s[i].split(',')))
    s.sort(key=lambda x:len(x))
    for i in s:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer