from itertools import combinations


def solution(line):
    pairs = list(combinations(line, 2))
    cross = set()
    for p in pairs:
        a,b,e = p[0][0], p[0][1], p[0][2]
        c,d,f = p[1][0], p[1][1], p[1][2]
        if a * d == b * c: continue
        x = (b*f - e*d) / (a * d - b * c)
        y = (e*c - a*f) / (a * d - b * c)
        if x == int(x) and y == int(y):
            cross.add((int(x),int(y)))

    xPos = [i[0] for i in cross]
    yPos = [i[1] for i in cross]
    xMax = max(xPos)
    xMin = min(xPos)
    yMax = max(yPos)
    yMin = min(yPos)
    answer = ['.' * (xMax-xMin+1)] * (yMax-yMin+1)

    for i in cross:
        x, y = i[0], i[1]
        answer[yMax-y] = answer[yMax-y][:x-xMin] + '*' + answer[yMax-y][x-xMin+1:]
    answer = [''.join(i) for i in answer]
    for i in answer:
        print(i)
    return answer

solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])
# solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]])