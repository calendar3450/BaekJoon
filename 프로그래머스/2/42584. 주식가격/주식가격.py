def solution(prices):
    answer = []
    n = len(prices)
    
    for i in range(n):
        ans = 1
        for j in range(i+1,n):
            if prices[i] > prices[j] or j == n-1:
                answer.append(ans)
                break
            else:
                ans+=1
                
    answer.append(0)
    
    return answer