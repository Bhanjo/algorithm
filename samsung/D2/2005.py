T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    triangle = [[1]*i for i in range(n+1)]
    for i in range(3, n+1):
        for j in range(1, i-1):
            triangle[i][j] = (triangle[i-1][j-1] + triangle[i-1][j])

    print('#', end='')
    print(test_case)
    for i in range(1, n+1):
        for j in range(0, i):
            print(triangle[i][j], end=' ')
        print('')
