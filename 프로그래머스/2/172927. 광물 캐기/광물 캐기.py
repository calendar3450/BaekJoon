def solution(picks, minerals):
    answer = 0
    diamond_pick = picks[0]
    iron_pick = picks[1]
    stone_pick = picks[2]
    n = len(minerals)
    arrange_minerals = []
    
    for i in range(n//5):
        arrange_minerals.append(minerals[i*5:(i+1)*5])
    
    if n % 5 > 0:
        arrange_minerals.append(minerals[(n//5)*5:])
    
    if diamond_pick >= len(arrange_minerals):
        return len(minerals)
    
    total_picks = sum(picks)
    arrange_minerals = arrange_minerals[:total_picks] 
    
    # 광물중 다이아가 가장 많은 곳에 다이아 곡갱이 쓰면 됌. 아니면 철 아니면 돌
    arrange_minerals.sort(key = lambda x: sum(25 if m=='diamond' else 5 if m=='iron' else 1 for m in x), reverse=True)
    cur = 0
    
    print(arrange_minerals)
    
    # 다곡 사용
    for i in range(diamond_pick):
        answer += len(arrange_minerals[cur])
        cur +=1
        if cur >= len(arrange_minerals):
            return answer
        
    # 철곡 사용
    for i in range(iron_pick):
        arrange_mineral = arrange_minerals[cur]
        for miner in arrange_mineral:
            if miner == 'diamond':
                answer += 5
            else:
                answer +=1
        cur +=1
        if cur >= len(arrange_minerals):
            return answer
    
    # 돌곡 사용
    for i in range(stone_pick):
        arrange_mineral = arrange_minerals[cur]
        for miner in arrange_mineral:
            if miner == 'diamond':
                answer += 25
            elif miner == 'iron':
                answer += 5
            else:
                answer += 1
        cur +=1
        if cur >= len(arrange_minerals):
            return answer
        
    return answer