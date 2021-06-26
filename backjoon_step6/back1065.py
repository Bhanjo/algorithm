def hansu() :
    num = int(input())
    hansu = 0

    for i in range(1, num+1) :
        if i <= 99 :
            hansu += 1
        else :
            ckList = list(map(int, str(i)))
            if ckList[0] - ckList[1] == ckList[1] - ckList[2] :
                hansu += 1
    
    print(hansu)

def main() :
    hansu()
if (__name__ == "__main__") :
    main()