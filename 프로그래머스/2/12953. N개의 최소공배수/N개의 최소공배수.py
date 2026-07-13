def solution(arr):
    answer = 0
    max_num = max(arr)
    cur_num = max_num
    while True:
        cur_true = True
        for i in arr:
            if cur_num % i != 0:
                cur_true = False
                break
        
        if cur_true:
            return cur_num
        else:
            cur_num +=max_num