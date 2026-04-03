def solution(stones, k):
    l,r = 1,max(stones)
    
    while l <= r:
        mid = (l+r)//2
        cnt = 0
        
        for s in stones:
            if s-mid < 0:
                cnt +=1
                if cnt>= k:
                    break
            else:
                cnt = 0
                
        if cnt >= k:
            r = mid-1
        else:
            l = mid+1
    return r


