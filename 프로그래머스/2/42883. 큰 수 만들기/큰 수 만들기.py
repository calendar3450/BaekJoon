def solution(number, k):
    answer = ''
    stack = []
    
    for i in number:
        while stack and int(stack[-1]) < int(i) and k>0:
            stack.pop()
            k-=1
        
        stack.append(i)
        
    if k>0:
        stack = stack[:-k]
        
    for i in stack:
        answer += i
    
    return answer