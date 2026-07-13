from collections import Counter
def solution(k, tangerine):
    answer = 0
    lis = []
    lis = list(Counter(tangerine).values())

    lis.sort(reverse=True)
    
    for li in lis:
        if k <=0:
            break
        k -= li
        answer+=1
        
    return answer