n= int(input())
for _ in range(n):
    a,b= map(int, input().split())
    answer = pow(a, b, 10)
    
    if answer == 0:
        print(10)
    else:
        print(answer)