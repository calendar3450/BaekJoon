def solution(n, times):
    답 = 0
    왼,오 = 1,max(times)*n
    
    while 왼<=오:
        중 = (왼+오) //2
        사람 = 0
        for 심사 in times:
            사람 += 중//심사
            if 사람 >= n:
                break
                
        if 사람 >= n:
            답 = 중
            오 = 중 -1
            
        else:
            왼 = 중 +1
            
    return 답