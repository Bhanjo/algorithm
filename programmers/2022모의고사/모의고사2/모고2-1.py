# 100/100
def solution(number):
    answer = 0
    visit = []
    for i in range(len(number)-2):
        for j in range(i+1, len(number)-1):
            for k in range(j+1, len(number)):
                hap = number[i] + number[j] + number[k]
                arr = [i,j,k]
                arr.sort()
                if hap == 0 and arr not in visit:
                    visit.append(arr)
                    answer += 1
    return answer


# 2회차 (100/100)
def solution(number):
    answer = 0
    for i in range(len(number)-2):
        for j in range(i+1, len(number)-1):
            for k in range(j+1, len(number)):
                hap = number[i] + number[j] + number[k]
                if hap == 0:
                    answer += 1

    return answer