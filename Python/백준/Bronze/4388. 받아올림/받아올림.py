while True :
    a, b = map(str, input().split())
    answer = 0
    if a == b == "0":
        break
    if len(a) < len(b) :
        a = '0'*(len(b)-len(a)) + a
    if len(a) > len(b) :
        b = '0'*(len(a)-len(b)) + b
    y = 0
    for i in range(len(a)-1,-1,-1):
        x = int(a[i]) + int(b[i]) + y
        if x >= 10:
            answer += 1
            y = 1
    print(answer)