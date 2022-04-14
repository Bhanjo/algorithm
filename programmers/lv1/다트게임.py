def solution(dartResult):
    answer = 0
    dart = list(dartResult)
    score = []
    for i in range(len(dart)):
        if dart[i] == '1' and dart[i+1] == '0':
            score.append(10)
        elif ('0' <= dart[i] and dart[i] <= '9'):
            if dart[i-1] == '1' and dart[i] == '0':
                continue
            score.append(int(dart[i]))
        elif dart[i] == 'S':
            score[-1] *= 1
        elif dart[i] == 'D':
            score[-1] *= score[-1]
        elif dart[i] == 'T':
            score[-1] *= score[-1]**2
        elif dart[i] == '#':
            score[-1] *= -1
        elif dart[i] == '*':
            score[-1] *= 2
            if len(score) > 1:
                score[-2] *= 2
    print(score)
    answer = sum(score)
    return answer