def myCode():
    up, down, goal = map(int,input().split())
    move = goal - up
    if(move % (up - down) > 0):
        print(int(move / (up - down))+2)
    else:
        print(int(move / (up - down))+1)

def main():
    myCode()
if __name__ == "__main__":
    main()