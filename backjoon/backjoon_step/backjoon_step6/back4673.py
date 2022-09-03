def selfNum(n) :
    # 자기자신 + 자릿수로 나눈 리스트의 합
    n = n+sum(map(int,str(n)))
    return n

a = [0]*10001
for i in range(1, 10001) :
    a[i] = selfNum(i)

for i in range(1, 10001) :
    # 셀프넘버? : 생성자가 없는 숫자
    if(i not in a) :
        print(i)
