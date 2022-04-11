def solution(new_id):
    answer = new_id.lower()
    answer = answer.replace("~","").replace("#","").replace("@","").replace("$","").replace("%","").replace("^","").replace("&","").replace("*","").replace("(","").replace(")","").replace("=","").replace("+","").replace("[","").replace("{","").replace("]","").replace("}","").replace(":","").replace("?","").replace("!","").replace(",","").replace("<","").replace(">","").replace("/","")
    newWord = ''
    if len(answer) == 1:
        newWord = answer
    else:
        for i in range(len(answer) - 1):
            if answer[i] == '.' and answer[i+1] == '.':
                continue
            newWord += answer[i]
            if i == len(answer) - 2:
                newWord += answer[i+1]

    newWord = newWord.strip(".")

    if len(newWord) == 0:
        newWord = 'a'

    if len(newWord) >= 16:
        newWord = newWord[:15]

    newWord = newWord.strip(".")

    if len(newWord) <= 2:
        while(len(newWord) < 3):
            newWord += newWord[-1]
    return newWord

solution("b")