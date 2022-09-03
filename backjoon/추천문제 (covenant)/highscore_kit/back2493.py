import sys
input = sys.stdin.readline

n = int(input())
tops = list(map(int,input().split()))
answer = []
st = [] # 요소 = [index, tops[index]]

for i in range(n):
    while(len(st) > 0):
        last = st[-1]
        if last[1] > tops[i]:
            answer.append(last[0]+1)
            st.append([i, tops[i]])
            break
        else:
            st.pop()
    if len(st) == 0:
        st.append([i, tops[i]])
        answer.append(0)

print(*answer)

# 2회차
n = int(input())
tops = list(map(int, input().split()))
st = []
answer = []

for idx, top in enumerate(tops):
    if len(st) == 0:
        st.append([idx+1, top])
        answer.append(0)
        continue
    if st[-1][1] > top:
        answer.append(st[-1][0])
    else:
        while(st and st[-1][1] <= top):
            st.pop()
        if len(st) == 0:
            answer.append(0)
        else:
            answer.append(st[-1][0])
    st.append([idx+1, top])

print(*answer)