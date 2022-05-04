# 완전 탐색 풀이 (효율 테스트 탈락)
# def solution(info, query):
#     answer = []
#     info = [list(i.split()) for i in info]
#     query = [list(i.split()) for i in query]
#     for i in range(len(query)):
#         query[i] = query[i][:1] + query[i][2:3] + query[i][4:5] + query[i][6:]
    
#     infoSet = {}
#     for i in range(len(info)):
#         infoSet[i] = info[i]
    
#     for i in query:
#         cnt = 0
#         for key, value in infoSet.items():
#             if int(value[-1]) >= int(i[-1]):
#                 isCorrect = True
#                 for idx in range(len(i[:-1])):
#                     if i[idx] == '-':
#                         continue
#                     if i[idx] != value[idx]:
#                         isCorrect = False
#                         break
#                 if isCorrect:
#                     cnt += 1
#         answer.append(cnt)
        
#     return answer


# 이진 탐색 (효율 테스트 탈락)
from bisect import bisect_left
from itertools import combinations

def solution(info, query):
    answer = []
    infoDict = {}
    for i in range(len(info)):
        infos = info[i].split()
        myKey = infos[:-1]
        myVal = infos[-1]
        for j in range(5):
            # 모든 조합 생성
            for com in combinations(myKey, j):
                temp = ''.join(com)
                # 조합 temp가 딕셔너리에 있는지 판별
                if temp in infoDict:
                    infoDict[temp].append(int(myVal))
                else:
                    infoDict[temp] = [int(myVal)]
    
    # 이진 탐색을 위해 value 정렬
    for k in infoDict:
        infoDict[k].sort()
    
    for q in query:
        myQuery = q.split()
        queryValue = myQuery[-1]
        # and 및 - 제거
        queryKey = myQuery[:1] + myQuery[2:3] + myQuery[4:5] + myQuery[6:-1]
        while '-' in queryKey:
            queryKey.remove('-')
        
        queryKey = ''.join(queryKey)

        if queryKey in infoDict:
            scores = infoDict[queryKey]
            # 이진탐색, queryValue가 scores에 있는지 판단, 있다면 왼쪽 index 반환
            if scores:
                idx = bisect_left(scores, int(queryValue))
                answer.append(len(scores) - idx) # 전체에서 value 이상인 값 저장
        else:
            answer.append(0)

    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])