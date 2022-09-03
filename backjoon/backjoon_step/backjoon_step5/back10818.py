import time

# 내 코드
def myCode() :
    numArr = []
    tc = int(input())
    a = list(map(int, input().split()))

    for i in range(tc) :
        numArr.append(a[i])

    numMax = max(numArr)
    numMin = min(numArr)

    print(numMin)
    print(numMax)

# 최적 코드
def bestCode() :
    # tip : 파이썬 배열 입력은 따로 언급이 없다면 입력 횟수 지정 안해도 된다
    a = int(input())
    b = list(map(int, input().split()))
    print('{} {}'.format(min(b), max(b)))

def main() :
    start = time.time()
    bestCode()
    print("베스트코드 시간 : ", time.time() - start)

    start2 = time.time()
    myCode()
    print("내 코드 시간 : ", time.time() - start2)

if __name__ == "__main__":
    main()
