def solution(diffs, times, limit):
    l,r = 1, max(diffs)
    
    while l<= r:
        mid = (l+r) //2
        time = 0
        
        for idx,diff in enumerate(diffs):
            if diff <= mid:
                time += times[idx]
            else:
                time += (diff-mid) * (times[idx-1]+times[idx]) + times[idx]
                
        if time > limit:
            l = mid+1
        else:
            r = mid-1
            
    return l