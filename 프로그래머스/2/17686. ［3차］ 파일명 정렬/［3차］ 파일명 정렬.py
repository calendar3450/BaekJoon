def solution(files):
    storages = []

    for i, file in enumerate(files):
        storage = [i]
        strs = ""

        for ch in file:
            if len(storage) == 1 and ch.isdigit():
                storage.append(strs)   # head 확정
                strs = ""
            elif len(storage) == 2 and not ch.isdigit():
                # number 확정 (strs가 비어있거나 숫자 아니면 방어)
                storage.append(int(strs) if strs.isdigit() else 0)
                strs = ""

            strs += ch

        # 루프가 끝났는데 아직 number를 못 넣은 경우(파일이 숫자로 끝남 등)
        if len(storage) == 2:
            storage.append(int(strs) if strs.isdigit() else 0)
            strs = ""

        #  tail 저장 (없어도 빈 문자열로)
        if len(storage) == 3:
            storage.append(strs)
        else:
            # 혹시라도 형태가 깨졌으면 tail을 빈 문자열로 맞춤
            while len(storage) < 4:
                storage.append("")

        storages.append(storage)

    storages.sort(key=lambda x: (x[1].lower(), x[2]))
    return [files[s[0]] for s in storages]