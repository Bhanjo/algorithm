def solution(rows, columns, queries):
    box = [] * rows
    answer = []
    for i in range(rows):
        boxCol = [(j + 1) + (columns*i) for j in range(columns)]
        box.append(boxCol)
    
    for startX, startY, endX, endY in queries:
        temp = box[startX-1][startY-1]
        minValue = temp
        # 왼쪽 세로 (아래 -> 위)
        for i in range(startX - 1, endX - 1):
            currValue = box[i + 1][startY - 1]
            box[i][startY - 1] = currValue
            minValue = min(minValue, currValue)
        # 아래 가로 (오른쪽 -> 왼쪽)
        for i in range(startY - 1, endY - 1):
            currValue = box[endX - 1][i + 1]
            box[endX - 1][i] = currValue
            minValue = min(minValue, currValue)
        # 오른쪽 세로 (위 -> 아래)
        for i in range(endX - 1, startX - 1, -1):
            currValue = box[i - 1][endY - 1]
            box[i][endY - 1] = currValue
            minValue = min(minValue, currValue)
        # 위 가로 (왼쪽 -> 오른쪽)
        for i in range(endY - 1, startY - 1, -1):
            currValue = box[startX - 1][i - 1]
            box[startX-1][i] = currValue
            minValue = min(minValue, currValue)
        # 마지막 바뀌지 않았던 수 바꾸기
        box[startX - 1][startY] = temp
        answer.append(minValue)
        
    return answer