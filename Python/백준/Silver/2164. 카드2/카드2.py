from collections import deque
n = int(input())
card = deque([])
for i in range(n,0,-1):
    card.append(i)

while len(card) != 1:
    card.pop()
    card.rotate(1)
print(card[0])