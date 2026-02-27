def solution(board):
    n = len(board)
    m = len(board[0])
    
    dp = [row[:] for row in board]
    max_len = 0
    
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                max_len = max(max_len, dp[i][j])
            elif dp[i][j] == 1:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1],dp[i-1][j-1])
                max_len = max(max_len, dp[i][j])
                
                

    return max_len *max_len