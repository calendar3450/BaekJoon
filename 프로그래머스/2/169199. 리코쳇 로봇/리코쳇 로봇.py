from collections import deque

def solution(board):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    rows = len(board)
    cols = len(board[0])

    # 시작 위치: (행, 열)
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'R':
                sr, sc = r, c

    queue = deque([(sr, sc, 0)])
    visited = {(sr, sc)}

    while queue:
        r, c, move = queue.popleft()

        if board[r][c] == 'G':
            return move

        for dr, dc in directions:
            # 각 방향의 출발점은 현재 위치
            nr, nc = r, c

            while True:
                next_r = nr + dr
                next_c = nc + dc

                # 다음 칸이 보드 밖이면 현재 위치에서 멈춤
                if not (0 <= next_r < rows and
                        0 <= next_c < cols):
                    break

                # 다음 칸이 장애물이면 현재 위치에서 멈춤
                if board[next_r][next_c] == 'D':
                    break

                # 이동 가능한 경우에만 좌표 변경
                nr, nc = next_r, next_c

            if (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, move + 1))

    return -1