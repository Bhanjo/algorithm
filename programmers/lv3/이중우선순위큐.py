import heapq

def solution(operations):
    answer = [0,0]
    maxHeap, minHeap = [],[]
    candidate = []

    for i in operations:
        op, val = map(str, i.split())
        val = int(val)
        if op == 'I':
            heapq.heappush(maxHeap, (-val, val))
            heapq.heappush(minHeap, val)
        if op == 'D' and val == -1 and len(minHeap) > 0:
            heapq.heappop(minHeap)
        elif op == 'D' and val == 1 and len(maxHeap) > 0:
            heapq.heappop(maxHeap)

        if len(maxHeap) == 0 or len(minHeap) == 0:
            maxHeap = []
            minHeap = []

    for i in maxHeap:
        if i[1] in minHeap:
            candidate.append(i[1])

    if len(candidate) > 0:
        answer = [max(candidate), min(candidate)]
    return answer

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
