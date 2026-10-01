def solution(n, l, r):
    def count(level, length):
        """level번째 비트열의 앞 length칸에 있는 1의 개수"""
        if length == 0:
            return 0

        if level == 0:
            return 1  # 0번째 비트열은 "1"

        block_length = 5 ** (level - 1)
        block_ones = 4 ** (level - 1)
        total = 0

        for block in range(5):
            taken = min(length, block_length)

            if taken == 0:
                break

            if block != 2:  # 가운데 구간은 전부 0
                if taken == block_length:
                    total += block_ones
                else:
                    total += count(level - 1, taken)

            length -= taken

        return total

    return count(n, r) - count(n, l - 1)