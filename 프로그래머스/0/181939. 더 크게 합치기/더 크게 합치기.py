def solution(a, b):
    answer = 0
    a_str = str(a)
    b_str = str(b)
    answer = max(int(a_str+b_str), int(b_str+a_str))
    return answer