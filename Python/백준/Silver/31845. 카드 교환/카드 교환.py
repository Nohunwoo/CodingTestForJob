from collections import deque
card, turn = map(int, input().split())
pair_card = list(map(int, input().split()))

pair_card.sort(reverse=True)
pair_card = deque(pair_card)
max_score = 0

for i in range(turn):
    if len(pair_card) == 0:
        break
    elif pair_card[0] < 0:
        break
    max_score += pair_card[0]
    pair_card.popleft()
    if len(pair_card) == 0:
        break
    pair_card.pop()

print(max_score)