def solution(s):
    answer = ''
    s_list = list(s.split(' '))
    s_list2 =[]
    
    for s_l in s_list:
        s_list2.append(int(s_l))
        
    s_list2.sort()
    
    answer = str(s_list2[0])+" "+str(s_list2[-1])
    return answer