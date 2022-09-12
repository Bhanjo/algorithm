import sys
input = sys.stdin.readline

n = int(input())
answer = []

temp = []
visit = [False for _ in range(10)]
sets = {}
divNum = []

def permu(cnt, target):
    if len(temp) == cnt:
        ans = ''.join(map(str, temp))
        # 길이 cnt개의 조합을 divNum에 임시저장
        if ans[::-1] not in sets:
            sets[ans[::-1]] = 1
            divNum.append(int(ans[::-1]))
        return
    
    # 0~9 숫자를 가지고 조합 만들기
    for i in range(target,10):
        if not visit[i]:
            temp.append(i)
            visit[i] = True
            permu(cnt, i)
            visit[i] = False
            temp.pop()

# i = 자릿수
for i in range(1, 11):
    permu(i,0)
    divNum.sort() # 자릿수별 조합을 올바르게 정렬
    answer.extend(divNum)
    divNum = []

print(int(answer[n]) if len(answer) > n else -1)