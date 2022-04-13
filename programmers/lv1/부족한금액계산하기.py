def solution(price, money, count):
    for i in range(1, count + 1):
        money -= price * i
    print(money * -1)
    return money * -1

# solution(3, 20, 4)
solution(1, 1000000000, 2500)