def convertNum (num, digit):
    converted = []
    if num == 0:
        converted.append(0)
    while(num):
        rest = num % digit
        if rest == 10:
            converted.append('A')
        if rest == 11:
            converted.append('B')
        if rest == 12:
            converted.append('C')
        if rest == 13:
            converted.append('D')
        if rest == 14:
            converted.append('E')
        if rest == 15:
            converted.append('F')
        if rest < 10:
            converted.append(rest)
        num = num // digit
    converted.reverse()
    return converted

def solution(n, t, m, p):
    answer = ''
    num = 0
    rotate = 0
    while(len(answer) < t):
        transNum = convertNum(num, n)
        for i in transNum:
            if rotate % m == (p-1) and len(answer) < t:
                answer += str(i)
            rotate += 1
        num += 1

    answer = answer.upper()
    print("ans = ", answer)
    return answer

solution(2,4,2,1)
solution(16,16,2,1)

# 2회차
def changeNum(base, num): # base진법으로 num 바꾸기
    arr = []
    alpha = ['A', 'B', 'C', 'D', 'E', 'F']
    if num == 0:
        return [0]
    
    while(num > 0):
        etc = num % base
        if 10 <= etc <= 15:
            etc = alpha[etc % 10]
        arr.append(etc)
        num = num // base
    
    return arr[::-1]

def solution(n, t, m, p):
    answer = []
    nums = []
    cnt = 0
    
    while(len(nums) <= 100000):
        temp = changeNum(n,cnt)
        nums.extend(temp)
        cnt += 1
    
    idx = p-1
    for i in range(t):
        answer.append(str(nums[idx]))
        idx += m
        
    return ''.join(answer)