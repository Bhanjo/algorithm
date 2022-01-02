participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    dic = dict()
    cnt = 0
    for i in participant:
        dic[hash(i)] = i
        cnt += hash(i)
    for i in completion:
        cnt -= hash(i)
    return dic[cnt]


print(solution(participant, completion))
