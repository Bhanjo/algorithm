def myCode():
    word = input()
    hap = [0]*8
    hap[0] = (word.count('A') + word.count('B') + word.count('C')) * 3
    hap[1] = (word.count('D') + word.count('E') + word.count('F')) * 4
    hap[2] = (word.count('G') + word.count('H') + word.count('I')) * 5
    hap[3] = (word.count('J') + word.count('K') + word.count('L')) * 6
    hap[4] = (word.count('M') + word.count('N') + word.count('O')) * 7
    hap[5] = (word.count('P') + word.count('Q') + word.count('R') + word.count('S')) * 8
    hap[6] = (word.count('T') + word.count('U') + word.count('V')) * 9
    hap[7] = (word.count('W') + word.count('X') + word.count('Y') + word.count('Z')) * 10
    print(sum(hap))

def bestCode():
    dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    word = input()
    hap = 0
    for i in range(len(word)): # 2차원 배열 이용
        for j in dial:
            if word[i] in j:
                hap += dial.index(j) + 3
    print(hap)


def main():
    myCode()
if(__name__ == "__main__"):
    main()