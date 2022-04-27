def solution(dirs):
    answer = 0
    pos = [5,5]
    lines = []
    for i in dirs:
        prevPos = [pos[0],pos[1]]
        if i == "U":
            pos[0] -= 1
        if i == "D":
            pos[0] += 1
        if i == "L":
            pos[1] -= 1
        if i == "R":
            pos[1] += 1
            
        if pos[0] < 0:
            pos[0] = 0
        if pos[0] > 10:
            pos[0] = 10
            
        if pos[1] < 0:
            pos[1] = 0
        if pos[1] > 10:
            pos[1] = 10
        
        if pos[0] == prevPos[0] and pos[1] == prevPos[1]:
            continue

        if [pos[0], pos[1], prevPos[0], prevPos[1]] not in lines and [prevPos[0], prevPos[1], pos[0], pos[1]] not in lines:
            answer += 1
            lines.append([pos[0], pos[1], prevPos[0], prevPos[1]])
            lines.append([prevPos[0], prevPos[1], pos[0], pos[1]])
    return answer
solution("ULURRDLLU")