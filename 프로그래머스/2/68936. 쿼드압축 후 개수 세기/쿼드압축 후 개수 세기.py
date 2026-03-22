def solution(arr):
    zero,one = 0,0
    n = len(arr)
    
    def compress(x,y,size):
        nonlocal zero,one
        val = arr[x][y]
        
        for i in range(x,x+size):
            for j in range(y,y+size):
                if val != arr[i][j]:
                    half = size//2
                    compress(x,y,half)
                    compress(x+half,y,half)
                    compress(x,y+half,half)
                    compress(x+half,y+half,half)
                    return
                
        if val == 0:
            zero +=1
        else:
            one+=1
            
    compress(0,0,n)
    return [zero,one]
