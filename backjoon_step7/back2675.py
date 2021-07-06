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


def main():
    myCode()

if(__name__ == '__main__'):
    main()