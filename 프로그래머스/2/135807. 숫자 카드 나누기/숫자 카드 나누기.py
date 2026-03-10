import math
from functools import reduce

def get_gcd_list(numbers):
    return reduce(math.gcd, numbers)


def solution(arrayA, arrayB):
    answer = 0
    n = len(arrayA)
    A_gcd = get_gcd_list(arrayA)
    B_gcd = get_gcd_list(arrayB)
    
    for i in range(n):
        if arrayB[i] % A_gcd == 0:
            A_gcd = 0
            break
    
    for i in range(n):
        if arrayA[i] % B_gcd == 0:
            B_gcd = 0
            break
    
    
    return max(A_gcd,B_gcd)