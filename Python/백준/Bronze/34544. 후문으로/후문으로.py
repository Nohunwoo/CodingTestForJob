# Bronze 2
n= int(input())

backdoor = 1
for i in range(n):
    front, back = map(int, input().split())
    if front < 0 and back > 0:
        backdoor += back - front -1
    elif front > 0 and back < 0:
        backdoor += back - front +1
    else :
        backdoor += back - front

if(backdoor>0):
    print(backdoor)

else:
    print(backdoor-1)