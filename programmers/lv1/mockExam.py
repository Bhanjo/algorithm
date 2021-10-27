# 프로그래머스 Lv1 완전탐색 모의고사
def solution(answers):
    answer = []
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    rank = [0]*3
    for i in range(len(answers)):
        if person1[i % 5] == answers[i]:
            rank[0] += 1
        if person2[i % 8] == answers[i]:
            rank[1] += 1
        if person3[i % 10] == answers[i]:
            rank[2] += 1
    cnt = rank.count(max(rank))
    if cnt == 1:
        answer.append(rank.index(max(rank)) + 1)
    else:
        for i in range(len(rank)):
            if rank[i] == max(rank):
                answer.append(i+1)
    return answer
