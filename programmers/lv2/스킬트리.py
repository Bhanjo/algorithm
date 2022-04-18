def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        skills = list(map(str, skill))
        isCorrect = True
        for j in i:
            if j not in skills:
                continue
            if skills[0] != j:
                isCorrect = False
                break
            else:
                skills.pop(0)
        if isCorrect:
            answer += 1
    return answer