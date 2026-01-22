def soulution():
    N = int(input())
    numbers = list(map(int,input().split()))
    operations = list(map(int,input().split()))
    opers = {'+':operations[0],'-':operations[1],'*':operations[2],'/':operations[3]}
    maxValue= -9999999999
    minValue= 9999999999
    total = numbers[0]

    def backtracking(pos,total):
        nonlocal maxValue
        nonlocal minValue
        nonlocal numbers

        if pos == N-1:
            maxValue = max(maxValue,total)
            minValue = min(minValue,total)
            return
        
        for i in opers:
            if opers[i] !=0:
                opers[i] -=1
                if i == '+':
                    backtracking(pos+1,total+numbers[pos+1])
                elif i == '-':
                    backtracking(pos+1,total-numbers[pos+1])
                elif i == '*':
                    backtracking(pos+1,total*numbers[pos+1])
                else:
                    if total <0:
                        backtracking(pos+1,-(-total//numbers[pos+1]))
                    else:
                        backtracking(pos+1,total//numbers[pos+1])
                opers[i] +=1

    backtracking(0,total)
    print(maxValue,minValue)
soulution()
            