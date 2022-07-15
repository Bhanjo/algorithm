import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
st = [0]
answer = [-1]*n

for i in range(1, n):
    while st and nums[st[-1]] < nums[i]:
        answer[st.pop()] = nums[i]
    st.append(i)

print(*answer)