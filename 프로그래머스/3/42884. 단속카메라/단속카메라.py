def solution(routes):
    routes.sort(key=lambda x: x[1])  # 진출 지점 기준 정렬
    cam = -10**18
    answer = 0

    for ini, out in routes:
        if cam < ini:          # 카메라가 구간 밖이면 새로 설치
            answer += 1
            cam = out          # 가능한 가장 오른쪽(=이 구간의 끝)에 설치

    return answer