def solution(n, s):
    answer = []
    if n> s:
        return [-1]
    
    if s%n == 0:
        answer = [s//n for i in range(n)]
    else:
        answer = [s//n for i in range(n)]
        rest = s%n
        for j in range(rest):
            answer[j] +=1
            
    answer.sort()
    return answer