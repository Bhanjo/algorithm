def myCode():
    a,b = map(int, input().split())
    
    num_list = [1 + i for i in range(a)] # 숫자 리스트 생성
    check_num = [False]*a
    arr = []

    def DFS(x):
        if x == b:
            print(*arr)
        
        for i in range(a):
            if check_num[i]:
                continue
            arr.append(num_list[i])
            check_num[i] = True
            DFS(x+1)
            arr.pop()
            check_num[i] = False # check 초기화
    DFS(0)

def main():
    myCode()
if __name__ == '__main__':
    main()