def myCode() :
    a = int(input())
    num = list(map(int, input().split()))
    maxNum = max(num)

    for i in range(len(num)) :
            num[i] = num[i]/maxNum*100

    result = 0
    for i in range(len(num)) :
        result += num[i]
    result /= len(num)
    print(result) 
    

def bestCode() :
    a = int(input())
    num = list(map(int, input().split()))
    maxNum = max(num)

    for i in range(len(num)) :
        num[i] = num[i]/maxNum*100

    avgNum = sum(num)/len(num)
    print(avgNum)

def main() :
    myCode()
    bestCode()

if __name__ == '__main__' :
    main()