steps = list(map(int, input().split()))
check = False
if sum(steps) < 100:
    print("none")
else:
    for i in range(len(steps)):
        if i <= 1 and steps[i] > 100:
            print("hacker")
            check = True
            break
        elif i > 1 and i <= 3 and steps[i] > 200:
            print("hacker")
            check = True
            break
        elif i > 3 and i <= 5 and steps[i] > 300:
            print("hacker")
            check = True
            break
        elif i > 5 and i <= 7 and steps[i] > 400:
            print("hacker")
            check = True
            break
        elif i == 8 and steps[i] > 500:
            print("hacker")
            check = True
            break
    if not check:
        print("draw")
