from itertools import combinations

def solution(orders, course):
    answer = []
    orderDict = {}
    # 모든 조합 생성
    for order in orders:
        for food in range(len(order)):
            combi = list(combinations(order, food+1))
            for i in combi:
                i = list(i)
                i.sort()
                i = ''.join(i)
                if i not in orderDict:
                    orderDict[i] = 1
                else:
                    orderDict[i] += 1

    # 코스 수에 따른 조합 판단
    for num in course:
        orderTuple = orderDict.items()
        courseItem = []
        maxOrder = 0
        for od in orderTuple:
            # 코스 수 일치 and 주문 수량 >= 2
            if len(od[0]) == num and od[1] >= 2:
                appendOd = od
                if len(courseItem) == 0:
                    courseItem.append(appendOd)
                    maxOrder = appendOd[1]
                elif appendOd[1] > maxOrder:
                    courseItem = [appendOd]
                    maxOrder = appendOd[1]
                elif appendOd[1] == maxOrder:
                    courseItem.append(appendOd)
        
        for i in courseItem:
            answer.append(i[0])
    answer.sort()
    return answer

# 다른 풀이
from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        for menu_li in orders:
            # orders에 있는 주문들에 대해 조합 list 생성
            for li in combinations(menu_li, k):
                # 조합 item에 대해 정렬 후 append
                res = ''.join(sorted(li))
                candidates.append(res)
        
        # k개의 조합에 대한 코스 중 가장 많이 나온 item 순으로 정렬
        sorted_candidates = Counter(candidates).most_common()
        # 후보들 중 cnt가 2 이상이고 맨 앞에 있는 아이템의 숫자(최다출현)과 같으면 해당 메뉴를 추가
        answer += [menu for (menu, cnt) in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    return sorted(answer)

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
# solution(["XYZ", "XWY", "WXA"], [2,3,4])

# 2회차
from itertools import combinations

def solution(orders, course):
    answer = []
    combi = {} # 조합에 대한 등장 횟수 카운트
    for i in range(len(orders)-1):
        order1 = set(list(orders[i]))
        for j in range(i+1, len(orders)):
            order2 = set(list(orders[j]))
            # 1,2의 교집합 구하기
            cross = list(order1 & order2)
            cross.sort()
            # 교집합을 통해서 조합 추출
            for idx in range(len(cross)+1):
                sub = list(combinations(cross,idx))
                for foods in sub:
                    foods = ''.join(foods)
                    if foods not in combi:
                        combi[foods] = 1
                    else:
                        combi[foods] += 1
    for c in course:
        candidate = []
        maxValue = 0
        for i in combi: # 조합별 주문 횟수
            if len(i) == c:
                if combi[i] == maxValue:
                    candidate.append(i)
                elif combi[i] > maxValue:
                    maxValue = combi[i]
                    candidate = [i]
        answer.extend(candidate)
        answer.sort()
    return answer