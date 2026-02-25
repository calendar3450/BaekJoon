def solution(sequence, k):
    answer = [0,99999999999]
    n = len(sequence)
    
    if k in sequence:
        return [sequence.index(k),sequence.index(k)]
    
    left , right = 0,0
    cur_sum = 0
    
    while right <n:
        cur_sum += sequence[right]
        
        while cur_sum > k:
            cur_sum -= sequence[left]
            left+=1
        
        if cur_sum == k:
            if answer[1] - answer[0] > right - left:
                answer= [left,right]
        
        right +=1
    return answer