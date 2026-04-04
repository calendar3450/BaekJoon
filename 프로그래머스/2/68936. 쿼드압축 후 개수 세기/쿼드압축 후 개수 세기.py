def solution(arr):
    n = len(arr)
    one, zero = 0, 0
    
    def compress (start,end,size):
        nonlocal one, zero
        val = arr[start][end]
        half = size//2
        for i in range(start,start+size):
            for j in range(end,end+size):
                if arr[i][j] != val:
                    compress(start,end,half)
                    compress(start+half,end,half)
                    compress(start,end+half,half)
                    compress(start+half,end+half,half)
                    return
        if val == 1:
            one +=1
        else:
            zero +=1
            
    compress(0,0,n)
    
    return [zero,one]