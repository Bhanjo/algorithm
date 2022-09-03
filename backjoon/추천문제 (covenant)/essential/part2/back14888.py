import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
calc = list(map(int, input().split()))
temp = []
maxAnswer = -10**10
minAnswer = 10**10

def hap(temp):
    global maxAnswer
    global minAnswer
    st = []
    for i in range(n-1):
        st.append(nums[i+1])
        st.append(temp[i])

    ans = 0
    ans += nums[0]

    while(st):
        b = st.pop(0) # 숫자
        a = st.pop(0) # 기호
        if a == '+':
            ans += b
        if a == '-':
            ans -= b
        if a == '*':
            ans *= b
        if a == '/':
            if ans < 0:
                ans = -1 * ans
                ans = (ans // b) * -1
            else:
                ans = ans // b
    
    maxAnswer = max(maxAnswer, ans)
    minAnswer = min(minAnswer, ans)

def dfs():
    if sum(calc) == 0:
        hap(temp)
        return
    for i in range(4):
        if calc[i] > 0:
            calc[i] -= 1
            if i == 0:
                temp.append('+')
            if i == 1:
                temp.append('-')
            if i == 2:
                temp.append('*')
            if i == 3:
                temp.append('/')
            dfs()
            temp.pop()
            calc[i] += 1

dfs()
print(maxAnswer)
print(minAnswer)