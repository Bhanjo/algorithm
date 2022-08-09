def solution(w,h):
    answer = w * h
    def gcd(w,h):
        minVal, maxVal = min(w,h), max(w,h)
        while(True):
            result = maxVal%minVal
            if result == 0:
                return minVal
            maxVal = minVal
            minVal = result
    return answer - (w+h-gcd(w,h))


# 2회차
def gcd(low,high):
    while(True):
        res = high % low
        if res == 0:
            return low
        high = low
        low = res

def solution(w,h):
    minVal, maxVal = min(w,h), max(w,h)
    answer = gcd(minVal, maxVal)
    return (w*h)-((w+h)-answer)


solution(8,12)