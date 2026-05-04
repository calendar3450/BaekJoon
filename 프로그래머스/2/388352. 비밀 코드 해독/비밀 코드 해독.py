from itertools import combinations

def solution(n, q, ans):
    answer = 0
    len_q = len(q)
    
    for code in combinations(range(1,n+1),5):
        total_cnt = 0
        for i in range(len_q):
            cnt = len(set(code) & set(q[i]))  # 겹치는 숫자 개수
            
            if cnt != ans[i]:
                break
        
        else:
            answer +=1
    return answer