import sys

def myCode():
    t = int(sys.stdin.readline())
    new_list = []*t
    for _ in range(t):
        new_list.append(str(input()))
    sort_word  = list(set(new_list)) # 중복 제거
    word_list = sorted(sort_word, key=lambda x : (len(x), x)) # 정렬
    
    for i in word_list:
        sys.stdout.write(i + "\n")

def main():
    myCode()
if __name__ == '__main__':
    main()