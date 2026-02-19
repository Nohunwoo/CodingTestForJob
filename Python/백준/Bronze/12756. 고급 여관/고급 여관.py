a = list(map(int, input().split()))
b = list(map(int, input().split()))

while True :
    b[1] -= a[0]
    a[1] -= b[0]
    
    if b[1] < 1 or a[1] < 1:
        break

if a[1] < 1 and b[1] < 1:
    print("DRAW")    
elif a[1] > b[1]:
    print("PLAYER A")
elif a[1] < b[1]:
    print("PLAYER B")