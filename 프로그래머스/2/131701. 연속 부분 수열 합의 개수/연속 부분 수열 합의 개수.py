def solution(elements):
    answer = set()
    n = len(elements)
    elements = elements + elements
    
    # 총 몇개의 합인지
    for i in range(n):
        current = 0
        for j in range(n):
            current +=elements[i+j]
            answer.add(current)
                
    return len(answer)