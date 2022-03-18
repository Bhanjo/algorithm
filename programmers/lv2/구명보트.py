def solution(people, limit):
    people.sort(reverse=True)
    answer = 0
    maxWeight = 0
    minWeight = len(people) - 1
    while(maxWeight <= minWeight):
        answer += 1
        currWeight = people[maxWeight]
        maxWeight += 1
        if(currWeight < limit and maxWeight <= minWeight):
            if(currWeight + people[minWeight] <= limit):
                minWeight -= 1
    print(answer)
    return answer
solution([60,50,20,10], 100)
solution([70, 80, 50], 100)
solution([70, 50, 80, 50], 100)