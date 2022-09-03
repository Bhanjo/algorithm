def myCode() :
    a = list(str(input()))
    cnt = [-1] * 26
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

    for i in range(26) :
        if(alphabet[i] in a) :
            cnt[i] = a.index(alphabet[i])
    for i in range(26) :
        print(cnt[i])

def bestCode() :
    word = input()
    alphabet = list(range(97,123)) # 아스키코드 알파벳 범위

    # find 함수 : 문자가 문자열 안에 있으면 첫 번째 위치를 표시, 없으면 -1
    for i in alphabet :
        print(word.find(chr(i)))

def main() :
    # myCode()
    bestCode()
if __name__ == "__main__" : 
    main()