def solution(n):
    answer = 1
    for i in range(1,n//2+1):
        total = 0
        for j in range(i,n):
            total +=j
            if total >n:
                break
            elif total == n:
                answer +=1 
                break
            
    return answer