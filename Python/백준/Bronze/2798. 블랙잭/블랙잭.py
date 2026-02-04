from itertools import combinations

card, max_sum = map(int, input().split())
numbers = list(map(int, input().split()))
result = 0

for cards in combinations(numbers, 3):
    temp_sum = sum(cards)
    
    if temp_sum <= max_sum:
        result = max(result, temp_sum)

print(result)