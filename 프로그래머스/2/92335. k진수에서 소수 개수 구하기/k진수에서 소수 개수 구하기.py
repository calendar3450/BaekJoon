import math
def checkPrime(n):
    if n == 1:
        return False
    if n==2:
        return True
    
    if n%2 == 0:
        return False
    
    r = int(math.isqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True 

def solution(n, k):
    answer = 0
    result_num = ''
    digits = []
    
    while n > 0:
        digits.append(str(n % k))
        n //= k
    result_num = ''.join(reversed(digits))
    
    for i in result_num.split('0'):
        if i == '':
            continue
        if checkPrime(int(i)):
            answer+=1
        
    return answer