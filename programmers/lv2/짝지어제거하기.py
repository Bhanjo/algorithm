def solution(s):
    st = []
    for i in s:
        if len(st) == 0:
            st.append(i)
        else:
            if st[-1] == i:
                st.pop(-1)
            else:
                st.append(i)
    answer = 1 if len(st) == 0 else 0
    return answer