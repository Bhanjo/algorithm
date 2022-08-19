import math

def solution(progresses, speeds):
    answer = []
    st = []
    for i in range(len(speeds)):
        day = 100 - progresses[i]
        fin = int(math.ceil(day / speeds[i]))
        # 스택이 비어있거나 스택 최대값 >= 계산값일 때
        if len(st) == 0 or max(st) >= fin:
            st.append(fin)
        else:
            answer.append(len(st))
            st = []
            st.append(fin)
    answer.append(len(st))
    return answer