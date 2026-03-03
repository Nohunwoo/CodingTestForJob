import sys
input = sys.stdin.readline

sugar = int(input())
bags = 0 

while sugar >= 0:
    if sugar % 5 == 0:  
        bags += (sugar // 5)
        print(bags)
        break
    
    sugar -= 3  
    bags += 1

if sugar < 0:
    print('-1')