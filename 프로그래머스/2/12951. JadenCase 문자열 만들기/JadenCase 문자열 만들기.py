def solution(s):
    answer = []
    # 공백 하나를 기준으로 분리합니다.
    s_list = s.split(' ')
    
    for word in s_list:
        # capitalize()는 빈 문자열('')이나 숫자로 시작하는 문자열도 에러 없이 처리합니다.
        answer.append(word.capitalize())
        
    # 분리했던 기준인 공백(' ')으로 다시 합쳐서 반환합니다.
    return ' '.join(answer)