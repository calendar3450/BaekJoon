def solution(numbers):
    answer = ''
    numbers_str = [str(number) for number in numbers]
    numbers_str.sort(key = lambda x : x*3, reverse = True)
    for i in numbers_str:
        answer += i
    
    if answer[0] == '0':
        return '0'
    else:
        return answer

