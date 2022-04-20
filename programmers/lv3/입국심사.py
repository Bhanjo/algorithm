def solution(n, times):
    answer = 0
    start, end = 1, max(times)*n
    while(start <= end):
        mid, donePeople= (start + end) // 2, 0
        for i in times:
            donePeople += mid // i
            if donePeople >= n: break
        if donePeople >= n:
            end = mid - 1
            answer = mid
        if donePeople < n:
            start = mid + 1
    return answer