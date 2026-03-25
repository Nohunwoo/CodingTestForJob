change = int(input())

ball = 1
for i in range(change):
    x,y = map(int, input().split())
    if x == ball:
        ball = y
    elif y == ball:
        ball = x

print(ball)