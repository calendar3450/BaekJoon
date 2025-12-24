import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    number = int(input())
    candidate = [int(input()) for _ in range(number)]

    total = sum(candidate)
    max_vote = max(candidate)

    if candidate.count(max_vote) > 1:
        print("no winner")
        continue

    winner = candidate.index(max_vote) + 1

    if max_vote > total / 2:
        print("majority winner", winner)
    else:
        print("minority winner", winner)