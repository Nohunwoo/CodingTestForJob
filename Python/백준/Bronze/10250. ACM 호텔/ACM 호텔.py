import sys
input = sys.stdin.readline

n = int(input())
real_x = 0
real_y = 0
for i in range(n):
    stair,stage,number = map(int, input().split())
    real_y = number % stair
    if number % stair == 0:
        real_y = stair
    real_x = number // stair + 1
    if number % stair == 0:
        real_x -= 1
    
    real_number = real_y*100 + real_x
    print(real_number)