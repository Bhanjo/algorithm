def solution(number, k):
    st = []
    for num in number:
        if len(st) == 0:
            st.append(num)
            continue
        if k > 0:
            while(st[-1] < num):
                k -= 1
                st.pop(-1)
                if (len(st) == 0 or k <= 0):
                    break
        st.append(num)
    st = st[:len(st) - k]  if k > 0 else st
    print(st)
    return ''.join(st)

# solution("4177252841", 4)
solution("9876", 2)

# 2회차
def solution(number, k):
    answer = ''
    st = []
    cnt = 0
    
    for i in number:
        if len(st) == 0:
            st.append(i)
            continue
        while len(st) > 0 and st[-1] < i and cnt < k:
            st.pop()
            cnt += 1
        st.append(i)
    
    while cnt < k:
        cnt += 1
        st.pop()
    
    return ''.join(st)