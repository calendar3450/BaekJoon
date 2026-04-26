def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for idx, num in enumerate(numbers):
        while stack and numbers[stack[-1]] <num:
            j = stack.pop()
            answer[j] = num
        stack.append(idx)
        
    return answer