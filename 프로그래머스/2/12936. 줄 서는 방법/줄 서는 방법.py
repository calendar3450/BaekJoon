import math

def solution(n, k):
    nums = list(range(1, n + 1))
    k -= 1  # 0-index로 변환
    answer = []

    for i in range(n, 0, -1):
        f = math.factorial(i - 1)
        idx = k // f
        k %= f
        answer.append(nums.pop(idx))

    return answer