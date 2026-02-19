while True :
    a, b = map(int, input().split())
    if a == b == 0 :
        break
    half = abs(a-b)
    answer = min(a,b) - half
    print(answer)