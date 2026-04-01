def solution(tickets):
    answer = []
    n = len(tickets)
    tickets.sort()
    check = [0] * (n+1)
    print(tickets)
    def DFS(arr, path):
        nonlocal answer
        if len(path) == n+1:
            answer=path[:]
            return True
        
        for i in range(n):
            if check[i] == 0 and arr == tickets[i][0]:
                check[i] = 1
                DFS(tickets[i][1],path+[tickets[i][1]])
                if answer:
                    return True
                check[i] = 0
        return False
    
    DFS("ICN", ["ICN"])
            
    return answer