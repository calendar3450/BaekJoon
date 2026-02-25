def solution(sequence, k):
    answer = [0,99999999999]
    if k in sequence:
        ans = sequence.index(k)
        return [ans,ans]
    
    n = len(sequence)
    left , right = 0,0
    cur_sum = 0
    
    while right < n:
        cur_sum +=sequence[right]
        
        while cur_sum >k:
            cur_sum -= sequence[left]
            left +=1
        
        
                
        if cur_sum == k:
            if answer[1]-answer[0] > right-left:
                answer = [left,right]
                cur_sum -=sequence[left]
                left+=1
        right +=1
        
    return answer
