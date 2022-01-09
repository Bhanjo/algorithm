T = int(input())
for test_case in range(1, T + 1):
    word = input()
    result = 0
    for i in range(1, len(word)):
        if word[:i] == word[i:i*2]:
            result = i
            break
    print('#', end='')
    print(test_case, result)
