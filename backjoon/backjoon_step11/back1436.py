def myCode():
    num = int(input())
    i = 0
    cnt = 0
    while(True):
        i += 1
        if("666" in str(i)):
            cnt += 1
        if(cnt == num):
            print(i)
            break
            

def main():
    myCode()
if __name__ == '__main__':
    main()