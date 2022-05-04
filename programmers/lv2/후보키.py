from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    combi = []
    for i in range(1, col + 1):
        # extend를 통해 요소만 이어서 붙임
        combi.extend(combinations(range(col), i))
    
    unique = []
    for i in combi:
        # 릴레이션의 각 행(item) 순환
        # 조합 i를 순환(key)하면서 item[key]를 찾아 튜플화
        temp = [tuple([item[key] for key in i]) for item in relation]
        
        # 중복 없다면
        if len(set(temp)) == row:
            isCorrect = True
            for info in unique:
                # info가 조합 i의 부분집합인지 확인
                if set(info).issubset(set(i)):
                    isCorrect = False
                    break
            if isCorrect:
                unique.append(i)
    return len(unique)

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])