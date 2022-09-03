# 나의 코드
def myCode() : 
    numArr = []
    for i in range(9) :
        numArr.append(int(input()))
    i = 0
    cnt = 1
    while(True) :
        if(numArr[i] == max(numArr)) :
            maxIndex = cnt
            break
        i += 1
        cnt += 1
    print(max(numArr), maxIndex)

# 최적 코드
def bestCode() : 
    num_list = []
    for i in range(9):
        num_list.append(int(input()))
        
    print(max(num_list))
    # tip : num_list.index는 index값을 반환해준다
    print(num_list.index(max(num_list))+1)

def main() :
    bestCode()
    myCode()

if __name__ == "__main__" : 
    main()