def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    print(max(land[len(land) - 1]))
    return max(land[len(land) - 1])
solution([[1,100,92,5],[2,105,1,9],[1,2,3,100]])
