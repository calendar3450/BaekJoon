# def solution(number, k):
#     answer = ''
#     stack=[]
    
#     for num in number:
#         while k > 0 and stack and stack[-1] < num:
#             stack.pop()
#             k-=1
#         stack.append(num)
        
#     if k >0:
#         stack[:-k]
        
#     return ''.join(stack)

def solution(number, k):
    stack = []

    for digit in number:
        while k > 0 and stack and stack[-1] < digit:
            stack.pop()
            k -= 1

        stack.append(digit)

    # 끝까지 읽었는데도 삭제 횟수가 남았다면 뒤에서 삭제
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)