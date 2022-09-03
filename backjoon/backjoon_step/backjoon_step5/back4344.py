def myCode() :
    tc = int(input())
    for i in range(tc) :
        num = list(map(int, input().split()))
        avg = (sum(num)-num[0])/(len(num)-1)
        cnt = 0
        for j in range(1, len(num)) :
            if(num[j] > avg) :
                cnt += 1
        result = (cnt/(len(num)-1))*100
        print(f'{result:.3f}%')

def bestCode() :
    tc = int(input())
    for i in range(tc) :
        num = list(map(int, input().split()))
        avg = sum(num[1:])/num[0] #num의 index 1부터 끝 index까지 sum
        cnt = 0
        for j in num[1:] :
            if(j > avg) : #파이썬 for문 특성으로 j에 점수 각각을 선언
                cnt += 1
        result = cnt/num[0]*100
        print(f'{result:.3f}%') ##f-string 표기법

def main() :
    # myCode()
    bestCode()
if __name__ == "__main__" :
    main()