while(True):
    # 이번 문제에는 종료 조건이 없으니 try except로 에러 발생 시 break
    try :
        a,b = map(int, input().split())
        print(a+b)
    except :
        break
