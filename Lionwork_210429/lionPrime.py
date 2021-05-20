def is_prime(num) :
    ck_prime = True
    for i in range(2, num) :
        if(num%i == 0) :
            ck_prime = False

    if(ck_prime) :
        return True
    else : 
        return False

def calculate_prime_number(length) :
    n = length
    cklen = 0

    i = 2
    li = []

    while(True) :
        tf = is_prime(i)
        if(tf) :
            li.append(i)
            cklen += 1
        i += 1
        if(cklen == n):
            break
    
    return li

n = int(input('Length? : '))

print(calculate_prime_number(n))