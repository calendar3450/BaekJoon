from collections import Counter

def solution(weights):
    answer =0
    cnt = Counter(weights)

    
    for i in cnt:
        # 비율이 같은경우
        if cnt[i] > 1:
            answer +=cnt[i]*(cnt[i]-1)//2
        
        if i *1/2 in cnt:
            answer += cnt[i] * cnt[i*1/2]
        if i*2/3 in cnt:
            answer += cnt[i] * cnt[i*2/3]
        if i*3/4 in cnt:
            answer += cnt[i] * cnt[i*3/4]
            
        
        
    
    return answer