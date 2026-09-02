def solution(triangle):
    answer = 0
    dp = []
    height = len(triangle)
    
    for i in range(height):
        dp1=[0]*len(triangle[i])
        dp.append(dp1)
    
    dp[0][0] = triangle[0][0]
    
    for j in range(1,height):
        for h in range(len(triangle[j])):
            # 처음과 마지막 사이.
            if h > 0 and h < len(triangle[j])-1:
                dp[j][h] = max(dp[j-1][h],dp[j-1][h-1]) + triangle[j][h]
            # 그 층의 마지막 수   
            elif h == len(triangle[j])-1:
                dp[j][h] = dp[j-1][h-1] + triangle[j][h]
            # h == 0 일때 즉, 그 층의 첫번째일때
            else:
                dp[j][h] = dp[j-1][h] + triangle[j][h]
    
    return max(dp[-1])