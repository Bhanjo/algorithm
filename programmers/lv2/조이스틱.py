def solution(name):
    answer = 0
    minMove = len(name) - 1
    for idx, word in enumerate(name):
        # 알파벳 찾기 카운트
        answer += min(ord(word) - ord('A'), ord('Z') - ord(word) + 1)
        # 위치 이동 카운트
        nextIdx = idx + 1
        while nextIdx < len(name) and name[nextIdx] == 'A':
            nextIdx += 1
        minMove = min(minMove, 2 * idx + len(name) - nextIdx, idx + 2 * (len(name) - nextIdx))
    answer += minMove
    return answer
solution("JAZ")