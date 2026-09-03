def solution(word):
    alpha = ['A','E','I','O','U']
    answer = 0
    
    def backtracking(words):
        nonlocal answer
        
        if words == word:
            return True
        
        if len(words) <5:
            for i in alpha:
                answer +=1
                if backtracking(words+i):
                    return True
        
        return False
                
    backtracking('')
    
    return answer