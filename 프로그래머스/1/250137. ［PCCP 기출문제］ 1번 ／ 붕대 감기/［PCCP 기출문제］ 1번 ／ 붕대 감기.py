def solution(bandage, health, attacks):
    # 초기값들
    answer = 0
    cur_healthes = [0] *(attacks[-1][0])
    cur_healthes[0] = health
    cur_health = health
    attacks_ord = 0
    seq_suc = 0
    
    for i in range(len(cur_healthes)+1):
        # 공격 받았다면,
        if i == attacks[attacks_ord][0]:
            cur_health -=attacks[attacks_ord][1]
            if cur_health <= 0:
                return -1
            attacks_ord +=1
            seq_suc =0
        else:
            # 시전시간 최대치일때
            seq_suc +=1
            if seq_suc == bandage[0]:
                seq_suc = 0
                cur_health += bandage[1] + bandage[2]
            else:
                cur_health += bandage[1]
                
            # 최대 체력보다 높을떄
            if cur_health >= health:
                cur_health = health
        
    
    return cur_health