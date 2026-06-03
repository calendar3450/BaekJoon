def change_note(melody):
    # #이 붙은 음들을 단일 소문자 문자로 치환해주는 함수
    melody = melody.replace("C#", "c")
    melody = melody.replace("D#", "d")
    melody = melody.replace("F#", "f")
    melody = melody.replace("G#", "g")
    melody = melody.replace("A#", "a")
    return melody

def solution(m, musicinfos):
    answer = "(None)"  
    max_time = -1  
    
    m = change_note(m)
    
    for musicinfo in musicinfos:
        start, end, name, sound = musicinfo.split(',')
    
        # 재생 시간 계산
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        play_time = (end_h * 60 + end_m) - (start_h * 60 + start_m)
        
        # 악보 정보 치환
        sound = change_note(sound)
        sound_len = len(sound)
        
        # 실제 라디오에서 재생된 전체 멜로디 구성
        # 재생 시간이 악보보다 길면 반복하고, 짧으면 자름
        full_melody = (sound * (play_time // sound_len + 1))[:play_time]
        
        # 5. 조건 체크
        if m in full_melody:
            # 기존에 찾은 곡보다 재생 시간이 더 길 때만 정답 갱신
            # (시간이 같을 때는 먼저 입력된 곡이 우선이므로 > 연산자 사용)
            if play_time > max_time:
                max_time = play_time
                answer = name
                
    return answer
            