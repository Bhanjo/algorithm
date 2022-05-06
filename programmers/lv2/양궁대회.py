from collections import deque


def bfs(n, info):
    res = []
    q = deque([(0, [0,0,0,0,0,0,0,0,0,0,0])])
    maxGap = 0

    while q:
        # focus = 어디에 화살을 쏠 건지
        focus, arrow = q.popleft()
        if sum(arrow) == n:
            apeach, lion = 0, 0
            for i in range(11):
                # 해당 과녁에 한 발이라도 쐈으면
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if lion > apeach:
                gap = lion - apeach
                # 최고 점수인지 판단
                if maxGap > gap:
                    continue
                if maxGap < gap:
                    maxGap = gap
                    res.clear()
                res.append(arrow)
        elif sum(arrow) > n: # 화살을 초과해서 쓴 경우
            continue
        elif focus == 10:
            # 덜 쏜 경우 해당 부분에 나머지 화살 다 쏘기
            temp = arrow.copy()
            temp[focus] = n - sum(temp)
            q.append((-1, temp))
        else:
            # 한 발 더 쏘기, focus + 1 = 다음 과녁으로 이동
            temp = arrow.copy()
            temp[focus] = info[focus] + 1
            q.append((focus + 1, temp))
            # 쏘지 않기
            temp2 = arrow.copy()
            temp2[focus] = 0
            q.append((focus + 1 , temp2))
    return res

def solution(n, info):
    winList = bfs(n, info)
    if not winList:
        return [-1]
    elif len(winList) > 1:
        return winList[-1]
    else:
        return winList[0]

solution(5, [2,1,1,1,0,0,0,0,0,0,0])