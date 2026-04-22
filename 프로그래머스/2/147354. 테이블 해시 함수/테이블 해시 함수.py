def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x: (x[col-1],-x[0]))
    data_sum = []
    
    for i in range(row_begin-1, row_end):
        tmp= 0
        for j in data[i]:
            tmp += (j%(i+1))
            
        data_sum.append(tmp)
    
    if len(data_sum) == 2:
        return data_sum[0] ^ data_sum[1]
    
    elif len(data_sum) == 1:
        return data_sum[0]
    
    else:
        init = data_sum[0] ^ data_sum[1]
        
    for i in range(2,len(data_sum)):
        init = init ^ data_sum[i]
    
    return init