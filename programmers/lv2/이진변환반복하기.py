def toBin(num):
    bi = []
    while(num):
        bi.append(str(num % 2))
        num = num // 2
    bi.reverse()
    bi = ''.join(bi)
    return bi

def solution(s):
    answer = []
    zeroCnt = 0
    cicle = 0
    while(True):
        if s == "1": break
        zeroCnt += s.count("0")
        s = s.replace("0", "")
        size = len(s)
        s = toBin(size)
        cicle += 1
    answer = [cicle, zeroCnt]
    return answer

# 다른 풀이
def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:] # 0bnnn에서 0b 제외
    return [a, b]
solution("0111010")