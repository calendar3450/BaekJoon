def solution(s):
    answer = 1
    n = len(s)
    
    for i in range(n-1):
        for j in range(i,n):
            tmp = s[i:j+1]
            if tmp == tmp[::-1]:
                if answer < len(tmp):
                    answer = len(tmp)
    
    
    return answer