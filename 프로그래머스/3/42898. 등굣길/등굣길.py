def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    MOD = 1000000007
    dp[0][0] = 1
    check = False
    
    for i in range(m):
        if [i+1,1] in puddles:
            check = True
            dp[0][i] = 0
        elif not check:
            dp[0][i] = 1
        elif check:
            dp[0][i] = 0
            
    check = False
    
    for j in range(n):
        if [1,j+1] in puddles:
            check = True
            dp[j][0] = 0
        elif not check:
            dp[j][0] = 1
        elif check:
            dp[j][0] = 0
        
    for i in range(1,n):
        for j in range(1,m):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD
            if [j+1,i+1] in puddles:
                dp[i][j] = 0
        
    return dp[n-1][m-1]