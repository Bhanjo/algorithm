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

# 2회차
def solution(rows, columns, queries):
    answer = []
    graph = []
    
    # 그래프 제작
    cnt = 1
    for i in range(rows):
        col = []
        for j in range(columns):
            col.append(cnt)
            cnt += 1
        graph.append(col)
    
    for x1, y1, x2, y2 in queries:
        minVal = 10**7
        temp = graph[x1-1][y1-1]
        # 왼쪽 세로
        for i in range(x1-1, x2-1):
            val = graph[i][y1-1]
            minVal = min(minVal, val)
            graph[i][y1-1] = graph[i+1][y1-1]
        # 아래 가로
        for i in range(y1-1, y2-1):
            val = graph[x2-1][i]
            minVal = min(minVal, val)
            graph[x2-1][i] = graph[x2-1][i+1]
        # 오른쪽 세로
        for i in range(x2-1, x1-1, -1):
            val = graph[i][y2-1]
            minVal = min(minVal, val)
            graph[i][y2-1] = graph[i-1][y2-1]
        # 위 가로
        for i in range(y2-1, y1-1, -1):
            val = graph[x1-1][i]
            minVal = min(minVal, val)
            graph[x1-1][i] = graph[x1-1][i-1]
        
        graph[x1-1][y1] = temp
        answer.append(minVal)
    
    return answer