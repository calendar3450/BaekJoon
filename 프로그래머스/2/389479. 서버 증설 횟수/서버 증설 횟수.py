def solution(players, m, k):
    answer = 0
    cur_server = [0] * 50
    
    for i in range(24):
        # 증설 해야 하는 경우
        if players[i] >= (cur_server[i] + 1) * m:
            added = (players[i] // m) - cur_server[i]
            for j in range(k):
                cur_server[i+j] += added
            answer += added
            
    return answer