def solution(x, y, n):
    if x== y:
        return 0
    
    answer = 0
    dp=[99999999] * (y+1)
    dp[x] = 0
    
    for i in range(x+1,y+1):
        if i//2<x and i//3<x and i-n<x:
            continue
            
        if i%6==0:
            dp[i] = min(dp[i//2]+1,dp[i//3]+1,dp[i-n]+1)
            
        elif i%2==0:
            dp[i] = min(dp[i//2]+1,dp[i-n] +1)
            
        elif i%3 ==0:
            dp[i] = min(dp[i//3] +1, dp[i-n]+1)
            
        else:
            dp[i] =dp[i-n]+1
        
    
    if dp[y] >= 99999999:
        return -1
    
    return dp[y]