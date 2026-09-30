def solution(sticker):
    one_before = 0
    two_before = 0
    n = len(sticker)
    
    if n == 1:
        return sticker[0]
    
    for num in sticker[:-1]:
        cur_val = max(one_before, two_before + num)
        one_before,two_before = cur_val, one_before
        
    result_fir = one_before
    one_before = 0
    two_before = 0
    
    for num in sticker[1:]:
        cur_val = max(one_before, two_before + num)
        one_before,two_before = cur_val, one_before
        
    result_sec = one_before
    

    return max(result_sec,result_fir)