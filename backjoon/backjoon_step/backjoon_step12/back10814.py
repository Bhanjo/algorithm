def myCode():
    t = int(input())
    peoples = []

    for _ in range(t):
        age, name = map(str, input().split())
        age = int(age)
        peoples.append([age,name])

    sort_people = sorted(peoples, key=lambda x : (x[0]))
    
    for i in sort_people:
        print(i[0], i[1])

def main():
    myCode()
if __name__ == '__main__':
    main()