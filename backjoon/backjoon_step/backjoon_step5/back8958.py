def myCode() :
    tc = int(input())
    for i in range(tc) :
        cnt = 0
        result = 0
        quize = list(input())
        for j in range(len(quize)) :
            if(quize.pop() == "O") :
                cnt += 1
            else :
                cnt = 0
            result += cnt
        print(result)

# def bestCode() :
    # 내 풀이와 비슷
        
def main() :
    myCode()
if __name__ == "__main__" :
    main()