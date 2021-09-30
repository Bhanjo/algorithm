def myCode():
    num = int(input())
    people = []
    rank = [1] * num
    for _ in range(num):
        w, h = map(int, input().split())
        people.append([w, h])

    for i in range(len(people)):
        for j in range(len(people)):
            if( people[i][0] < people[j][0] and people[i][1] < people[j][1] ):
                rank[i] += 1
    
    for i in rank:
        print(i, end=(' '))

def main():
    myCode()
if __name__ == '__main__':
    main()