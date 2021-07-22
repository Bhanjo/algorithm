def star(num):
    if(num == 1):
        return ('*')
    
    stars = star(num//3)
    lists = []

    for s in stars:
        lists.append(s*3)
    for s in stars:
        lists.append(s+ ' '*(num//3)+s)
    for s in stars:
        lists.append(s*3)
    return lists

num = int(input())
print('\n'.join(star(num)))