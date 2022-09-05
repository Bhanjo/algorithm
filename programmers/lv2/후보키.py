from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    combi = []
    unique = []

    # index 기준으로 조합 만들기
    # 0~(col-1) 까지 1개 조합, 2개 조합...
    for i in range(1, col + 1):
        # extend를 통해 요소만 이어서 붙임
        combi.extend(combinations(range(col), i))
    
    for i in combi:
        # column 기준으로 튜플화 => 학번 튜플, 이름 튜플, 전공 튜플, ... , (학번,이름) 튜플...
        # 릴레이션의 각 row를 순회 (for item in relation)
        # => 조합 i의 각 요소를 key로 가짐 row[i] 값을 튜플에 삽입 => row[i]가 모여 튜플 temp[index] 완성
        # => row 끝까지 가면 temp 완성 => temp[index]가 모여 temp 완성
        temp = [tuple([item[key] for key in i]) for item in relation]
        
        # 중복 없다 => 유일성 만족
        if len(set(temp)) == row:
            isCorrect = True
            # 조합 i의 최소성 만족 판별
            for info in unique:
                # i에 info(유니크key)가 포함되어있다 => 최소성 만족x
                if set(info).issubset(set(i)):
                    isCorrect = False
                    break
            if isCorrect:
                unique.append(i)
    return len(unique)

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])