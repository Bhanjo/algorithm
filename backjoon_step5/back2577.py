def myCode() :
    a = []
    for i in range(3) :
        a.append(int(input()))
    gop = a[0] * a[1] * a[2]
    
    digit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    cnt = 10
    while(True) :
        nanum = gop%cnt
        gop = int(gop/cnt)

        if(nanum == 0) :
            digit[0] += 1
        elif(nanum == 1) :
            digit[1] += 1
        elif(nanum == 2) :
            digit[2] += 1
        elif(nanum == 3) :
            digit[3] += 1
        elif(nanum == 4) :
            digit[4] += 1
        elif(nanum == 5) :
            digit[5] += 1
        elif(nanum == 6) :
            digit[6] += 1
        elif(nanum == 7) :
            digit[7] += 1
        elif(nanum == 8) :
            digit[8] += 1
        elif(nanum == 9) :
            digit[9] += 1

        if(gop <= 0) :
            break
    for i in range(10) :
        print(digit[i])

def bestCode() :
    a = []
    for i in range(3) :
        a.append(int(input()))

    # 곱셈의 결과를 문자열로 형변환 후 각 list로 저장
    result = list(str(a[0] * a[1] * a[2]))
    
    # 숫자(문자로 변환한) i가 result에 몇개 있나 count
    for i in range(10) :
        print(result.count(str(i)))

def main() :
    # myCode()
    bestCode()

if __name__ == "__main__" : 
    main()