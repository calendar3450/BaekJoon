def solution(a, b, g, s, w, t):
    answer = -1
    left, right = 0, 9999999999999999
    def check (mid):
        t_g,t_s,t_a = 0,0,0
        
        for i in range(len(g)):
            trips = mid//(2*t[i])
            if mid%(2*t[i]) >=t[i]:
                trips+=1
                
            t_g += min(w[i]*trips,g[i])
            t_s += min(w[i]*trips,s[i])
            t_a += min(g[i] + s[i], w[i]*trips)
            
        return t_g >= a and t_s >= b and t_a >= a+b
    
    while left <= right:
        mid = (left+right) // 2
        
        if check(mid):
            answer = mid
            right = mid-1
        else:
            left = mid+1
            
    return answer