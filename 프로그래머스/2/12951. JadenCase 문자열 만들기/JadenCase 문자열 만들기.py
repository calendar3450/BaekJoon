def solution(s):
    words = s.split(' ')

    for i in range(len(words)):
        words[i] = words[i].lower()

        if words[i] and words[i][0].isalpha():
            words[i] = words[i][0].upper() + words[i][1:]

    return ' '.join(words)