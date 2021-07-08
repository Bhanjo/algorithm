def myCode():
    word = input()
    croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    cnt = 0
    for i in range(len(croatia)):
        cnt += word.count(croatia[i])
    print(len(word)-cnt)

def bestCode():
    word = input()
    croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    for i in croatia:
        word = word.replace(i, '*') # 크로아티아 문자를 특정 문자 하나로 대체
    print(len(word))

def main():
    # myCode()
    bestCode()
if(__name__ == "__main__"):
    main()