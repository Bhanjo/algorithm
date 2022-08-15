def solution(triangle):
    for i in range(1, len(triangle)):
        triangle[i][0] += triangle[i-1][0]
    for i in range(1, len(triangle)):
        triangle[i][i] += triangle[i-1][i-1]
    
    for i in range(2, len(triangle)):
        for j in range(1, i):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    
    return max(triangle[len(triangle)-1])