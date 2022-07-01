answer = []
def checkNum(s):
    if s == 'zero':
        answer.append('0')
    elif s == 'one':
        answer.append('1')
    elif s == 'two':
        answer.append('2')
    elif s == 'three':
        answer.append('3')
    elif s == 'four':
        answer.append('4')
    elif s == 'five':
        answer.append('5')
    elif s == 'six':
        answer.append('6')
    elif s == 'seven':
        answer.append('7')
    elif s == 'eight':
        answer.append('8')
    elif s == 'nine':
        answer.append('9')

def solution(s):
    for i in range(len(s)):
        if s[i] >= '0' and s[i] <= '9':
            answer.append(s[i])
            continue
        else:
            word = []
            for j in range(i,i+5):
                if j < len(s):
                    word.append(s[j])
                    checkNum(''.join(word))
    return int(''.join(answer))

solution("oneseveneightfoursixeight")

# 2회차
def solution(s):
    answer = ''
    word = ''
    alphabets = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3',
        'four': '4', 'five': '5', 'six': '6', 'seven': '7',
        'eight': '8', 'nine': '9'
    }
    for i in s:
        if '0' <= i <= '9':
            answer += i
        else:
            word += i
        if word in alphabets:
            answer += alphabets[word]
            word = ''
    return int(answer)