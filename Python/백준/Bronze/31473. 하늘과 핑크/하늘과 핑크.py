import math

hair = int(input())
pink_list = list(map(int, input().split()))
sky_list = list(map(int, input().split()))

pink_sum = sum(pink_list)
sky_sum = sum(sky_list)

a = sky_sum // math.gcd(pink_sum,sky_sum)
b = pink_sum // math.gcd(pink_sum,sky_sum)
    
print(f'{a} {b}')