def solution():
    A,B = map(int,input().split())
    list_A = list(str(A))
    n = len(list_A)
    used= [False] *n
    curMax= -1

    def backtracking(C):
        nonlocal curMax

        if len(C) == n:
            if int(C) <= B:
                curMax = max(int(C), curMax)

            return
        
        for i in range(n):
            if used[i]:
                continue

            if len(C) == 0 and list_A[i] =='0':
                continue

            used[i] = True
            backtracking(C+list_A[i])
            used[i] = False

    backtracking('')
    print(curMax)
    

solution()