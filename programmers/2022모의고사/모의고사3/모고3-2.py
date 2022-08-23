#  100 / 100
def solution(ingredient):
    answer = 0
    st = []
    for i in ingredient:
        st.append(i)
        # 마지막이 빵, 대기열 = 4
        if len(st) >= 4 and st[-1] == 1:
            temp = st[len(st)-4:len(st)]
            if temp == [1,2,3,1]:
                answer += 1
                for i in range(4):
                    st.pop()

    return answer

# 2회차
def solution(ingredient):
    answer = 0
    st = []
    for i in ingredient:
        st.append(i)
        # 최근에 빵 들어오고 재료가 4개 이상 들어옴
        if i == 1 and len(st) >= 4:
            temp = st[len(st)-4: len(st)]
            if temp == [1,2,3,1]:
                answer += 1
                for i in range(4):
                    st.pop()
    return answer