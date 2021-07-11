from abc import abstractmethod


def myCode():
    sugar = int(input())
    small = 0

    while(True):
        if(int(sugar % 5) == 0):
            print(int(sugar/5) + small)
            break
        elif(sugar < 0):
            print(-1)
            break
        sugar = sugar - 3
        small += 1
    

def main():
    myCode()
if __name__ == '__main__':
    main()