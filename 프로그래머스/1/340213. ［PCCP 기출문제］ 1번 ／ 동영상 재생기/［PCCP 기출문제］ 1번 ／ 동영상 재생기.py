def solution(video_len, pos, op_start, op_end, commands):
    def to_sec(t):
        return int(t[:2]) * 60 + int(t[3:])
    
    # mm:ss 형식으로 변환하는 함수
    def to_str(s):
        return f"{s//60:02d}:{s%60:02d}"
    
    video_len = to_sec(video_len)
    pos = to_sec(pos)
    op_start = to_sec(op_start)
    op_end = to_sec(op_end)
    
    if op_start <= pos <= op_end:
        pos = op_end
        
    for com in commands:
        if com == 'next':
            pos = min(pos+10, video_len)
        else:
            pos = max(pos-10,0)
        
        if op_start <= pos <= op_end:
            pos = op_end
            
    return to_str(pos)