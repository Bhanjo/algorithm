"""
    KMP 알고리즘
    - 문자열 검색을 위한 알고리즘
    - O(N+M)의 시간 복잡도를 가짐
    - 파이 배열을 이용한 알고리즘
    - 실행 과정
        - 주어진 패턴에 대해 파이 배열 만들기
        - KMP 실행
            - i, j  두 개의 포인터로 진행 (i,j 둘 다 0으로 초기화)
            - i = 패턴 탐색 포인터 / j = 전체 문자열 탐색 포인터
            - 패턴[i]와 문자[j] 비교
            - 패턴[i] == 문자[j] && i += 1, j += 1
                - 만약, i == len(패턴) && 원하는 패턴 찾은 것 => 패턴의 시작 index를 저장
            - 패턴[i] == 문자[j] || i = Pi[i-1]

    파이 배열
    - 파이 배열의 i번째 요소 = 문자열 i번째 까지의 부분 문자열 중 접두=접미의 최대 길이
    - O(N) 시간 복잡도를 가짐
    - 예시
        - ababbab 배열 존재
        - [i, 부분 문자열, Pi[i]] 가정
        - [0, a, 0]
        - [1, ab, 0]
        - [2, aba, 1] << a = a
        - [3, abab, 2] << ab = ab
        - [4, ababba, 1] << a = a
        - [4, ababbab, 2] << ab = ab
    - 실행 과정
        - i, j 두 개의 포인터로 진행
        - i = 어디까지 일치하는지 표시 / j = 탐색 위치 표시
        - i = 0, j = 1로 초기화
            (파이[0]은 항상 0이기 때문, 한 글자 짜리에는 접두, 접미 존재 안함)
        - pattern이 주어질 때 pattern[i], pattern[j] 비교
        - pattern[i] == pattern[j] && i += 1, j += 1, Pi[j] = i
        - pattern[i] == pattern[j] || i = Pi[i-1]
    
    예시 문제
    - 백준 1786, 16916
"""

# 파이 배열
def PiArray(pattern):
    table = [0 for _ in range(len(pattern))]
    i = 0
    for j in range(1, len(pattern)):
        # pattern[i] != pattern[j] 의 경우
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i-1]
        
        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i
    return table

# 결과: [0, 0, 1, 2, 0, 1, 2]
# print(PiArray('ababbab'))

# KMP 알고리즘
def kmp(word, pattern):
    # 1. 파이 배열 만들기
    table = PiArray(pattern)

    # 2. kmp 실행
    result = []
    i = 0
    for j in range(len(word)):
        # 패턴[i] != 문자[j]
        while i > 0 and pattern[i] != word[j]:
            i = table[i-1]
        
        # 패턴[i] == 문자[j]
        if pattern[i] == word[j]:
            i += 1
            # i가 끝까지 진행됨 => 패턴 찾음 => 패턴의 시작 인덱스를 저장
            if i == len(pattern):
                result.append(j-i+1)
                i = table[i-1]
    return result

# 결과: [0,2,4]
print(kmp('abababab', 'abab'))