def solution(arr):
    answer = [0,0]

    def divcon(startX, endX, startY, endY):
        targetNum = arr[startX][startY]
        if startX == endX == startY == endY:
            if targetNum == 0: answer[0] += 1
            else: answer[1] += 1
            return
        
        midX = (startX + endX) // 2
        midY = (startY + endY) // 2
        for i in range(startX, endX + 1):
            for j in range(startY, endY + 1):
                if arr[i][j] != targetNum:
                    divcon(startX, midX, startY, midY)
                    divcon(startX, midX, midY + 1, endY)
                    divcon(midX + 1, endX, startY, midY)
                    divcon(midX + 1, endX, midY + 1, endY)
                    return
        
        if targetNum == 0: answer[0] += 1
        else: answer[1] += 1

    divcon(0, len(arr) - 1, 0, len(arr) - 1)
    return answer

solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])

# 다른 풀이
def solution(arr):
    answer = [0, 0]

    def check(size, x, y):
        if size == 1:
            answer[arr[y][x]] += 1
            return
        else:
            first = arr[y][x]

            for dy in range(size):
                for dx in range(size):
                    if first != arr[y + dy][x + dx]:
                        check(size // 2, x, y)
                        check(size // 2, x + size // 2, y)
                        check(size // 2, x, y + size // 2)
                        check(size // 2, x + size // 2, y + size // 2)
                        return
            answer[first] += 1
    check(len(arr),0,0)


    return answer