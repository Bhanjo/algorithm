def solution(numbers):
    answer = []
    for item in numbers:
        binItem = list('0' + bin(item)[2:])
        if item % 2 == 0:
            binItem[-1] = '1'
        else:
            for i in range(len(binItem) - 1, -1, -1):
                if binItem[i] == '0':
                    binItem[i] = '1'
                    binItem[i + 1] = '0'
                    break
        answer.append(int(''.join(binItem),2)) # 2진수를 10진수로
    return answer
solution(7)