def solution(numbers):
    answer = 0
    number_list = list(numbers)
    combination = []
    n = len(numbers)
    visited= [False] *n 
    
    def backtracking(cur_num):
        if len(cur_num) == len(numbers):
            if int(cur_num) not in combination:
                combination.append(int(cur_num))
            return
        
        for i in range(n):
            if visited[i]:
                continue
            visited[i] = True
            if int(cur_num+number_list[i]) >1:
                combination.append(int(cur_num+number_list[i]))
            backtracking(cur_num+number_list[i])
            visited[i] = False
            
    def findPrime(num):
        if num ==2:
            return True
        
        for i in range(2,int(num**0.5)+1):
            if num% i == 0:
                return False
        return True


    backtracking('')
    combin = list(set(combination))
    
    for i in combin:
        if findPrime(i):
            answer+=1
            
    return answer