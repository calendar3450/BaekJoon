def solution(sticker):
    answer = 0
    n = len(sticker)
    
    if n <= 2:
        return max(sticker)
    
    # 스티커 앞에 뜯었을때,
    dp = [0] * (n+1)
    dp[0] = sticker[0]
    dp[1] = dp[0]
    
    for i in range(2,n-1):
        dp[i] = max(dp[i-1], dp[i-2] + sticker[i])
    
    # 스티커 한칸 뒤에 뜯었을때,
    dp1 = [0] * (n+1)
    dp1[1] = sticker[1]
    
    for i in range(2,n):
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
        
    return max(max(dp1),max(dp))


