import sys
input = sys.stdin.readline

def gcd(a,b):
    while b != 0:
        temp = a%b
        (a,b) = b,temp
    return abs(a)

word = input().strip().split(':')

num = gcd(int(word[0]), int(word[1]))
print(str(int(word[0])//num )+ ':' + str(int(word[1])//num))