def solution(N, A):
    ans = [0 for _ in range(N+1)]
    maxVal = 0
    saveMaxVal = 0
    for i in A:
        if i <= N:
            if ans[i] < saveMaxVal: # 값 업데이트 하고 +1
                ans[i] = saveMaxVal
            ans[i] += 1
            maxVal = max(ans[i], maxVal)
        else:
            saveMaxVal = maxVal
    for i in range(N+1):
        if ans[i] < saveMaxVal:
            ans[i] = saveMaxVal
    return ans[1:]

print(solution(5,[3,4,4,6,1,4,4]))