def myCode():
    num, hap = map(int,input().split()) # 개수와 숫자합
    card = list(map(int, input().split()))
    maxhap = 0

    for i in range(len(card)-2):
        for j in range(i+1, len(card)-1):
            for k in range(j+1, len(card)):
                if(card[i] + card[j] + card[k] == hap):
                    maxhap = card[i] + card[j] + card[k]
                    break
                elif(card[i] + card[j] + card[k] <= hap):
                    if (maxhap <= card[i] + card[j] + card[k]):
                        maxhap = card[i] + card[j] + card[k]
    print(maxhap)

def bestCode():
    num, hap = map(int,input().split())
    card = list(map(int, input().split()))
    length = len(card)
    maxhap = 0
    
    for i in range(0,length - 2):
        for j in range(i + 1,length - 1):
            for k in range(j + 1,length):
                if(card[i] + card[j] + card[k] < hap):
                    continue
                else:
                    maxhap = max(maxhap, card[i] + card[j] + card[k])
    print(maxhap)

def main():
    myCode()
if __name__ == '__main__':
    main()