from collections import Counter

def solution(gems):
    answer = [0,99999999999999]
    set_gems = list(set(gems))
    cnt_gems = Counter(gems)

    m = len(set_gems)
    n = len(gems)
    
    if m == 1:
        return [1,1]
    
    l = 0
    dict_win = {}
    
    for r in range(n):
        if gems[r] in dict_win:
            dict_win[gems[r]] +=1
        else:
            dict_win[gems[r]] = 1
            
        while len(dict_win) == m:
            if answer[1] - answer[0] > r-l:
                answer = [l+1,r+1]
                
            dict_win[gems[l]] -=1
            
            if dict_win[gems[l]] == 0:
                del dict_win[gems[l]]
            l+=1
            
    return answer