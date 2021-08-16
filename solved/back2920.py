num = list(map(int, input().split()))
updown = ""

for i in range(len(num)-1):
    if(num[i] - num[i+1] == -1):
        updown = "ascending"
    elif(num[i] - num[i+1] == 1):
        updown = "descending"
    else:
        updown = "mixed"
        break
print(updown)