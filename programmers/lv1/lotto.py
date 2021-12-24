# 프로그래머스 lv.1 로또의 최고 순위와 최저 순위
import sys
input = sys.stdin.readline


def solution(lottos, win_nums):
    answer = []
    cnt = 0  # 맞은 개수
    countLotto = [0 for i in range(2)]

    for i in win_nums:
        if i in lottos:
            cnt += 1

    countLotto[0] = cnt + lottos.count(0)
    countLotto[1] = cnt

    for i in range(len(countLotto)):
        if countLotto[i] == 6:
            answer.append(1)
        elif countLotto[i] == 5:
            answer.append(2)
        elif countLotto[i] == 4:
            answer.append(3)
        elif countLotto[i] == 3:
            answer.append(4)
        elif countLotto[i] == 2:
            answer.append(5)
        else:
            answer.append(6)

    return answer


def solution2(lottos, win_nums):

    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans], rank[ans]


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))
