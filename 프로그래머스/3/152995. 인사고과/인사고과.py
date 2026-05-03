def solution(scores):
    answer = 1
    wan = scores[0]
    sum_wan = sum(scores[0])
    
    scores.sort(key = lambda x: [-x[0],x[1]])
    
    max_b = 0
    
    for s in scores:
        if s[1] <max_b:
            if s== wan:
                return -1
        else:
            max_b = max(s[1],max_b)
            if sum(s) > sum_wan:
                answer +=1
                
    return answer
                