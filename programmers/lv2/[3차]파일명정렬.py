def solution(files):
    sortToFiles = {}
    nums = ''
    strs = ''
    for i in files:
        sortToFiles[i] = []
        for word in i:
            if len(nums) > 0 and not '0' <= word <= '9':
                break
            if '0' <= word <= '9':
                nums += word
            else:
                strs += word
        sortToFiles[i].append(strs.upper())
        sortToFiles[i].append(int(nums))
        nums = ''
        strs = ''
    
    answer = list(sortToFiles.items())
    answer.sort(key = lambda x: (x[1][0], x[1][1]))
    ans = []
    for i in answer:
        ans.append(i[0])
    return ans

# 정규식을 이용한 풀이
import re
def solution(files):
    temp = [re.split(r"([0-9]+)", s) for s in files]
    print(temp)
    sort = sorted(temp, key = lambda x: (x[0].lower(), int(x[1])))
    
    return [''.join(s) for s in sort]
solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])