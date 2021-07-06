def myCode():
    numA, numB = list(input().split())

    numA_list = list(str(numA))
    numA_list.reverse()
    numA_reverse = "".join(numA_list)

    numB_list = list(str(numB))
    numB_list.reverse()
    numB_reverse = "".join(numB_list)
    
    if(numA_reverse > numB_reverse):
        print(numA_reverse)
    else:
        print(numB_reverse)

def bestCode():
    num1, num2 = input().split()
    num1 = int(num1[::-1])  # [::-1] : 역순
    num2 = int(num2[::-1])

    print(num1) if num1 > num2 else print(num2) # 삼항 연산자 표현식

def main():
    myCode()

if(__name__ == '__main__'):
    main()