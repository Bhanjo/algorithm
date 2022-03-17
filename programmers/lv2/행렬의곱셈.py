def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        arrX = []
        for j in range(len(arr2[0])):
            hap = 0
            for k in range(len(arr2)):
                hap += (arr1[i][k] * arr2[k][j])
            arrX.append(hap)
        answer.append(arrX)
    return answer
solution([[1,2,3], [2,3,4]], [[1,2],[2,3],[3,4]])
solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])