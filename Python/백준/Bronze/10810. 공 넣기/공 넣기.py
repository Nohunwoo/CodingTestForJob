import sys
input = sys.stdin.readline

basket, times = map(int, input().split())
basket = [0] * basket
for _ in range(times):
    start, end, ball_num = map(int, input().split())
    basket[start-1:end] = [ball_num] * (end-start+1)

for i in basket:
    print(i, end=' ')