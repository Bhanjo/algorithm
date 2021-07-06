def myCode():
    string = list(str(input().upper()))
    maxCnt = 0
    maxStr = 0
    for i in range(64,123):
        cnt = string.count(chr(i))
        if(cnt > maxCnt):
            maxCnt = cnt
            maxStr = i
        elif(cnt == maxCnt):
            maxStr = 63
    print(chr(maxStr))

def BestCode():
    words = input().upper()
    unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

    cnt_list = []
    for x in unique_words :
        cnt = words.count(x)
        cnt_list.append(cnt)  # count 숫자를 리스트에 append

    if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
        print('?')
    else :
        max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
        print(unique_words[max_index])

def main():
    myCode()

if(__name__ == '__main__'):
    main()