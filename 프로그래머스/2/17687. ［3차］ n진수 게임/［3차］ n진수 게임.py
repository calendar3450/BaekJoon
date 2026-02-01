def solution(n, t, m, p):
    answer = ''
    cur_num = 0
    cur_turn = 1
    digits = "0123456789ABCDEF"

    while len(answer) < t:
        tmp = cur_num

        # 진수 변환: 0 처리 필수
        if tmp == 0:
            cur_base = "0"
        else:
            cur_base = ''
            while tmp > 0:
                cur_base += digits[tmp % n]
                tmp //= n
            cur_base = cur_base[::-1]

        # 순서대로 말하기
        for ch in cur_base:
            if cur_turn == p and len(answer) < t:
                answer += ch
            cur_turn += 1
            if cur_turn > m:
                cur_turn = 1

        cur_num += 1

    return answer