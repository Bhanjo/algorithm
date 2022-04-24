def solution(n, words):
    answer = []

    order, cicle = 0, 1
    usedWord = []
    prevWord = ''
    for i in words:
        order += 1
        if i not in usedWord:
            usedWord.append(i)
        else:
            answer.append(order)
            answer.append(cicle)
            break
        
        if prevWord == '':
            prevWord = i
        elif prevWord[-1] != i[0]:
            answer.append(order)
            answer.append(cicle)
            break
        else:
            prevWord = i

        if order == n:
            cicle += 1
            order = 0

    if len(answer) == 0:
        answer.append(0)
        answer.append(0)

    return answer

solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])