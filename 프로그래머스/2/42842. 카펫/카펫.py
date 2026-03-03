def solution(brown, yellow):
    answer = []
    m = 3
    n = 3
    
    while True:
        if m*n == brown + yellow and m+n == (brown//2)+2:
            answer =[m,n]
            break
        if m == n:
            m+=1
            n=3
        else:
            n+=1
        
    return answer