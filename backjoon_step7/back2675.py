def myCode():
    tc = int(input())
    for i in range(tc) :
        input_list = list(input().split())
        input_list_int = int(input_list[0])
        input_list_str = list(str(input_list[1]))
        for j in range(len(input_list_str)):
            for k in range(input_list_int):
                print(input_list_str[j], end='')
        print('')

def BestCode():
    t = int(input())
    for i in range(t):
        num, s = input().split() # split을 통해 변수 2개를 받음
        text = ''
        for i in s:
            text += int(num) * i # text에 문자i를 num번 반복해 추가
        print(text)

def main():
    myCode()

if(__name__ == '__main__'):
    main()