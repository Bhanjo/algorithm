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