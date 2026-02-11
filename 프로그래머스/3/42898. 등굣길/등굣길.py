def solution(m, n, puddles):
    answer = 0
    MOD = 1000000007
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    
    for y in range(n):
        for x in range(m):
            if [x+1, y+1] in puddles:
                dp[y][x] = 0
                continue
            if x == 0 and y == 0:
                continue
            left = dp[y][x-1] if x > 0 else 0
            up = dp[y-1][x] if y > 0 else 0
            dp[y][x] = (left + up) % MOD
        
    return dp[n-1][m-1]