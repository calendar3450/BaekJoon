from itertools import permutations

def solution(numbers):
    answer = 0
    result =set()
    n = len(numbers)
    
    for i in range(1,n+1):
        for j in permutations(numbers,i):
            result.add(int("".join(j)))
    
    result= list(result)
    max_num= max(result)
    dp=[True] * (max_num+1)
    dp[0] = dp[1] = False
    
    # 에라토스테네스의 체 사용
    for j in range(2, int(max_num**0.5) + 1):
        if dp[j]:
            for k in range(j * j, max_num + 1, j):
                dp[k] = False

    # 2. 미리 만들어둔 체(dp)로 소수 개수만 카운트
    for i in result:
        if dp[i]:
            answer += 1
        

            
    return answer