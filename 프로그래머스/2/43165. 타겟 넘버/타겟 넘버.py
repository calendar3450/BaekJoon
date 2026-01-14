def solution(numbers, target):
    answer = 0
    
    def BFS(current,i):
        nonlocal answer
        if len(current) == len(numbers):
            if sum(current) == target:
                answer +=1
            return
        
        current.append(numbers[i])
        BFS(current,i+1)
        current.pop(-1)
        current.append(-numbers[i])
        BFS(current,i+1)
        current.pop(-1)
        return
        
    BFS([],0)
        
    return answer