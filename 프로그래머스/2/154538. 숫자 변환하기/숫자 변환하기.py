def solution(x, y, n):
    answer = 0
    dp= [9999999] * (y+1)
    dp[x] = 0
    
    for i in range(x,y):
        if dp[i] <9999999:
            if i *2 <=y:
                dp[i*2] = min(dp[i] +1 , dp[i*2])
            if i*3 <=y:
                dp[i*3] = min(dp[i]+1,dp[i*3])
            if i+n <=y:
                dp[i+n] = min(dp[i]+1,dp[i+n])
            
        
    return -1 if dp[y] == 9999999 else dp[y]