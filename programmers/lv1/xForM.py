# def solution(x, n):
#     answer = []
#     for i in range(x, x*n + 1):
#         answer.append(i*x)
#         if i*x == x*n:
#             break
#     print(answer)
#     return answer

# sol2
def solution2(x, n):
    answer = [i * x + x for i in range(n)]
    return answer
