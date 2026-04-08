def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for idx, number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            cur = stack.pop()
            answer[cur] = number
        stack.append(idx)
    return answer