def solution(n, stations, w):
    answer = 0
    pos = 1
    cover = 2*w +1
    
    for s in stations:
        left = s-w
        right = s+w
        
        if pos < left:
            gap = left - pos
            answer += (gap+cover -1) // cover
        
        pos = right +1
    
    if pos <=n:
        gap = n-pos +1
        answer += (gap+cover-1) //cover
            
    return answer