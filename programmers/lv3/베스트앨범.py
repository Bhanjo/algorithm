def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        # 해당 장르별 id와 판매량
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        # 해당 장르의 총 판매량 수
        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p
        # print(dic1, dic2)

    # 가장 많이 팔린 장르로 1차 정렬
    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        # 장르 중 많이 팔린 순으로 정렬
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer

# 파이썬 해시 => 딕셔너리
# 딕셔너리.items() => {key: value}를 [(key, value)]로 전환
solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])