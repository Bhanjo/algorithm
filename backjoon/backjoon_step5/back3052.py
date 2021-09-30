def myCode() :
    result = []
    cnt = 0
    for i in range(10) :
        a = int(input()) % 42
        if(a not in result) :
            result.append(a)
            cnt += 1
    print(cnt)

def bestCode() :
    result = []
    for i in range(10) :
        a = int(input())
        result.append(a % 42)
    result = set(result) #set으로 중복 제거
    len(result)
    print(result)

def main() :
    myCode()
    bestCode()

if __name__ == '__main__' :
    main()