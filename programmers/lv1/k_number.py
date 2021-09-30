# K번째 수 문제
array = [1, 5, 3, 2, 4]
commands = [[1, 4, 1], [2, 5, 2]]


def solution(array, commands):
    # ex) 2,5,3 = 2~5까지 자르고 정렬
    answer = []
    for i in commands:
        start = i[0] - 1
        end = i[1]
        target = i[2] - 1
        new_array = array[start:end]
        new_array.sort()
        result = new_array[target]
        answer.append(result)
        print(new_array)
        print(result)
    return answer


solution(array, commands)
