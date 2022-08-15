def solution(str1, str2):
    answer = 0
    check = ['1','2','3','4','5','6','7','8','9','0', ' ', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', ';', ':', '"', "'", ',', '<', '.', '>', '/', '?']
    str1 = str1.upper()
    str2 = str2.upper()
    str1Word = [str1[i:i+2] for i in range(len(str1) - 1)]
    str2Word = [str2[i:i+2] for i in range(len(str2) - 1)]
    cross = {}
    crossSize = 0
    union = {}
    unionSize = 0
    
    for i in str1Word:
        if i[0] not in check and i[1] not in check:
            a = str1Word.count(i)
            b = str2Word.count(i)
            if min(a,b) > 0:
                cross[i] = min(a,b)
            union[i] = str1Word.count(i)
            
    for i in str2Word:
        if i[0] not in check and i[1] not in check:
            if i in str1Word:
                union[i] = max(union[i], str2Word.count(i))
            elif i in str2Word:
                union[i] = str2Word.count(i)
    
    crossSize = sum(cross.values())
    unionSize = sum(union.values())
    answer = int((crossSize / unionSize) * 65536) if crossSize > 0 or unionSize > 0 else (1*65536)
    print(cross)
    print(union)
    print(answer)
    return answer

solution("ABC", "abbb")
# solution("aa1+aa2", "AA12")

# 다른 풀이
from collections import Counter

def solution(str1, str2):
    str1_low = str1.lower()
    str2_low = str2.lower()
    
    str1_lst = []
    str2_lst = []
    
    # 알파벳이면 리스트에 삽입
    for i in range(len(str1_low)-1):
        if str1_low[i].isalpha() and str1_low[i+1].isalpha():
            str1_lst.append(str1_low[i] + str1_low[i+1])
    for j in range(len(str2_low)-1):
        if str2_low[j].isalpha() and str2_low[j+1].isalpha():
            str2_lst.append(str2_low[j] + str2_low[j+1])
    
    # Counter는 원소를 key로 하고 개수를 item으로 한다
    Counter1 = Counter(str1_lst)
    Counter2 = Counter(str2_lst)
    
    # Counter는 집합 관계를 만들 수 있다
    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())
    
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)

# 2회차
def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    listA = []
    listB = []
    dic = {}
    
    # 나눈 글자가 알파벳일 때만 리스트에 추가
    for i in range(len(str1)-1):
        word = str1[i:i+2]
        if word.isalpha():
            listA.append(word)
    for i in range(len(str2)-1):
        word = str2[i:i+2]
        if word.isalpha():
            listB.append(word)
    
    # 다중집합의 교집합 합집합 판별
    for i in listA:
        countA = listA.count(i)
        countB = listB.count(i)
        if i not in dic: 
                dic[i] = [min(countA,countB), max(countA,countB)]
    for i in listB: # listB에만 있는 요소들 추가
        if i not in dic:
            dic[i] = [0,listB.count(i)]
    
    cross = 0
    uni = 0
    for i in dic:
        cross += dic[i][0]
        uni += dic[i][1]
    
    answer = int((cross/uni)*65536) if uni != 0 else 65536
    return answer